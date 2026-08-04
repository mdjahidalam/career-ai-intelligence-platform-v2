from pydantic import BaseModel


class InterviewResponse(BaseModel):

    id: int

    session_name: str

    company_name: str | None = None

    job_role: str | None = None

    interview_level: str

    score: float

    feedback: dict | None = None

    class Config:

        from_attributes = True