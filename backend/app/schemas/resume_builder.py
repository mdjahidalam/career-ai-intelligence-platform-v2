from pydantic import BaseModel


class ResumeRequest(BaseModel):
    resume_id: int


class ResumeResponse(BaseModel):
    success: bool
    message: str
    data: dict