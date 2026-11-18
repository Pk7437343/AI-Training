from openai import OpenAI
import json
from prompts.prompt_role_based import(
    HUMAN_PROMPT,
    SYSTEM_PROMPT
)

from models.model_role_based import(
    PythonAIRequest,
    PythonAIResponse
)

from config.settings import AZURE_OPENAI_API_KEY,AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINT

#create llm

llm = OpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=f"{AZURE_OPENAI_ENDPOINT.rstrip("/")}/openai/v1"
)

def analyze_python_role_based(request: PythonAIRequest)->PythonAIResponse:
    user_prompt = HUMAN_PROMPT.format(
        learner_name = request.learner_name,
        question = request.question,
        experience_level = request.experience_level
    )
    # response = llm.responses.parse(
    #   
    #     input=user_prompt,
    #     text_format= PythonAIResponse
    # )
    response = llm.responses.parse(
        model=AZURE_OPENAI_DEPLOYMENT,
        instructions=SYSTEM_PROMPT,
        input=user_prompt,
        text_format=PythonAIResponse
    )
    ai_reponses = response.output_text
    print(ai_reponses)
    parse_data = json.loads(ai_reponses)
    print(parse_data)
  
    return PythonAIResponse(
        **parse_data 
    )
