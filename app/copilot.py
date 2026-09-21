from app.knowledge import KNOWLEDGE_BASE
from app.llm import build_llm
from app.prompt import build_prompt
from app.retrieval import Retriever
from app.schemas import Citation, CopilotResponse


class Copilot:
    def __init__(self):
        self.retriever = Retriever(KNOWLEDGE_BASE)
        self.llm = None

    def _get_llm(self):
        if self.llm is None:
            self.llm = build_llm()
        return self.llm

    def answer(self, question: str) -> dict:
        results = self.retriever.retrieve(question, top_k=3)

        # Baseline evidence threshold. Tune this using an evaluation dataset.
        usable = [
            (chunk, score)
            for chunk, score in results
            if score >= 0.10
        ]

        if not usable:
            return CopilotResponse(
                decision="INSUFFICIENT_EVIDENCE",
                answer="I do not have enough evidence to answer that question.",
                citations=[],
                confidence=0.0,
                retrieved_chunks=0,
            ).model_dump()

        chunks = [chunk for chunk, _ in usable]
        prompt = build_prompt(question, chunks)

        try:
            answer = self._get_llm().generate(prompt)
        except ValueError:
            # Useful when running retrieval tests without configuring an LLM.
            answer = (
                "LLM is not configured. Retrieved evidence: "
                + " ".join(chunk.text for chunk in chunks)
            )

        if "INSUFFICIENT_EVIDENCE" in answer:
            decision = "INSUFFICIENT_EVIDENCE"
        else:
            decision = "ANSWER"

        citations = [
            Citation(
                document_id=chunk.document_id,
                chunk_id=chunk.chunk_id,
                quote=chunk.text,
            )
            for chunk in chunks
        ]

        confidence = min(
            1.0,
            max(score for _, score in usable),
        )

        return CopilotResponse(
            decision=decision,
            answer=answer,
            citations=citations,
            confidence=confidence,
            retrieved_chunks=len(chunks),
        ).model_dump()
