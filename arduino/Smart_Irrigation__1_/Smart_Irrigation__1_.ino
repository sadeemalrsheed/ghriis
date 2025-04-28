//Welcome
//Electronics University

// Pin definitions
const int relayPin = 8;
const int sensor_pin = A0;  // Soil Sensor input at Analog PIN A0

// Sensor variables
int output_value;
int raw_sensor_value;

// Timing variables
unsigned long lastReadingTime = 0;
unsigned long lastRelayChangeTime = 0;
// unsigned long lastSerialAttempt = 0; // Removed for checkSerial removal
const unsigned long readingInterval = 1000;     // Reading interval in milliseconds
const unsigned long relayDebounceTime = 5000;   // 5 seconds between relay changes
// const unsigned long serialRetryInterval = 2000; // Removed for checkSerial removal

// Control variables
const int sensorThreshold = 20;                 // Moisture threshold percentage
bool relayState = false;                        // Track relay state (false = OFF, true = ON)
int consecutiveRelayOps = 0;                    // Count consecutive relay operations
const int maxConsecutiveOps = 3;                // Max operations before forced delay

// Diagnostic variables
unsigned long startTime;

void setup()
{
  // Initialize pins
  pinMode(relayPin, OUTPUT);
  pinMode(sensor_pin, INPUT);

  // Make sure relay is OFF at startup (HIGH for active LOW relay)
  digitalWrite(relayPin, HIGH);
  relayState = false; // Explicitly set initial state variable

  // Small delay to allow components to stabilize
  delay(1000);

  // Start serial communication
  Serial.begin(9600);

  // Wait briefly for serial port to open (especially on boards that reset on connect)
  delay(2000);

  // Initial status message
  if (Serial) {
    Serial.println("------------------------------");
    Serial.println("System starting...");
    Serial.println("Initial Relay State: OFF");
    Serial.println("Waiting for stabilization...");
  }

  // Longer stabilization period after Serial init
  delay(5000);

  startTime = millis();

  if (Serial) {
    Serial.println("System ready!");
    Serial.println("------------------------------");
  }
}

/* // Removed checkSerial() as it's often not helpful for USB serial issues
void checkSerial() {
  if (!Serial) {
    unsigned long currentTime = millis();
    if (currentTime - lastSerialAttempt > serialRetryInterval) {
      lastSerialAttempt = currentTime;
      Serial.end();
      delay(100);
      Serial.begin(9600);
      delay(100);
    }
  }
}
*/

void loop() {
  unsigned long currentTime = millis();

  // checkSerial(); // Removed checkSerial() call

  // Only proceed with sensor reading if enough time has passed
  if (currentTime - lastReadingTime >= readingInterval) {
    lastReadingTime = currentTime;

    // Read sensor value - store raw value for diagnostics
    raw_sensor_value = analogRead(sensor_pin);

    // Map sensor value to moisture percentage (adjust 550 and 10 based on YOUR sensor's dry/wet readings)
    // Ensure constrain is used correctly
    output_value = constrain(map(raw_sensor_value, 550, 10, 0, 100), 0, 100);

    // Print moisture value and diagnostics IF serial is available
    // IMPORTANT: Keep this message consistent for Python parsing
    if (Serial) {
      // Only print full status line if Serial connection appears active
      Serial.print("Raw: ");
      Serial.print(raw_sensor_value);
      Serial.print(" | Moisture: ");
      Serial.print(output_value);
      Serial.print(" | Relay: ");
      Serial.println(relayState ? "ON" : "OFF");
    }

    // --- Relay Control Logic ---
    bool shouldChangeRelay = false;
    bool newRelayState = relayState; // Assume no change initially

    // Determine if relay state needs to change based on threshold
    if (output_value < sensorThreshold) {
      // Condition: DRY -> Turn relay ON (if currently OFF)
      if (!relayState) { // If relay is currently OFF
        newRelayState = true; // Target state is ON
        // Check if enough time has passed since last change
        if (currentTime - lastRelayChangeTime >= relayDebounceTime) {
          shouldChangeRelay = true;
        }
      }
    } else {
      // Condition: WET -> Turn relay OFF (if currently ON)
      if (relayState) { // If relay is currently ON
        newRelayState = false; // Target state is OFF
        // Check if enough time has passed since last change
        if (currentTime - lastRelayChangeTime >= relayDebounceTime) {
          shouldChangeRelay = true;
        }
      }
    }

    // Execute relay change if needed and allowed
    if (shouldChangeRelay) {
      // Check consecutive operations limit
      consecutiveRelayOps++;
      if (consecutiveRelayOps > maxConsecutiveOps) {
        if (Serial) {
          Serial.println("WARNING: Max consecutive relay ops reached. Forced 10s delay.");
        }
        delay(10000); // Forced delay
        consecutiveRelayOps = 0; // Reset counter after delay
        // Skip the rest of the relay change logic in this iteration
      } else {
        // Log the intended change (briefly)
        if (Serial) {
            Serial.print("Attempting to change relay to: ");
            Serial.println(newRelayState ? "ON" : "OFF");
        }

        // *** ACTIVATE/DEACTIVATE RELAY ***
        // (LOW turns ON, HIGH turns OFF for typical relay modules)
        digitalWrite(relayPin, newRelayState ? LOW : HIGH);

        // Update state variables AFTER changing the relay
        relayState = newRelayState;
        lastRelayChangeTime = currentTime; // Record time of successful change

        // Short delay AFTER relay change for electrical stabilization
        delay(250); // Increased stabilization delay slightly

        // Confirm change completion
        if (Serial) {
          Serial.println("Relay change complete.");
          // Print the NEW status line immediately after successful change and delay
          Serial.print("Raw: ");
          Serial.print(raw_sensor_value);
          Serial.print(" | Moisture: ");
          Serial.print(output_value);
          Serial.print(" | Relay: ");
          Serial.println(relayState ? "ON" : "OFF");
        }
      }
    } else {
      // If no change was needed or allowed by debounce, reset the consecutive counter
      consecutiveRelayOps = 0;
    }
  } // End of reading interval check

  // Add a small delay at the end of the loop to prevent it from running too fast
  // This yields time to other processes (like serial handling)
  delay(10);
} // End of loop