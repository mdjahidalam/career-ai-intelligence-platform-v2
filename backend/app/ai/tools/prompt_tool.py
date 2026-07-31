class PromptTool:

    @staticmethod
    def build(
        system_prompt: str,
        user_prompt: str,
        **kwargs
    ):

        return (

            system_prompt,

            user_prompt.format(
                **kwargs
            )

        )