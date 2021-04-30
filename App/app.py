import os
import joblib
from werkzeug.utils import secure_filename
from flask import Flask, send_from_directory, Response, flash, request, redirect, url_for, render_template
from PIL import Image
import joblib
import numpy as np
import face_recognition
import dlib
import cv2

app = Flask(__name__)

def predict_height_width_BMI(picture):
    height_model_weights = joblib.load('height_model.pkl')
    weight_model_weights = joblib.load('weight_model.pkl')
    bmi_model_weights = joblib.load('bmi_model.pkl')

    face_encode = face_recognition.face_encodings(picture)
    if not face_encode:
        print("NO FACE DETECTED!")
        test_image = np.zeros(128).tolist()
    else:
        test_image = face_encode[0].tolist()
    test_array = np.expand_dims(np.array(test_image), axis = 0)
    #test_array = np.expand_dims(np.array(get_face_encoding(test_image)),axis=0)
    height = np.ndarray.item(height_model_weights.predict(test_array))
    weight = np.ndarray.item(weight_model_weights.predict(test_array))
    bmi = np.ndarray.item(bmi_model_weights.predict(test_array))
    if bmi < 19:
        bmi_category = "UNDERWEIGHT"
    elif bmi > 26:
        bmi_category = "OVERWEIGHT"
    else:
        bmi_category = "NORMAL"
    return str({'HEIGHT':height, 'WEIGHT':weight, 'BMI':bmi, "BMI CATEGORY":bmi_category})

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/uploadr',methods=['GET','POST'])
def uploadr():
    if request.method == 'POST':
        image = request.files['file']
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'images', secure_filename(image.filename))
        image.save(file_path)
        text = predict_height_width_BMI(cv2.imread(file_path))
        return text
    return None

if __name__ == '__main___':
    app.run()
