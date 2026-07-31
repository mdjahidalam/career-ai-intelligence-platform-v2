from app.ai.agents.base_agent import BaseAgent

from app.ai.prompts.resume_builder_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT
)

from app.ai.schemas.resume_builder_schema import ResumeBuilder


class ResumeBuilderAgent(BaseAgent):

    SYSTEM_PROMPT = SYSTEM_PROMPT

    USER_PROMPT = USER_PROMPT

    SCHEMA = ResumeBuilder

    def run(
        self,
        resume_json
    ):

        return self.execute(
            resume_json=resume_json
        )