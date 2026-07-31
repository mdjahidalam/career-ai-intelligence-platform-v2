from pydantic import ValidationError


class ValidationTool:

    @staticmethod
    def validate(
        schema,
        data
    ):

        try:

            return schema.model_validate(
                data
            )

        except ValidationError as e:

            raise e