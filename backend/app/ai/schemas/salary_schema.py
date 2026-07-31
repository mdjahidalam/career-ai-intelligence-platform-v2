from typing import List, Optional

from pydantic import BaseModel, Field


class SalaryPrediction(BaseModel):

    india_salary_range: Optional[str] = None

    global_salary_range: Optional[str] = None

    reasoning: List[str] = Field(default_factory=list)