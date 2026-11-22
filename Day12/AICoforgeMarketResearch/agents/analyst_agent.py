from langchain_core.messages import(
    SystemMessage, 
    HumanMessage
)
from services.llm_service import create_llm
from models.market__models import AnalysisResult
from graph.state import Marketstate

def analyst_agent(state:Marketstate):
    print("Market Analyst Agent Started")
    research = state.get("research_result")

    if research is None:
        raise ValueError(
            "Reserch must be completed befor analysis"
        )
    llm = create_llm()
    structured_llm = llm.with_structures_output(
        AnalysisResult
    )
    SYSTEM_PROMPT ="""
    you are an enterprise business market analyst.

    Your responsibilities:
    1. Analyze the supplied market research.
    2. Identify company strength.
    3. Identify potential weaknesses.
    4.
"""