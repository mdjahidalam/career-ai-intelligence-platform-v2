from app.ai.agents.base_agent import BaseAgent

from app.ai.prompts.interview_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT
)

from app.ai.schemas.interview_schema import InterviewPreparation


class InterviewAgent(BaseAgent):

    SYSTEM_PROMPT = SYSTEM_PROMPT

    USER_PROMPT = USER_PROMPT

    SCHEMA = InterviewPreparation

    def run(
        self,
        resume_json
    ):

        return self.execute(
            resume_json=resume_json
        )