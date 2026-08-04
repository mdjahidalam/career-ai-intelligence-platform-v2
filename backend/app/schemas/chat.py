from pydantic import BaseModel

from datetime import datetime


class ChatMessageResponse(BaseModel):

    id: int

    role: str

    message: str

    created_at: datetime

    class Config:

        from_attributes = True


class ChatSessionResponse(BaseModel):

    id: int

    title: str

    created_at: datetime

    class Config:

        from_attributes = True