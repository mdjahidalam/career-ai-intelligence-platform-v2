from pydantic import BaseModel


class CareerResponse(BaseModel):

    id: int

    career_title: str

    match_score: float

    roadmap: list

    required_skills: list

    estimated_salary: str | None = None

    class Config:

        from_attributes = True