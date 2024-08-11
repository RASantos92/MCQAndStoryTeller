from typing import List
from pydantic import BaseModel
class Story(BaseModel):
    story_number : int
    genres: List[str]
    story_content : str
    coherency_score : int
    plot_complexity_score: int
    has_start_middle_end : bool
    overall_score : int