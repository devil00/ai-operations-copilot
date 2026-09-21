from typing import Literal
from pydantic import BaseModel, Field


Decision = Literal["ANSWER", "INSUFFICIENT_EVIDENCE"]


class Citation(BaseModel):
    document_id: str
    chunk_id: str
    quote: str


class CopilotResponse(BaseModel):
    decision: Decision
    answer: str
    citations: list[Citation] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)
    retrieved_chunks: int = Field(ge=0)
