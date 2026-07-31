import logging
import time

from google import genai


logger = logging.getLogger(__name__)


class LLMTool:

    def __init__(
        self,
        api_key: str,
        model_name: str,
        max_retry: int = 3
    ):

        self.client = genai.Client(
            api_key=api_key
        )

        self.model_name = model_name

        self.max_retry = max_retry

    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ):

        prompt = f"""
{system_prompt}

{user_prompt}
"""

        for attempt in range(self.max_retry):

            try:

                response = self.client.models.generate_content(

                    model=self.model_name,

                    contents=prompt

                )

                return response.text

            except Exception as e:

                logger.warning(
                    f"Retry {attempt+1}: {e}"
                )

                if attempt == self.max_retry - 1:

                    raise

                time.sleep(2)