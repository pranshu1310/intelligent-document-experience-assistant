import json, os
from llm_inference import load_generator, run_generation

INPUT_PATH = "/kaggle/working/intermediate_text.json"
OUT_PATH = "/kaggle/working/intermediate_analysis.json"

persona_tasks = {
    "Author": "Summarize briefly and list 3 concrete improvements for clarity, structure or tone.",
    "Reviewer": "List missing or weak sections and any risks or inconsistencies.",
    "End User": "Explain the document in simple non-technical language (3–4 sentences)."
}

def main():
    with open(INPUT_PATH) as f:
        docs = json.load(f)

    gen = load_generator()
    results = {}

    for doc_id, text in docs.items():
        print(f"🧠 Generating insights for {doc_id}")
        results[doc_id] = {}

        for persona, task in persona_tasks.items():
            prompt = f"""
You are a {persona} analyzing an enterprise document.

Document:
{text}

Task:
{task}

Respond clearly with bullet points where appropriate.
"""
            output = run_generation(gen, prompt)
            results[doc_id][persona] = output

    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"✅ Saved raw LLM outputs to {OUT_PATH}")

if __name__ == "__main__":
    main()
