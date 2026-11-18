from langchain.agents import create_agent
from langchain_openai import AzureChatOpenAI

from config.settings import AZURE_OPENAI_API_KEY, AZURE_OPENAI_API_VERSION, AZURE_OPENAI_DEPLOYMENT, AZURE_OPENAI_ENDPOINT

from prompts.Employee_Salary_prompt import SYSTEM_PROMPT

from tools.ai_tools import calculate_basic_salary, calculate_da, calculate_gross_salary, calculate_hra


def create_salary_agent():
    llm = AzureChatOpenAI( #connect to azure api
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        azure_deployment=AZURE_OPENAI_DEPLOYMENT,
        api_version=AZURE_OPENAI_API_VERSION
    )

# register four tools

    salary_tools = [
        calculate_basic_salary,
        calculate_hra,
        calculate_da,
        calculate_gross_salary
    ]

    agent = create_agent(
        model=llm,
        tools= salary_tools,
        system_prompt=SYSTEM_PROMPT
    )
    return agent