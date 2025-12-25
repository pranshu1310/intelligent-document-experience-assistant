import os, json
from src.offline_pipeline.pdf_extraction import extract_text_from_pdf


PDF_DIR = "/kaggle/input/testv3demo"
OUT_PATH = "/kaggle/working/intermediate_text.json"

def main():
    results = {}

    pdfs = [f for f in os.listdir(PDF_DIR) if f.lower().endswith(".pdf")]
    print(f"Found {len(pdfs)} PDFs")

    for pdf in pdfs:
        doc_id = pdf.replace(".pdf", "")
        path = os.path.join(PDF_DIR, pdf)

        print(f"📄 Extracting: {doc_id}")
        text = extract_text_from_pdf(path)
        results[doc_id] = text[:2000]  # context safety

    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"✅ Saved extracted text to {OUT_PATH}")

if __name__ == "__main__":
    main()
