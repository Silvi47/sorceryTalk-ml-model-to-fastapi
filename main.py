from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
from tensorflow.keras.models import load_model
import pickle
from config import MODEL_PATH
from predict import predict_something
from typing import List
from config import TOKENIZER_PATH

# Define error responses for FastAPI UI
API_ERRORS = {
    500: {"description": "Internal Server Error (Prediction or File I/O failed)"},
    503: {"description": "Service Unavailable (Model, Tokenizer, or NLTK Stopwords missing)"}
}

class DataInput(BaseModel):
    data: str

class DataOutput(BaseModel):
    result_label: str

ml_resources = {}

# Load model helper
def load_ml_model():
    """Loads the .h5 model and tokenizer."""
    try:
        # Load Model
        ml_resources['model'] = load_model(MODEL_PATH)
        
        # Load Tokenizer
        with open(TOKENIZER_PATH, 'rb') as handle:
            ml_resources['tokenizer'] = pickle.load(handle)
            
        print("ML Resources loaded successfully.")
        return ml_resources
    except Exception as e:
        print(f"Error loading ML resources: {e}")
        return None

# Code ini dijalankan saat aplikasi FastAPI dimulai dan dimatikan
@asynccontextmanager
async def lifespan(app: FastAPI):
    global ml_resources
    print("Loading ML model...")
    ml_resources  = load_ml_model()

    yield

    print("Cleaning up resources...")
    ml_resources.clear()

app = FastAPI(lifespan=lifespan)

@app.get("/", response_model=str)
def get_api_desc():
    return "Ini adalah API untuk mendeteksi sesuatu."

@app.post("/detect", response_model=DataOutput, responses=API_ERRORS)
def detect_something(data: DataInput):
    """
    Deteksi sesuatu dari data yang diberikan.
    """
    result_label = predict_something(data.data, ml_resources["model"], ml_resources["tokenizer"])
    return result_label
