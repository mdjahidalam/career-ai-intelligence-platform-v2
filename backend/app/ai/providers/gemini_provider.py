import json

from google import genai

from app.ai.providers.base_provider import BaseProvider

from google.genai import types

class GeminiProvider(BaseProvider):

    def __init__(

        self,

        api_key: str,

        model_name: str

    ):

        self.client = genai.Client(
            api_key=api_key
        )

        self.model_name = model_name

    # -----------------------------------

    def generate(

        self,

        system_prompt,

        user_prompt

    ):

        prompt = f"""

{system_prompt}

{user_prompt}

"""

        response = self.client.models.generate_content(

            model=self.model_name,

            contents=prompt,

            config=types.GenerateContentConfig(

            response_mime_type="application/json")

        )

        return response.text

    # -----------------------------------

    def generate_json(

        self,

        system_prompt,

        user_prompt,

        schema=None

    ):

        text = self.generate(

            system_prompt,

            user_prompt

        )

        return json.loads(text)

    # -----------------------------------

    def generate_stream(

        self,

        system_prompt,

        user_prompt

    ):

        prompt = f"""

{system_prompt}

{user_prompt}

"""

        return self.client.models.generate_content_stream(

            model=self.model_name,

            contents=prompt

        )

    # -----------------------------------

    def count_tokens(

        self,

        text

    ):

        return self.client.models.count_tokens(

            model=self.model_name,

            contents=text

        )