from app.ai.agents.base_agent import BaseAgent

from app.ai.prompts.salary_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT
)

from app.ai.schemas.salary_schema import SalaryPrediction


class SalaryAgent(BaseAgent):

    SYSTEM_PROMPT = SYSTEM_PROMPT

    USER_PROMPT = USER_PROMPT

    SCHEMA = SalaryPrediction

    def run(
        self,
        resume_json
    ):

        return self.execute(
            resume_json=resume_json
        )