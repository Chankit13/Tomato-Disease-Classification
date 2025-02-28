# Multi-Class Classification of Tomato Leaf Diseases Using CNN

## Overview
This project aims to classify 11 distinct tomato plant leaf diseases using **Convolutional Neural Networks (CNNs)**. The model is deployed using **TensorFlow Serving** and the backend is built with **FastAPI**. The system is integrated with a **React Native** frontend for user interaction.

## Tech Stack
- **Machine Learning & Deep Learning**: TensorFlow, Keras, OpenCV, NumPy, Pandas
- **Backend**: FastAPI
- **Model Deployment**: TensorFlow Serving
- **Frontend**: React Native
- **Containerization**: Docker (if required)
- **Database**: MySQL (if needed)
- **Cloud Services**: Google Cloud Functions

## Dataset
- The dataset is sourced from Kaggle and contains **11 classes**:
  - Late Blight
  - Healthy
  - Early Blight
  - Septoria Leaf Spot
  - Tomato Yellow Leaf Curl Virus
  - Bacterial Spot
  - Target Spot
  - Tomato Mosaic Virus
  - Leaf Mold
  - Spider Mites (Two-Spotted Spider Mite)
  - Powdery Mildew

## Project Phases
1. **Data Collection & Preprocessing**
2. **Model Building & Training**
3. **ML Ops & Deployment**
4. **Mobile App Integration**

## Installation
### Backend Setup
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
### Model Deployment (TensorFlow Serving)
```bash
docker run -p 8501:8501 --name=tf_serving \
    -v "$(pwd)/model:/models/tomato_model" \
    -e MODEL_NAME=tomato_model \
    tensorflow/serving
```
### Frontend Setup
```bash
cd frontend
npm install
npm start
```

## API Endpoints
- `POST /predict`: Takes an image and returns the predicted disease class.
- `GET /health`: Health check for the FastAPI server.

## Contribution
1. Fork the repo.
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request.

## License
This project is licensed under the MIT License.

