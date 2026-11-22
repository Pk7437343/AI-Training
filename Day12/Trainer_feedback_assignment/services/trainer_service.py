from config.settings import AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION,AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from models.trainer_model import trainer_request, trainer_response
from prompts.trainer_prompts import SYSTEM_PROMPT, HUMAN_PROMPT

llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version=AZURE_OPENAI_API_VERSION,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

structuren_llm = llm.with_structured_output(trainer_response)

prompts = ChatPromptTemplate.from_messages(
    [
        ("system", SYSTEM_PROMPT),
        ("human", HUMAN_PROMPT)
    ]
)

chain = prompts|structuren_llm

def analyze(request: trainer_request)->trainer_response:  #langchain function for 2 models
    response = chain.invoke({
        "trainer_name":request.trainer_name,
        "trainer_topic":request.trainer_topic,
        "learner_name":request.learner_name,
        "rating": request.rating,
        "feedback": request.feedback
    })
    return trainer_response(
        trainer_name = response.trainer_name,
        trainer_topic=response.trainer_topic,
        learner_name=response.learner_name,
        rating= response.rating,
        analyzed_rating= response.analyzed_rating,
        performance_level= response.performance_level,
        sentiment= response.sentiment,
        analysis_summary=response.analysis_summary,
        
        strengths= response.strengths,
        improvement_areas= response.improvement_areas,
        recommendation= response.recommendation,
        overall_summary= response.overall_summary
    )
