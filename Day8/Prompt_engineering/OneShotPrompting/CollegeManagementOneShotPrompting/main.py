from fastapi import FastAPI
from services.llm_service import StudentResponse,StudentAnalysis,StudentRequest, analyze_student_profile


app = FastAPI(
    title="student profile Analyzer"
)

@app.get("/home")
def Home():
    return{
        "message= Here is Analysis"
    }
@app.post("/api/v1/AI", response_model=StudentResponse)
def analyze(request: StudentRequest)->StudentResponse:
    response = analyze_student_profile(request)
    return response

