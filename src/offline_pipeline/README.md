### Offline Analysis Pipeline (Kaggle)

The document intelligence pipeline is executed offline using Kaggle GPUs.
It includes:

- Hybrid PDF text extraction (native + OCR fallback)
- Persona-aware prompt design
- LLM inference using Mistral-7B-Instruct
- Structured JSON artifact generation

The live HuggingFace demo visualizes precomputed artifacts to ensure
performance, cost-efficiency, and deterministic behavior.
