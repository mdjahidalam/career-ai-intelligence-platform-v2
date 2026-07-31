from abc import ABC, abstractmethod

from app.ai.tools.prompt_tool import PromptTool
from app.ai.tools.response_parser_tool import ResponseParserTool


class BaseAgent(ABC):

    SYSTEM_PROMPT = ""

    USER_PROMPT = ""

    SCHEMA = None

    JSON_SCHEMA = None

    def __init__(self, provider):

        self.provider = provider

    # --------------------------------------------------
    # Hooks
    # --------------------------------------------------

    def pre_process(self, **kwargs):

        return kwargs

    def post_process(self, result):

        return result

    # --------------------------------------------------
    # Main Pipeline
    # --------------------------------------------------

    def execute(

        self,

        validate=True,

        **kwargs

    ):

        # 1. Pre Process

        kwargs = self.pre_process(

            **kwargs

        )

        # 2. Prompt Build

        system_prompt, user_prompt = PromptTool.build(

            self.SYSTEM_PROMPT,

            self.USER_PROMPT,

            schema=self.SCHEMA.model_json_schema(),

            **kwargs

        )

        # 3. LLM Call

        response = self.provider.generate(

            system_prompt,

            user_prompt

        )

        print("="*80)
        print(response)
        print("="*80)

        # 4. Parse

        if validate:

            result = ResponseParserTool.parse(

                response,

                self.SCHEMA

            )

        else:

            result = ResponseParserTool.parse_without_validation(

                response

            )

        # 5. Post Process

        return self.post_process(

            result

        )

    @abstractmethod
    def run(self, *args, **kwargs):

        """
        Every agent must implement run().
        """

        pass