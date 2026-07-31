from app.ai.agents.base_agent import BaseAgent

from app.ai.prompts.resume_optimizer_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT
)

from app.ai.schemas.resume_optimizer_schema import ResumeOptimizer


class ResumeOptimizerAgent(BaseAgent):

    SYSTEM_PROMPT = SYSTEM_PROMPT

    USER_PROMPT = USER_PROMPT

    SCHEMA = ResumeOptimizer

    def run(
        self,
        resume_json
    ):

        return self.execute(
            resume_json=resume_json
        )