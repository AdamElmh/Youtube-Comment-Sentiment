from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
import joblib

# Load model and vectorizer
MODEL_PATH = "models/logreg_model.joblib"
VECTORIZER_PATH = "models/tfidf_vectorizer.joblib"
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# FastAPI app
app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Health endpoint
@app.get("/health")
def health():
    return {"status": "OK", "model_loaded": model is not None}


# Input model for prediction
class CommentBatch(BaseModel):
    comments: List[str]


# Predict batch endpoint
@app.post("/predictbatch")
def predict_batch(data: CommentBatch):
    comments = data.comments
    if not comments or not isinstance(comments, list):
        raise HTTPException(status_code=400, detail="No comments provided.")
    X = vectorizer.transform(comments)
    preds = model.predict(X)
    # Optionally, get model prediction probabilities/confidence
    confs = None
    if hasattr(model, "predict_proba"):
        confs = model.predict_proba(X).max(axis=1)
    return {
        "results": [{"comment": c, "sentiment": int(s), "confidence": float(conf) if confs is not None else None}
                    for c, s, conf in zip(comments, preds, confs if confs is not None else [None] * len(comments))]
    }
