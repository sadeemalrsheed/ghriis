from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS # type: ignore
import serial
import threading
import time
import re
import os
import json
import logging
from collections import deque
from datetime import datetime, timedelta

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('arduino_server')

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Serial port configuration for windows use com3 or com4
SERIAL_PORT = 'com3'
BAUD_RATE = 9600

# Global variables to store latest readings
sensor_data = {
    "moisture": 0,
    "raw": 0,
    "relay": "OFF",
    "timestamp": 0
}

# Store historical data - maximum records for 1 day (assuming 1 reading per minute)
MAX_HISTORY_RECORDS = 24 * 60
history_data = deque(maxlen=MAX_HISTORY_RECORDS)

system_status = {
    "arduino_connected": False,
    "last_error": "",
    "last_successful_read": 0,
    "reconnect_attempts": 0
}

# Serial connection management
ser_lock = threading.Lock()
ser = None

def manage_serial_connection():
    """Thread function to maintain serial connection"""
    global ser, sensor_data, system_status
    
    reconnect_delay = 2  # Initial reconnect delay in seconds
    max_reconnect_delay = 30  # Maximum reconnect delay
    last_history_save = 0  # Track when we last saved to history
    
    while True:
        try:
            with ser_lock:
                if ser is None or not ser.is_open:
                    try:
                        # Close if exists but not properly closed
                        if ser is not None:
                            try:
                                ser.close()
                            except:
                                pass
                        
                        # Try to open the serial port
                        new_ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
                        logger.info(f"Connected to {SERIAL_PORT}")
                        
                        # Wait for Arduino reset
                        time.sleep(2)
                        
                        # Flush any pending data
                        new_ser.reset_input_buffer()
                        new_ser.reset_output_buffer()
                        
                        # If we got here without exception, assign to global
                        ser = new_ser
                        system_status["arduino_connected"] = True
                        system_status["last_error"] = ""
                        system_status["reconnect_attempts"] = 0
                        reconnect_delay = 2  # Reset reconnect delay
                    except Exception as e:
                        system_status["arduino_connected"] = False
                        system_status["last_error"] = f"Connection error: {str(e)}"
                        system_status["reconnect_attempts"] += 1
                        logger.error(f"Failed to connect: {e}")
                        # Use exponential backoff for reconnect attempts
                        time.sleep(reconnect_delay)
                        reconnect_delay = min(reconnect_delay * 1.5, max_reconnect_delay)
                        continue
                
                # Try to read data if connected
                if ser and ser.is_open:
                    try:
                        if ser.in_waiting > 0:
                            line = ser.readline().decode('utf-8', errors='replace').strip()
                            if line:
                                process_serial_data(line)
                                
                                # Save to history every minute
                                current_time = time.time()
                                if current_time - last_history_save >= 60:  # Save every minute
                                    save_to_history()
                                    last_history_save = current_time
                    except Exception as e:
                        logger.error(f"Error reading serial: {e}")
                        system_status["arduino_connected"] = False
                        system_status["last_error"] = f"Read error: {str(e)}"
                        # Close connection for clean restart
                        try:
                            ser.close()
                        except:
                            pass
                        ser = None
                        time.sleep(1)
            
            # Short sleep between checks
            time.sleep(0.1)
                
        except Exception as e:
            logger.error(f"Error in connection manager: {e}")
            time.sleep(1)

def save_to_history():
    """Save current sensor data to history"""
    if sensor_data["timestamp"] > 0:
        history_data.append({
            "moisture": sensor_data["moisture"],
            "raw": sensor_data["raw"],
            "relay": sensor_data["relay"],
            "timestamp": sensor_data["timestamp"]
        })
        logger.info(f"Saved data point to history. Total points: {len(history_data)}")

def process_serial_data(line):
    """Process a line of data from the Arduino"""
    global sensor_data, system_status
    
    logger.info(f"Received: {line}")
    
    # Correct typo to match both "Moisture" and "Mositure"
    moisture_match = re.search(r'(?:Moisture|Mositure)\s*[:=]\s*(\d+)', line)
    if moisture_match:
        sensor_data["moisture"] = int(moisture_match.group(1))
    
    # Extract raw value
    raw_match = re.search(r'Raw\s*[:=]\s*(\d+)', line)
    if raw_match:
        sensor_data["raw"] = int(raw_match.group(1))
    
    # Extract relay status
    relay_match = re.search(r'Relay\s*[:=]\s*(ON|OFF)', line)
    if relay_match:
        sensor_data["relay"] = relay_match.group(1)
    
    current_time = time.time()
    sensor_data["timestamp"] = current_time
    system_status["last_successful_read"] = current_time



@app.route('/api/v1/status')
def get_status():
    """Get system status"""
    return jsonify({
        "status": "ok" if system_status["arduino_connected"] else "error",
        "message": "Connected to Arduino" if system_status["arduino_connected"] else system_status["last_error"],
        "arduino_connected": system_status["arduino_connected"],
        "last_error": system_status["last_error"],
        "last_successful_read": system_status["last_successful_read"],
        "reconnect_attempts": system_status["reconnect_attempts"],
        "server_time": time.time()
    })

@app.route('/api/v1/sensor')
def get_sensor_data():
    """Get sensor data"""
    return jsonify({
        "moisture": sensor_data["moisture"],
        "raw": sensor_data["raw"],
        "relay": sensor_data["relay"],
        "timestamp": sensor_data["timestamp"]
    })

@app.route('/api/v1/history')
def get_history_data():
    """Get historical sensor data for the past day"""
    # Convert deque to list for serialization
    one_day_ago = time.time() - (24 * 60 * 60)
    # Filter for only the last day's data
    day_history = [item for item in list(history_data) if item["timestamp"] > one_day_ago]
    return jsonify({
        "history": day_history,
        "count": len(day_history)
    })

@app.route('/api/v1/data')
def get_all_data():
    """Get all data (combined status and sensor data)"""
    return jsonify({
        "status": {
            "connected": system_status["arduino_connected"],
            "last_error": system_status["last_error"],
            "last_successful_read": system_status["last_successful_read"],
            "reconnect_attempts": system_status["reconnect_attempts"],
            "server_time": time.time()
        },
        "sensor": {
            "moisture": sensor_data["moisture"],
            "raw": sensor_data["raw"],
            "relay": sensor_data["relay"],
            "timestamp": sensor_data["timestamp"]
        }
    })

@app.route('/')
def index():
    """Serve the main HTML page"""
    return send_from_directory('.', 'moisture_monitor.html')

@app.route('/history')
def history_page():
    """Serve the history page"""
    return send_from_directory('.', 'moisture_history.html')

@app.route('/static/<path:path>')
def serve_static(path):
    """Serve static files"""
    return send_from_directory('static', path)

if __name__ == '__main__':
    # Make sure the static directory exists
    os.makedirs('static', exist_ok=True)
    
    # Start serial reading in a separate thread
    serial_thread = threading.Thread(target=manage_serial_connection, daemon=True)
    serial_thread.start()
    
    # Start the Flask server
    logger.info("Starting web server on http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
