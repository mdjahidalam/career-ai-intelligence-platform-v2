from app.ai.config.ai_config import AIConfig

from app.ai.providers.gemini_provider import GeminiProvider


class ProviderFactory:

    @staticmethod
    def create():

        provider = AIConfig.PROVIDER.lower()

        if provider == "gemini":

            return GeminiProvider(

                api_key=AIConfig.API_KEY,

                model_name=AIConfig.MODEL_NAME

            )

        raise ValueError(

            f"Unsupported provider: {provider}"

        )