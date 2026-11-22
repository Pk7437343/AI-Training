from fastapi import FastAPI
from services.trainer_service import analyze
from models.trainer_model import trainer_response,trainer_request

app = FastAPI(
    title="Langachain successful",
    version="1.0.1"
)

@app.get("/")
def get_info():
    return "home"

@app.post("/post_method", response_model=trainer_response)
def post_method(request: trainer_request):
    result = analyze(request)
    return result