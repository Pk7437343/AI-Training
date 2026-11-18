#structure prompting means--------Role, Task, context, Rule

from pydantic import BaseModel, Field

#API request
class LearnerRequest(BaseModel):
    learnername : str = Field(min_length=1)
    department : str = Field(min_length=1)
    PythonScore: int = Field(ge=0, le=100)
    SqlScore: int = Field(ge=0, le=100)
    FastApiScore: int = Field(ge=0, le=100)
    AttendancePercentage: float = Field(ge=0, le=100)
    AssignmentsCompleted: float = Field(gt=0)
    TotalAssignments: float = Field(gt=0)

#ai analysis
class LearnerAnalysis(BaseModel):
    AverageScore : float
    PerformanceLevel : str
    StrongestTechnology : str
    WeakestTechnology: str
    TotalAssessment: str
    RecommendedLearning: list[str]

class LearnerResponse(BaseModel):
    learnername:str
    department: str
    analysis: LearnerAnalysis
    FinalRecommendation: str