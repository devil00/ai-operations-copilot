# AI Operations Copilot Roadmap

## Phase 1 — Baseline RAG
- [x] Basic retrieval
- [x] Grounded prompt
- [x] Citation objects
- [x] Abstention
- [x] Retrieval evaluation

## Phase 2 — Production RAG
- [ ] Sentence-transformer embeddings
- [ ] PostgreSQL + pgvector
- [ ] BM25
- [ ] Hybrid retrieval
- [ ] Cross-encoder reranking
- [ ] Metadata filtering
- [ ] Chunking experiments
- [ ] Recall@K / MRR / NDCG benchmark

## Phase 3 — Agent
- [ ] LangGraph state graph
- [ ] Order lookup tool
- [ ] Payment lookup tool
- [ ] Incident search tool
- [ ] Refund recommendation
- [ ] Human approval
- [ ] Agent trajectory evaluation

## Phase 4 — LLMOps
- [ ] Prompt registry
- [ ] Model registry
- [ ] OpenTelemetry traces
- [ ] Langfuse/Phoenix
- [ ] Token/cost tracking
- [ ] Online evaluation
- [ ] Regression gates
- [ ] Canary model/prompt release
- [ ] Rollback

## Phase 5 — Model Engineering
- [ ] LoRA fine-tuning
- [ ] QLoRA experiment
- [ ] Specialist classifier
- [ ] vLLM serving
- [ ] FP16/INT8/INT4 benchmark
- [ ] KV-cache/inference benchmark
- [ ] Model routing

## Phase 6 — Safety
- [ ] Prompt-injection dataset
- [ ] RAG poisoning tests
- [ ] PII detection/masking
- [ ] Tool authorization
- [ ] Cross-tenant isolation
- [ ] Audit trail
- [ ] High-risk action approval
