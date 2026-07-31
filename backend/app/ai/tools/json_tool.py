import json


class JSONTool:

    @staticmethod
    def clean(text: str) -> str:

        text = text.strip()

        if text.startswith("```json"):
            text = text.replace("```json", "", 1)

        if text.startswith("```"):
            text = text.replace("```", "", 1)

        if text.endswith("```"):
            text = text[:-3]

        return text.strip()

    @staticmethod
    def loads(text: str):

        cleaned = JSONTool.clean(text)

        return json.loads(cleaned)

    @staticmethod
    def dumps(data: dict):

        return json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        )