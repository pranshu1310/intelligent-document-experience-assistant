import json, os, re

TEXT_PATH = "/kaggle/working/intermediate_text.json"
ANALYSIS_PATH = "/kaggle/working/intermediate_analysis.json"
FINAL_DIR = "/kaggle/working/analysis_results_batch"

def confidence_score(output, source):
    tokens = [w for w in re.findall(r"\b\w{5,}\b", output)]
    matched = sum(1 for w in tokens if w.lower() in source.lower())
    return round(matched / max(1, len(tokens)), 2)

def main():
    os.makedirs(FINAL_DIR, exist_ok=True)

    with open(TEXT_PATH) as f:
        texts = json.load(f)

    with open(ANALYSIS_PATH) as f:
        outputs = json.load(f)

    for doc_id in texts:
        analysis = {}

        for persona, text in outputs[doc_id].items():
            conf = confidence_score(text, texts[doc_id])
            analysis[persona] = {
                "text": text,
                "confidence": conf
            }

        out = {
            "doc_id": doc_id,
            "analysis": analysis
        }

        out_path = os.path.join(FINAL_DIR, f"{doc_id}.json")
        with open(out_path, "w") as f:
            json.dump(out, f, indent=2)

        print(f"✅ Saved {out_path}")

if __name__ == "__main__":
    main()
