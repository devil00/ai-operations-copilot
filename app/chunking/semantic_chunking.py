from llama_index.core import SimpleDirectoryReader

from llama_index.core.node_parser import (
    SentenceSplitter,
    SemanticSplitterNodeParser,
)

import os

documents = SimpleDirectoryReader(input_files=["app/input_files/pg_essay.txt"]).load_data()

os.environ["OPENAI_API_KEY"] = "sk-..."

def semantic_chunker():
    embed_model = OpenAIEmbedding()
    splitter = SemanticSplitterNodeParser(
        buffer_size=1, breakpoint_percentile_threshold=95, embed_model=embed_model
    )

    # also baseline splitter
    base_splitter = SentenceSplitter(chunk_size=512)
    nodes = splitter.get_nodes_from_documents(documents)


if __name__ == "__main__":
    semantic_chunker()
