from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@dataclass(frozen=True)
class DocumentChunk:
    document_id: str
    chunk_id: str
    text: str


class Retriever:
    def __init__(self, chunks: list[DocumentChunk]):
        self.chunks = chunks
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words="english",
            ngram_range=(1, 2),
        )
        self.matrix = self.vectorizer.fit_transform(
            [chunk.text for chunk in chunks]
        )

    def retrieve(self, query: str, top_k: int = 5) -> list[tuple[DocumentChunk, float]]:
        query_vector = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vector, self.matrix)[0]

        ranked = sorted(
            enumerate(scores),
            key=lambda item: item[1],
            reverse=True,
        )

        return [
            (self.chunks[index], float(score))
            for index, score in ranked[:top_k]
        ]
