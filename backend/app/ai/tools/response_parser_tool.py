from pydantic import ValidationError

from app.ai.tools.json_tool import JSONTool
from app.ai.tools.validation_tool import ValidationTool


class ResponseParserTool:

    @staticmethod
    def parse(
        response: str,
        schema
    ):

        data = JSONTool.loads(response)

        validated = ValidationTool.validate(
            schema,
            data
        )

        return validated

    @staticmethod
    def parse_without_validation(
        response: str
    ):

        return JSONTool.loads(response)