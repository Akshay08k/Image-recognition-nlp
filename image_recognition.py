import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np

#specifying the model
model = MobileNetV2(weights='imagenet')

def preprocess_img(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return preprocess_input(img_array)

def classify_image(img_path):
    img_array = preprocess_img(img_path)
    preds = model.predict(img_array)
    return decode_predictions(preds, top=3)[0]

def generate_description(predictions):
    descriptions = []
    for pred in predictions:
        label = pred[1]  
        confidence = round(pred[2] * 100, 2) 
        descriptions.append(f"{label} ({confidence}%)")
    
    description = "The image contains: " + ", ".join(descriptions) + "."
    return description
