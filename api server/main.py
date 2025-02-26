from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np
import requests
from io import BytesIO
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware

origins =[
    "http://localhost",
    "http://localhost:3000",
]
# Define TensorFlow Serving API URL (Change this if running on a remote server)
TF_SERVING_URL = "http://localhost:8501/v1/models/potato_model:predict"

# Class names for interpretation
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins= origins,
    allow_credentials= True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/ping")
async def ping():
    return {"message": "Hey, I am online!"}

# Function to read image file and convert it to numpy array
def read_file_as_image(data) -> np.ndarray:
    image = np.array(Image.open(BytesIO(data)).resize((256, 256)))  # Resize if needed
    return image

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = read_file_as_image(await file.read())
    image_batch = np.expand_dims(image, axis=0).tolist()  # Convert to batch format

    # Send the image batch to TensorFlow Serving API
    payload = {"instances": image_batch}
    response = requests.post(TF_SERVING_URL, json=payload)

    if response.status_code != 200:
        return {"error": "Failed to get prediction from TensorFlow Serving"}

    predictions = response.json()["predictions"]
    predicted_class = CLASS_NAMES[np.argmax(predictions)]
    confidence = float(np.max(predictions))

    return {"class": predicted_class, "confidence": confidence}

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
