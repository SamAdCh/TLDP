# Import necessary libraries
import streamlit as st
import numpy as np
import os
import requests
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

model_url = 'https://github.com/SamAdCh/TLDP/raw/master/model.h5'
model_path = 'model.h5'

# Download the model file from GitHub
response = requests.get(model_url)
with open(model_path, 'wb') as f:
    f.write(response.content)

model = load_model(model_path)
print("Model Loaded Successfully")

def pred_tomato_disease(tomato_plant):
    test_image = load_img(tomato_plant, target_size=(128, 128)) # load image 
    st.write("@@ Got Image for prediction")
  
    test_image = img_to_array(test_image)/255 # convert image to np array and normalize
    test_image = np.expand_dims(test_image, axis=0) # change dimension 3D to 4D
  
    result = model.predict(test_image) # predict diseased plant or not
    st.write('@@ Raw result = ', result)
  
    pred = np.argmax(result, axis=1)
    st.write(pred)
    
    classes = [
        "Tomato - Bacteria Spot Disease",
        "Tomato - Early Blight Disease",
        "Tomato - Late Blight Disease",
        "Tomato - Leaf Mold Disease",
        "Tomato - Septoria Leaf Spot Disease",
        "Tomato - Two Spotted Spider Mite Disease",
        "Tomato - Target Spot Disease",
        "Tomato - Tomato Yellow Leaf Curl Virus Disease",
        "Tomato - Tomato Mosaic Virus Disease",
        "Tomato - Healthy and Fresh"
    ]

    return classes[pred[0]]


# Create Streamlit app
def main():
    st.title("Tomato Disease Classification")
    st.write("Upload an image of a tomato plant to classify its disease.")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        file_path = "uploaded_image.jpg"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        st.write("@@ Predicting class......")
        pred = pred_tomato_disease(file_path)
        
        st.write("Prediction:", pred)


if __name__ == "__main__":
    main()
