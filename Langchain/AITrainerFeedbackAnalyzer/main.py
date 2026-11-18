from fastapi import FastAPI
from services.llm_service import analyze_feedback

from models.trainer_feedback_model import TrainerFeedbackResponse, TrainingFeedbackRequest

app = FastAPI(
    title="student profile Analyzer"
)

@app.get("/")
def Home():
    return{
        "message= Here is Analysis"
    }

@app.post("/api/v1/langchainai", response_model=TrainerFeedbackResponse)
def analyze(request: TrainingFeedbackRequest)->TrainerFeedbackResponse:
    response = analyze_feedback(request)
    return response

