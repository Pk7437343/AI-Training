from crewai import Agent
from config.settings import llm

hr_policy_analyst = Agent(
    role = "HR Policy Analyst",
    goal =(
        "Evaluate employee leave requests"
        "According to company HR policies"
    ),
    backstory=(
        "You are an HR policy specialist."
        "you can check employee leave eligibility"
        "using verified employee information"
        "and company leave policy"
        "You never invent leave balances."
    ),
    llm = llm,
    verbose = True,
    allow_delegation =False
)