import json
import re


class JSONTool:

    @staticmethod
    def clean(text: str):

        text = text.strip()

        text = re.sub(r"^```json", "", text)
        text = re.sub(r"^```", "", text)
        text = re.sub(r"```$", "", text)

        start = text.find("{")
        end = text.rfind("}")

        if start != -1 and end != -1:
            text = text[start:end + 1]

        return text.strip()

    @staticmethod
    def loads(text):

        cleaned = JSONTool.clean(text)

        try:
            return json.loads(cleaned)

        except json.JSONDecodeError as e:

            print("=" * 80)
            print("RAW JSON:")
            print(repr(cleaned))
            print("=" * 80)

            print(f"LINE: {e.lineno}")
            print(f"COLUMN: {e.colno}")

            lines = cleaned.splitlines()

            if e.lineno <= len(lines):
                print("ERROR LINE:")
                print(lines[e.lineno - 1])

            raise

    @staticmethod
    def dumps(data):

        return json.dumps(
            data,
            indent=4,
            ensure_ascii=False
        )