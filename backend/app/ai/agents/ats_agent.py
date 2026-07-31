from app.ai.agents.base_agent import BaseAgent

from app.ai.prompts.ats_prompt import (
    SYSTEM_PROMPT,
    USER_PROMPT
)

from app.ai.schemas.ats_schema import ATSAnalysis


class ATSAgent(BaseAgent):

    SYSTEM_PROMPT = SYSTEM_PROMPT

    USER_PROMPT = USER_PROMPT

    SCHEMA = ATSAnalysis

    def run(
        self,
        resume_json
    ):

        return self.execute(
            resume_json=resume_json
        )