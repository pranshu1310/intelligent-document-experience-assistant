# Kaggle Inference Workflow

For deeper persona-based document analysis, a larger instruction-tuned language model was run on Kaggle using free GPU resources.

Steps:
1. OCR text generated locally or via HuggingFace Space
2. Text uploaded to Kaggle notebook
3. Mistral-7B-Instruct used for persona-aware reasoning
4. Outputs saved as JSON and committed to this repository under `artifacts/`

This approach mirrors real-world systems where heavy batch inference is separated from live user-facing applications.
