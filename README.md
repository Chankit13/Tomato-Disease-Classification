# 🥔Multi-Class Classification of Potato Leaf Diseases 

## 📝Overview
This project aims to classify 3 distinct potato plant leaf diseases using **Convolutional Neural Networks (CNNs)**. The model is deployed using **TensorFlow Serving** and the backend is built with **FastAPI**. The system is integrated with a **React.js** frontend for user interaction.

## 🛠️Tech Stack
- **Machine Learning & Deep Learning**: TensorFlow, Keras, matplotlib, NumPy, Pandas
- **Backend**: FastAPI
- **Model Deployment**: TensorFlow Serving
- **Frontend**: React.js
- **Containerization**: Docker 
## 📂Dataset

- The dataset is sourced from Kaggle and contains **3 classes**:
  - Late Blight
  - Healthy
  - Early Blight
## 🚀Project Phases
1. **Data Collection & Preprocessing**
2. **Model Building & Training**
3. **ML Ops & Deployment**
4. **Web Interface**

## ⚙️Installation
### Backend Setup
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```
### 🚢Model Deployment (TensorFlow Serving)
```bash
docker run -p 8501:8501 --name=tf_serving \
    -v "$(pwd)/model:/models/potato_model" \
    -e MODEL_NAME=potato_model \
    tensorflow/serving
```
### 🎨Frontend Setup
```bash
cd frontend
npm install
npm start
```
## 📜License
This project is licensed under the MIT License.

