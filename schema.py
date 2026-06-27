from typing import Literal #force prompt to follow specific values for str data types
from pydantic import BaseModel, Field #parses response (for strings), forces prompt to follow constraint values (int)

class schema(BaseModel): # Define how we're controlling the response from GPT5.5
  fit_grade: Literal['A', 'A-', 'B+', 'B', 'B-', 'C', 'D', 'F']

  fit_score: int = Field(ge=0, le=100)

  decision: Literal['APPLY_AND_TAILOR', 'APPLY_WITH_BASE_RESUME', 'MANUAL_REVIEW', 'SKIP']

  strong_matches: list[str]

  major_gaps: list[str]

  summary: str
