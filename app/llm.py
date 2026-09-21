from typing import Protocol

from openai import OpenAI

from app.config import settings


class LLM(Protocol):
    def generate(self, prompt: str) -> str:
        ...


class OpenAIResponsesLLM:
    def __init__(self, api_key: str, model: str):
        if not api_key or not model:
            raise ValueError(
                "LLM_API_KEY and LLM_MODEL must be configured in .env"
            )

        self.client = OpenAI(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )
        return response.output_text


def build_llm() -> LLM:
    return OpenAIResponsesLLM(
        api_key=settings.llm_api_key,
        model=settings.llm_model,
    )
