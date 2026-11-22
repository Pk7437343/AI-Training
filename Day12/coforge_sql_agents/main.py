from crewai import Crew, Process
from agents.sql_executor_agent import sql_executor
from agents.sql_generator_agent import sql_generator
from agents.sql_validator_agent import sql_validator

from tasks.tasks import create_tasks

question = input("Ask you sql question")
tasks = create_tasks(question)

crew = Crew(
    agents=[sql_generator,
            sql_validator,
            sql_executor],
            tasks=tasks,
            process= Process.sequential,
            verbose=True
)
result= crew.kickoff()
print("final sql agent response")
print(result.raw)