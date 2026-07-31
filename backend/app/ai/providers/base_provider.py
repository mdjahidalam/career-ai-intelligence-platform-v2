from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def generate(
        self,
        system_prompt: str,
        user_prompt: str
    ):
        pass

    @abstractmethod
    def generate_json(
        self,
        system_prompt: str,
        user_prompt: str,
        schema=None
    ):
        pass

    @abstractmethod
    def generate_stream(
        self,
        system_prompt: str,
        user_prompt: str
    ):
        pass

    @abstractmethod
    def count_tokens(
        self,
        text: str
    ):
        pass