import streamlit as st
import requests
from PIL import Image
import io

API_URL = "http://backend:8000/predict/"


st.sidebar.title("📌 Project Details")
st.sidebar.markdown("""
## 🥗 Food Contamination Detection
Food contamination leads to health risks. This project uses **deep learning** to classify food images as **Contaminated** or **Safe**.

### 🚀 Technologies Used
- **Deep Learning**: MobileNetV2 (TensorFlow)
- **Backend**: FastAPI
- **Frontend**: Streamlit
- **Containerization**: Docker

### 🔍 How It Works?
1️⃣ Upload a **food image**  
2️⃣ **AI Model** analyzes the image  
3️⃣ Get **instant prediction**  

---
📌 **Upload an image in the main screen to get started!**
""")

st.title("🍏 Food Contamination Detection")
st.write("Upload a food image to check if it is **Contaminated** or **Safe**.")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="🖼 Uploaded Image", use_container_width=True)

    img_bytes = io.BytesIO()
    image.save(img_bytes, format=image.format)
    img_bytes = img_bytes.getvalue()

    with st.spinner("🔍 Analyzing image..."):
        response = requests.post(API_URL, files={"file": ("image.jpg", img_bytes, "image/jpeg")})

    if response.status_code == 200:
        result = response.json()
        prediction = result.get("prediction", "Unknown")
        st.success(f"✅ **Result: {prediction}**")
    else:
        st.error("⚠️ Error: Unexpected response from server. Please try again.")

st.markdown("---")
st.markdown("🍽️ **AI-Powered Food Safety | Detect Contamination in a Click! 🚀**")

