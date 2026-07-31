from app.ai.agents.base_agent import BaseAgent

from app.ai.prompts.placement_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT
)

from app.ai.schemas.placement_schema import PlacementPrediction


class PlacementAgent(BaseAgent):

    SYSTEM_PROMPT = SYSTEM_PROMPT

    USER_PROMPT = USER_PROMPT

    SCHEMA = PlacementPrediction

    def run(
        self,
        resume_json
    ):

        return self.execute(
            resume_json=resume_json
        )