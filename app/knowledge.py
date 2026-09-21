from app.retrieval import DocumentChunk


KNOWLEDGE_BASE = [
    DocumentChunk(
        document_id="delivery_policy_v1",
        chunk_id="delivery-001",
        text=(
            "Customers may be eligible for compensation when an order is "
            "delayed beyond the threshold defined by the applicable delivery "
            "policy. Eligibility depends on the reason for the delay and the "
            "specific policy version applicable to the order."
        ),
    ),
    DocumentChunk(
        document_id="refund_policy_v3",
        chunk_id="refund-001",
        text=(
            "A customer may qualify for a refund when an order is cancelled "
            "by the platform or when a qualifying service failure occurs. "
            "The final refund amount must be determined using the applicable "
            "refund rules; an assistant must not invent an amount."
        ),
    ),
    DocumentChunk(
        document_id="payment_policy_v2",
        chunk_id="payment-001",
        text=(
            "A payment marked as failed should not be treated as successful "
            "solely because a client request was accepted. Payment status "
            "must be confirmed from the authoritative payment record."
        ),
    ),
    DocumentChunk(
        document_id="support_policy_v1",
        chunk_id="support-001",
        text=(
            "Sensitive actions such as refunds require an authorized "
            "workflow. An AI assistant may recommend an action but must not "
            "bypass authorization or approval controls."
        ),
    ),
]
