from fastapi import FastAPI
from services.llm_service import PythonAIResponse, PythonAIRequest, analyze_python_role_based
from models.model_role_based import PythonAIRequest,PythonAIResponse


app = FastAPI(
    title="Python Ai Model",
    version="1.0"
)

@app.get("/home")
def home():
    return {
        "message":"Python AI"
    }


@app.post("/PythonAI", response_model=PythonAIResponse)
def training(request: PythonAIRequest):
    return analyze_python_role_based(request)