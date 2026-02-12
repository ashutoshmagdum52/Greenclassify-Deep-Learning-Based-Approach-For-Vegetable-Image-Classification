import re
import numpy as np
import pandas as pd
import os
# Suppress TensorFlow INFO and WARNING logs
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
from flask import Flask, request, render_template
from keras.models import load_model

# Loading the model
model = load_model(r"vegetable_classification.h5", compile=False)

app = Flask(__name__)

# Ensure uploads folder exists
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/index.html')
def home():
    return render_template("index.html")

@app.route('/logout.html')
def logout():
    return render_template('logout.html')

@app.route('/result', methods=["GET", "POST"])
def res():
    if request.method == "POST":
        f = request.files['image']
        
        # Getting the current path i.e where app.py is present
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'uploads', f.filename)
        f.save(filepath)
        
        # Reading image
        img = tf.keras.utils.load_img(filepath, target_size=(150, 150))
        img_arr = tf.keras.utils.img_to_array(img)
        
        # Expanding Dimensions
        img_input = np.expand_dims(img_arr, axis=0)
        
        # Predicting the higher probability index
        pred = np.argmax(model.predict(img_input))
        
        # FIXED: Updated to include ALL 15 classes that the model was trained on
        op = {
            0: 'Bean',
            1: 'Bitter Gourd',
            2: 'Bottle Gourd',
            3: 'Brinjal',
            4: 'Broccoli',
            5: 'Cabbage',
            6: 'Capsicum',
            7: 'Carrot',
            8: 'Cauliflower',
            9: 'Cucumber',
            10: 'Papaya',
            11: 'Potato',
            12: 'Pumpkin',
            13: 'Radish',
            14: 'Tomato'
        }
        
        # Get result with error handling
        result = op.get(pred, f'Unknown (Class {pred})')
        
        # Copy image to static folder for display
        static_img_path = os.path.join(basepath, 'static', 'uploads')
        if not os.path.exists(static_img_path):
            os.makedirs(static_img_path)
        
        import shutil
        static_file = os.path.join(static_img_path, f.filename)
        shutil.copy(filepath, static_file)
        
        return render_template('prediction.html', pred=result, img_name=f.filename)
    
    return render_template('prediction.html')

# Running our application
if __name__ == "__main__":
    app.run(debug=True)
