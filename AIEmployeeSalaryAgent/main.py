from fastapi import FastAPI
from services.llm_service import create_salary_agent, calculate_employee_salary
from models.Employee_Salary_model import SalaryResponse, SalaryRequest

app= FastAPI(
    title="AI Agent"
)

@app.get("/")
def Home():
    return "Home"

@app.post("/api/v1/AiAgent", response_model=SalaryResponse)
def analyze(request: SalaryRequest)-> SalaryResponse:
    response = calculate_employee_salary(request)
    return response

