# Food Contamination Prediction using Deep Learning

## Table of Contents
- [Introduction](#introduction)
- [Problem Statement](#problem-statement)
- [Solution Overview](#solution-overview)
- [Technologies Used](#technologies-used)
- [System Architecture](#system-architecture)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributors](#contributors)
- [License](#license)

---

## Introduction
Food contamination is a serious concern, leading to foodborne illnesses and health hazards. Detecting contamination manually is inefficient and prone to errors. This project leverages deep learning to automate the detection of food contamination using image classification.

## Problem Statement
Manual inspection of food contamination is not only time-consuming but also unreliable. This project aims to build an automated system that classifies food images as "Contaminated" or "Safe" using a deep learning model.

## Solution Overview
The project consists of a deep learning model trained to classify food images based on contamination. The system includes:
- **Data Collection:** A dataset of labeled food images ("Contaminated" and "Safe").
- **Model Training:** Fine-tuning a MobileNetV2 model to classify food contamination.
- **Backend:** FastAPI-based API for handling requests and making predictions.
- **Frontend:** A Streamlit-based web application for user interaction.
- **Containerization:** Docker is used to containerize the application for easy deployment.

## Technologies Used
- **Deep Learning:** TensorFlow (MobileNetV2 for image classification)
- **Backend:** FastAPI for handling API requests
- **Frontend:** Streamlit for building an interactive user interface
- **Containerization:** Docker for deploying the application
- **Libraries:** NumPy, Pillow (PIL), OpenCV, Requests
- **Deployment:** Docker Compose

## System Architecture
1. **User uploads a food image through the Streamlit UI**
2. **Image is sent to the FastAPI backend**
3. **Pretrained MobileNetV2 model classifies the image**
4. **Prediction is returned to the frontend for display**

## Installation and Setup

### Prerequisites
- Python 3.8+
- Docker (for containerized deployment)
- pip (Python package manager)


### Install Dependencies
```bash
pip install -r requirements.txt
```

### Running Locally
#### Start the Backend (FastAPI)
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### Start the Frontend (Streamlit)
```bash
streamlit run app.py
```

The application will be available at `http://localhost:8501/`.

## Usage
1. Open the Streamlit web application.
2. Upload a food image.
3. The system processes the image and predicts whether it is "Contaminated" or "Safe."

## Dataset
The dataset consists of labeled food images:
- **Contaminated:** Food images with mold, discoloration, or other visible contamination.
- **Safe:** Fresh, uncontaminated food images.

Data augmentation techniques like rotation, flipping, and scaling were applied to enhance model performance.

## Model Training
- Used **MobileNetV2** for transfer learning.
- Fine-tuned the last layers to adapt to the food contamination classification task.
- Optimized using Adam optimizer and categorical cross-entropy loss.
- Achieved high accuracy through training on augmented data.

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/predict/` | POST | Accepts an image and returns the prediction |

### Example Request (Using cURL)
```bash
curl -X 'POST' \
  'http://localhost:8000/predict/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'file=@test_image.jpg'
```

### Example Response
```json
{
  "prediction": "Contaminated",
  "confidence": 0.95
}
```

## Deployment
To deploy the application using Docker:
1. Ensure Docker is installed.
2. Run `docker-compose up --build`
3. Access the frontend at `http://localhost:8501/`
4.Access the backend at `http://localhost:8000/`

## Contributors
- **Your Name** - Katta Sai Pranav Reddy

## License
This project is licensed under the MIT License.

