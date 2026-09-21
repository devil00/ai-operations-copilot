from app.retrieval import DocumentChunk


SYSTEM_INSTRUCTIONS = """You are an enterprise operations copilot.

Rules:
1. Use only the supplied evidence.
2. Do not invent policy rules, amounts, dates, IDs, or facts.
3. If the evidence is insufficient, explicitly say so.
4. Do not execute sensitive business actions.
5. Every factual claim should be supported by a citation.
"""


def build_prompt(question: str, evidence: list[DocumentChunk]) -> str:
    evidence_text = "\n\n".join(
        f"[{chunk.document_id}:{chunk.chunk_id}] {chunk.text}"
        for chunk in evidence
    )

    return f"""{SYSTEM_INSTRUCTIONS}

Evidence:
{evidence_text}

Question:
{question}

Answer concisely. If the evidence does not support a reliable answer,
respond with: INSUFFICIENT_EVIDENCE.
"""
