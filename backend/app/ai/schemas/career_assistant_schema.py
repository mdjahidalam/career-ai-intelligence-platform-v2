from pydantic import BaseModel, Field


class CareerChatRequest(BaseModel):

    message: str = Field(
        ...,
        min_length=1,
        max_length=10000,
        description="User's message"
    )

    conversation_id: int | None = Field(
        default=None,
        description="Current conversation ID"
    )