# Architecture

## Current baseline

```text
Client
  |
  v
FastAPI
  |
  v
Copilot
  |
  +--> Retriever
  |      |
  |      +--> Knowledge Base
  |
  +--> Grounded Prompt
  |
  +--> LLM
  |
  v
Structured Response
  |
  +--> Answer
  +--> Citations
  +--> Confidence
```

## Target architecture

```text
                         +----------------+
                         |    Client      |
                         +-------+--------+
                                 |
                                 v
                         +---------------+
                         |  AI Gateway   |
                         +-------+-------+
                                 |
                         +-------v-------+
                         | Model Router  |
                         +-------+-------+
                                 |
                    +------------+------------+
                    |                         |
                    v                         v
              +-----------+             +-----------+
              | RAG Engine |             |  Agent    |
              +-----+-----+             +-----+-----+
                    |                         |
             retrieve/rerank              tools
                    |                         |
                    +------------+------------+
                                 |
                                 v
                              LLM
                                 |
                    +------------+-------------+
                    |                          |
                    v                          v
             Claim validation          Trace/evaluation
                    |                          |
                    v                          v
                 Answer                 LLMOps platform
```
