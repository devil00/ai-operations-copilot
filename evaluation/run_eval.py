import json

from app.retrieval import Retriever
from app.knowledge import KNOWLEDGE_BASE


def main():
    with open("evaluation/dataset.json", encoding="utf-8") as file:
        dataset = json.load(file)

    retriever = Retriever(KNOWLEDGE_BASE)

    hits = 0

    for case in dataset:
        results = retriever.retrieve(case["question"], top_k=3)
        docs = [chunk.document_id for chunk, _ in results]

        found = case["expected_document"] in docs
        hits += int(found)

        print(
            f"question={case['question']!r}\n"
            f"expected={case['expected_document']}\n"
            f"retrieved={docs}\n"
            f"hit={found}\n"
        )

    recall_at_3 = hits / len(dataset)
    print(f"Recall@3: {recall_at_3:.3f}")


if __name__ == "__main__":
    main()
