import io
import os
import uvicorn
import numpy as np
import tensorflow as tf
from PIL import Image
from pathlib import Path

from fastapi import File, UploadFile, FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Membuat instance FastAPI
app = FastAPI()

# Ijinkan request dari frontend seperti Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan domain tertentu jika perlu
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

# Path ke model
BASE_DIR   = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / 'model' / 'best_transfer.h5'

# Load model
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(str(MODEL_PATH))
    print("Model berhasil dimuat.")
else:
    raise FileNotFoundError(f"Model tidak ditemukan di {MODEL_PATH}")

# Label klasifikasi
labels = ["paper", "rock", "scissors"]
UNKNOWN_LABEL = "unknown"
THRESHOLD = 0.6  # Confidence threshold

def preprocess_pipeline(image: Image.Image, IMG_SIZE=(224, 224)) -> np.ndarray:
    """
    Proses preprocessing:
    - Resize ke ukuran yang dibutuhkan model.
    - Ubah ke array float32.
    - Normalisasi piksel ke [0, 1].
    """
    image = image.resize(IMG_SIZE)
    arr = np.array(image, dtype=np.float32) / 255.0
    return arr

# Endpoint prediksi
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")
    x = preprocess_pipeline(image)
    x = np.expand_dims(x, axis=0)

    predictions = model.predict(x)
    best_index = int(np.argmax(predictions[0]))
    confidence = float(predictions[0][best_index])

    if confidence < THRESHOLD:
        label = UNKNOWN_LABEL
    else:
        label = labels[best_index]

    return {"label": label, "confidence": confidence}

# Jalankan aplikasi
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
