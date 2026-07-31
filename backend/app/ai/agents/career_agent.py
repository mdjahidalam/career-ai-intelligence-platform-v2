from app.ai.agents.base_agent import BaseAgent

from app.ai.prompts.career_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT
)

from app.ai.schemas.career_schema import CareerRecommendation


class CareerAgent(BaseAgent):

    SYSTEM_PROMPT = SYSTEM_PROMPT

    USER_PROMPT = USER_PROMPT

    SCHEMA = CareerRecommendation

    def run(
        self,
        resume_json
    ):

        return self.execute(
            resume_json=resume_json
        )