from app.ai.agents.base_agent import BaseAgent

from app.ai.prompts.job_matching_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT
)

from app.ai.schemas.job_matching_schema import JobMatching


class JobMatchingAgent(BaseAgent):

    SYSTEM_PROMPT = SYSTEM_PROMPT

    USER_PROMPT = USER_PROMPT

    SCHEMA = JobMatching

    def run(
        self,
        resume_json,
        job_description
    ):

        return self.execute(
            resume_json=resume_json,
            job_description=job_description
        )