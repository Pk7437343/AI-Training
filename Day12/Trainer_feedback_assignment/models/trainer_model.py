from pydantic import BaseModel, Field

class trainer_request(BaseModel):
    trainer_name:str
    trainer_topic:str
    learner_name:str
    rating: int = Field(ge=1, le=5)
    feedback:str

class trainer_response(BaseModel):
    trainer_name: str
    trainer_topic: str
    learner_name: str
    rating: int
    analyzed_rating: int
    performance_level: str
    sentiment: str
    analysis_summary: str

    strengths: list[str]
    improvement_areas: list[str]
    recommendation: str
    overall_summary: str