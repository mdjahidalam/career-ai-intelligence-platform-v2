import json
from pydantic import ValidationError

from app.ai.tools.json_tool import JSONTool
from app.ai.tools.validation_tool import ValidationTool


class ResponseParserTool:

    @staticmethod
    def parse(response: str, schema):

        try:
            data = JSONTool.loads(response)

        except json.JSONDecodeError as e:

            print("=" * 80)
            print("INVALID JSON FROM GEMINI")
            print("=" * 80)
            print(response)
            print("=" * 80)

            raise Exception(
                f"Gemini returned invalid JSON.\n{e}"
            )

        validated = ValidationTool.validate(
            schema,
            data
        )

        return validated

    @staticmethod
    def parse_without_validation(response: str):

        return JSONTool.loads(response)