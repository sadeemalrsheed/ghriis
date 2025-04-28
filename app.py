import os
import shutil
import time
import numpy as np
import pandas as pd 
from tensorflow.keras.preprocessing.image import ImageDataGenerator # type: ignore
from tensorflow.keras.models import load_model # type: ignore
import datetime

import requests 
from flask import Flask, render_template, request, redirect, flash, send_from_directory 
from werkzeug.utils import secure_filename 
from flask_apscheduler import APScheduler

from data import disease_map, details_map

import serial


if not os.path.exists('model.h5'):
    print("Downloading model...")
    url = "https://drive.google.com/uc?id=1JNggWQ9OJFYnQpbsFXMrVu-E-sR3VnCu&confirm=t"
    r = requests.get(url, stream=True)
    with open('./model.h5', 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Finished downloading model.")

# Load model from downloaded model file
model = load_model('model.h5')

# Create folder to save images temporarily
if not os.path.exists('./static/test'):
        os.makedirs('./static/test')

def predict(test_dir):
    test_img = [f for f in os.listdir(os.path.join(test_dir)) if not f.startswith(".")]
    test_df = pd.DataFrame({'Image': test_img})
    
    test_gen = ImageDataGenerator(rescale=1./255)

    test_generator = test_gen.flow_from_dataframe(
        test_df, 
        test_dir, 
        x_col='Image',
        y_col=None,
        class_mode=None,
        target_size=(256, 256),
        batch_size=20,
        shuffle=False)

    # FIX: Force steps to int
    predict = model.predict(test_generator, steps=int(np.ceil(test_generator.samples / 20)))

    # FIX: Convert predictions to int before indexing
    test_df['Label'] = np.argmax(predict, axis=-1).astype(int)
    test_df['Label'] = test_df['Label'].replace(disease_map)

    prediction_dict = {}
    for value in test_df.to_dict('index').values():
        image_name = value['Image']
        image_prediction = value['Label']
        prediction_dict[image_name] = {
            'prediction': image_prediction,
            'description': details_map[image_prediction][0],
            'symptoms': details_map[image_prediction][1],
            'source': details_map[image_prediction][2],
        }

    return prediction_dict



# Create an app
app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024 # maximum upload size is 50 MB
app.secret_key = "agentcrop"
ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg'}
folder_num = 0
folders_list = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# initialize scheduler
scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.init_app(app)

# Adding Interval Job to delete folder
@scheduler.task('interval', id='clean', seconds=1800, misfire_grace_time=900)
def clean():
    global folders_list
    try:
        for folder in folders_list:
            if (time.time() - os.stat(folder).st_ctime) / 3600 > 1:
                shutil.rmtree(folder)
                folders_list.remove(folder)
                print("\n***************Removed Folder '{}'***************\n".format(folder))
    except:
        flash("Something Went Wrong! couldn't delete data!")

scheduler.start()

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/condition', methods=['GET', 'POST'])

def get_disease():
    global folder_num
    global folders_list
    if request.method == 'POST':
        if folder_num >= 1000000:
            folder_num = 0
        # check if the post request has the file part
        if 'hiddenfiles' not in request.files:
            flash('No files part!')
            return redirect(request.url)

        files = request.files.getlist('hiddenfiles')

        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        app.config['UPLOAD_FOLDER'] = f"./static/test/predict_{folder_num:06d}_{timestamp}"

        # Create new folder
        os.makedirs(app.config['UPLOAD_FOLDER'])
        folders_list.append(app.config['UPLOAD_FOLDER'])
        folder_num += 1

        # Save files
        for file in files:
            if file.filename == '':
                flash('No Files are Selected!')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            else:
                flash("Invalid file type! Only PNG, JPEG/JPG files are supported.")
                return redirect('/')

        try:
            if len(os.listdir(app.config['UPLOAD_FOLDER'])) > 0:
                diseases = predict(app.config['UPLOAD_FOLDER'])
                print("Predictions:", diseases)
                return render_template('show_prediction.html',
                                       folder=app.config['UPLOAD_FOLDER'],
                                       predictions=diseases)
        except Exception as e:
            print("Prediction Error:", e)
            return redirect('/')
    return render_template('condition.html')

@app.route('/plants')
def show_plants():
    return render_template('plants.html')

# Central Region
@app.route('/nerium')
def nerium():
    return render_template('nerium.html')

@app.route('/ziziphus')
def ziziphus():
    return render_template('ziziphus.html')

@app.route('/acacia')
def acacia():
    return render_template('Acacia.html')

# Western Region
@app.route('/bougainvillea')
def bougainvillea():
    return render_template('Bougainvillea.html')

@app.route('/citrus')
def citrus():
    return render_template('Citrus.html')

@app.route('/ficus-benjamina')
def ficus_benjamina():
    return render_template('Ficus Benjamina.html')

# Eastern Region
@app.route('/date-palm')
def date_palm():
    return render_template('Date Palm.html')

@app.route('/jojoba')
def jojoba():
    return render_template('Jojoba.html')

@app.route('/acacia-rigidula')
def acacia_rigidula():
    return render_template('Acacia Rigidula.html')

# Northern Region
@app.route('/lavender')
def lavender():
    return render_template('Lavender.html')

@app.route('/rosemary')
def rosemary():
    return render_template('Rosemary.html')

@app.route('/thyme')
def thyme():
    return render_template('Thyme.html')

# Southern Region
@app.route('/sage')
def sage():
    return render_template('Sage.html')

@app.route('/oregano')
def oregano():
    return render_template('Oregano.html')

@app.route('/basil')
def basil():
    return render_template('Basil.html')

def get_arduino():
    try:
        return serial.Serial('COM3', 9600, timeout=2)
    except serial.SerialException as e:
        print("Error opening serial port:", e)
        return None


@app.route('/device')
def device_status():
    return render_template('device.html')  # Just load the page normally

@app.route('/device-moisture')
def get_moisture():
    arduino = get_arduino()
    if arduino:
        try:
            arduino.write(b'READ\n')
            data = arduino.readline().decode().strip()
            arduino.close()
            if data.isdigit():
                return f"{data}%"  # ← important: return plain percentage string!
        except:
            return ""  # ← empty to avoid showing error
    return ""  # ← also empty if no connection




@app.route('/water', methods=['POST'])
def water():
    arduino = get_arduino()
    if arduino:
        arduino.write(b'WATER\n')
        arduino.close()
        return ('', 204)
    else:
        return ("Could not connect to device", 500)




@app.route('/favicon.ico')

def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'Agent-Crop-Icon.png')

#API requests are handled here
@app.route('/api/predict', methods=['POST'])

def api_predict():
    global folder_num
    global folders_list
    if folder_num >= 1000000:
            folder_num = 0
    # check if the post request has the file part
    if 'files' not in request.files:
        return {"Error": "No files part found."}
    # Create a new folder for every new file uploaded,
    # so that concurrency can be maintained
    files = request.files.getlist('files')
    app.config['UPLOAD_FOLDER'] = "./static/test"
    app.config['UPLOAD_FOLDER'] = app.config['UPLOAD_FOLDER'] + '/predict_' + str(folder_num).rjust(6, "0")
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
        folders_list.append(app.config['UPLOAD_FOLDER'])
        folder_num += 1
    for file in files:
        if file.filename == '':
            return {"Error": "No Files are Selected!"}
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return {"Error": "Invalid file type! Only PNG, JPEG/JPG files are supported."}
    try:
        if len(os.listdir(app.config['UPLOAD_FOLDER'])) > 0:
            diseases = predict(app.config['UPLOAD_FOLDER'])
            return diseases
    except:
        return {"Error": "Something Went Wrong!"}

if __name__ == '__main__':
    app.run(debug=True)