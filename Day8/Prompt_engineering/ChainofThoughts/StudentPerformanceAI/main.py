from fastapi import FastAPI
from models.student_model import StudentPerformanceResponse, StudentPerformanceAnalysis,StudentPerformanceRequest
from services.llm_service import analyze_student_performance

app = FastAPI(
    title = "Student Performance Analyzer"
)

@app.get("/")
def home():
    return {
        "message": "Student Permormance Analyzer"
    }

@app.post("/api/v1/analyze-student", response_model=StudentPerformanceResponse)
def analyze_student(request: StudentPerformanceRequest):
    return analyze_student_performance(request)