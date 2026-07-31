from app.ai.agents.base_agent import BaseAgent

from app.ai.prompts.resume_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT
)

from app.ai.schemas.resume_schema import ResumeSchema
from app.ai.json_schema import RESUME_JSON_SCHEMA

class ResumeAgent(BaseAgent):

    SYSTEM_PROMPT = SYSTEM_PROMPT

    USER_PROMPT = USER_PROMPT

    SCHEMA = ResumeSchema
    JSON_SCHEMA = RESUME_JSON_SCHEMA
    def run(
        self,
        resume_text: str
    ):

        return self.execute(
            resume_text=resume_text
        )