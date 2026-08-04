from pydantic import BaseModel


class JobMatchingResponse(BaseModel):

    id: int

    match_score: float

    analysis: dict

    class Config:

        from_attributes = True