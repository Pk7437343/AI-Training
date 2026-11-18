from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from prompts.trainer_feedback_prompt import SYSTEM_PROMPT, HUMAN_PROMPT

from config.settings import AZURE_OPENAI_API_KEY,AZURE_OPENAI_API_VERSION, AZURE_OPENAI_DEPLOYMENT, AZURE_OPENAI_ENDPOINT
from models.trainer_feedback_model import TrainerFeedbackResponse, TrainingFeedbackRequest
# from prompts.trainer_feedback_prompt import SYSTEM_PROMPT, HUMAN_PROMPT



llm = AzureChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    azure_deployment=AZURE_OPENAI_DEPLOYMENT,
    api_version=AZURE_OPENAI_API_VERSION
)

structured_llm = llm.with_structured_output(
     TrainerFeedbackResponse
  )


prompt = ChatPromptTemplate.from_messages(
   [
       ("system", SYSTEM_PROMPT),
       ("human", HUMAN_PROMPT)
   ]
)

#LCEl use to start langchain
chain=prompt| structured_llm

def analyze_feedback(request: TrainingFeedbackRequest)-> TrainerFeedbackResponse:
    response = chain.invoke({
    "trainer_name": request.trainer_name,
    "trainer_topic": request.trainer_topic,
    "learner_name": request.learner_name,
    "rating": request.rating,
    "feedback": request.feedback
})
    return response









