from typing import List, Optional

from pydantic import BaseModel, Field


class PlacementPrediction(BaseModel):

    placement_probability: int = Field(default=0,ge=0,le=100)

    confidence_score: int = 0

    hiring_recommendation: Optional[str] = None

    reasoning: List[str] = Field(default_factory=list)