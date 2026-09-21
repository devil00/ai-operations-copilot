# AI Operations Copilot

A GitHub-ready starter project for learning and demonstrating production AI engineering and LLMOps.

## What this starter implements

- FastAPI API
- Provider-agnostic LLM interface
- OpenAI Responses API adapter
- Evidence-grounded RAG
- TF-IDF baseline retrieval
- Structured output validation
- Explicit abstention when evidence is insufficient
- Citation tracking
- Safe simulated business tools
- Basic evaluation suite
- Unit tests

## Roadmap

1. Baseline RAG — included
2. Embeddings + pgvector
3. Hybrid retrieval + reranking
4. LangGraph agent
5. Agent/tool evaluation
6. OpenTelemetry + Langfuse/Phoenix
7. Prompt/model registry with MLflow
8. Model routing
9. LoRA/QLoRA specialist model
10. vLLM + quantization benchmark
11. AI safety and prompt-injection tests
12. Automated evaluation/release gates

## Setup

```bash
python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# Add your LLM API key and model to .env

uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## Example

```bash
curl -X POST http://127.0.0.1:8000/copilot/ask \
  -H 'Content-Type: application/json' \
  -d '{"question":"When is a delayed order eligible for compensation?"}'
```

## Evaluate

```bash
python -m evaluation.run_eval
```

## Test

```bash
pytest
```

## Design principle

Do not start with a huge framework. First establish a measurable baseline:

question -> retrieval -> evidence -> answer -> citations

Then improve one AI capability at a time and measure the effect.
