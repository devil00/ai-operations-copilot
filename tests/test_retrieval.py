from app.knowledge import KNOWLEDGE_BASE
from app.retrieval import Retriever


def test_payment_query_retrieves_payment_policy():
    retriever = Retriever(KNOWLEDGE_BASE)

    results = retriever.retrieve(
        "Can a failed payment be considered successful?",
        top_k=3,
    )

    document_ids = [chunk.document_id for chunk, _ in results]

    assert "payment_policy_v2" in document_ids


def test_refund_query_retrieves_refund_policy():
    retriever = Retriever(KNOWLEDGE_BASE)

    results = retriever.retrieve(
        "When can a customer receive a refund?",
        top_k=3,
    )

    document_ids = [chunk.document_id for chunk, _ in results]

    assert "refund_policy_v3" in document_ids
