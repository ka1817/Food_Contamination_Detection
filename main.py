from fastapi import FastAPI, File, UploadFile
import uvicorn
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model
from io import BytesIO
from PIL import Image

app = FastAPI()

# Load the model
model = load_model('model.h5')

img_height, img_width = 224, 224

# Function to preprocess image
def preprocess_image(image_bytes):
    img = Image.open(BytesIO(image_bytes))
    img = img.resize((img_height, img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale
    return img_array

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img_array = preprocess_image(image_bytes)
    
    prediction = model.predict(img_array)
    result = "Contaminated" if prediction[0] > 0.5 else "Safe"
    
    return {"filename": file.filename, "prediction": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
