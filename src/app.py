import streamlit as st
import json
import os
import glob

st.set_page_config(
    page_title="Intelligent Document Experience Assistant",
    layout="wide"
)

st.title("📄 Intelligent Document Experience Assistant")
st.caption("Persona-aware document insights generated using enterprise-grade LLMs")

ARTIFACT_DIR = "artifacts/analysis_results"

# ---- Validate artifacts folder ----
if not os.path.exists(ARTIFACT_DIR):
    st.error(f"Artifacts folder not found at `{ARTIFACT_DIR}`")
    st.stop()

json_files = sorted(glob.glob(os.path.join(ARTIFACT_DIR, "*.json")))

if not json_files:
    st.error("No analysis JSON files found in artifacts/analysis_results/")
    st.stop()

# ---- Document selector ----
doc_ids = [os.path.basename(f).replace(".json", "") for f in json_files]
selected_doc = st.selectbox("Select document", doc_ids)

# ---- Load selected document ----
selected_path = os.path.join(ARTIFACT_DIR, f"{selected_doc}.json")
with open(selected_path, "r", encoding="utf-8") as f:
    data = json.load(f)

analysis = data.get("analysis", {})

# ---- Persona selector ----
persona = st.selectbox("Select persona", ["Author", "Reviewer", "End User"])

st.subheader(f"{persona} Insights")
st.markdown(analysis[persona]["text"])

st.info(f"Confidence score: {analysis[persona]['confidence']}")

# ---- Explanation ----
with st.expander("How this analysis was generated"):
    st.markdown("""
- PDFs processed offline on **Kaggle** using **Mistral-7B-Instruct**
- Hybrid PDF text extraction (native + OCR fallback)
- Persona-aware reasoning (Author / Reviewer / End User)
- Outputs saved as JSON artifacts
- This demo visualizes precomputed results (no live LLM calls)
""")
