import json
from config.setting import AZURE_OPENAI_API_KEY, AZURE_OPENAI_DEPLOYMENT,AZURE_OPENAI_ENDPOINT,AZURE_OPENAI_API_VERSION
from models.student_model import StudentPerformanceAnalysis, StudentPerformanceRequest, StudentPerformanceResponse

from prompts.student_prompt import SYSTEM_PROMPT, HUMAN_PROMPT
from openai import AzureOpenAI

llm = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)

def analyze_student_performance(request= StudentPerformanceRequest)->StudentPerformanceResponse:
    user_prompt = HUMAN_PROMPT.format(
        student_id = request.student_id,
        student_name = request.student_name,
        python_marks = request.python_marks,
        sql_marks = request.sql_marks,
        fastapi_marks = request.fastapi_marks
    )
    response = llm.chat.completions.create(
        model=AZURE_OPENAI_DEPLOYMENT,
        messages=[
            {
                "role":"system",
                "content":SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        response_format={"type":"json_object"}
    )
    content = response.choices[0].message.content
    if not content:
        raise ValueError("AI Return Empty Response")
    ai_analysis = StudentPerformanceAnalysis(**json.loads(content))

    analysis = StudentPerformanceAnalysis(
        total_marks = ai_analysis.total_marks,
        avg_marks = ai_analysis.avg_marks,
        grade = ai_analysis.grade,
        result = ai_analysis.result,
        # calculation_summary= ai_analysis.calculation_summary
    )
    return StudentPerformanceResponse(
        student_id=request.student_id,
        student_name=request.student_name,
        analysis=analysis
        # improvement_suggestion=request["improvement_suggestion"]
    )




    #     ai_analysis = StudentAnalysis(**json.loads(ai_text))

    # return Studentresponse(
    #     student_id=request.student_id,
    #     student_name=request.student_name,
    #     prompting_technique = "One Shot Prompting",
    #     ai_analysis=ai_analysis
    # )