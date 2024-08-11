from pydantic import BaseModel
from typing import List
class MCQModel(BaseModel):
    questionNumber: int
    scenario: str
    question: str
    options: List[str]
    explanation : str
    answer : str
