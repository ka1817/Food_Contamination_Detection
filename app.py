import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Set image size parameters
img_height, img_width = 224, 224

# Load the saved model
model = load_model(r'C:\Users\saipr\Food_Contamination\model.h5')

# Function to load and preprocess an image for prediction
def predict_image(image_path, model):
    # Load image
    img = image.load_img(image_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)  # Convert to array
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Rescale

    # Make prediction
    prediction = model.predict(img_array)
    if prediction[0] > 0.5:
        return "Contaminated"
    else:
        return "Safe"

# Streamlit app interface
st.title("Food Contamination Prediction")

# Upload an image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Ensure the 'temp' directory exists or create it
    if not os.path.exists("temp"):
        os.makedirs("temp")
    
    # Save the uploaded image temporarily in the 'temp' directory
    image_path = os.path.join("temp", uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Show the image (using use_container_width instead of use_column_width)
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
    
    # Make prediction
    result = predict_image(image_path, model)
    
    # Show prediction result
    st.write(f"Prediction: The food is {result}.")
