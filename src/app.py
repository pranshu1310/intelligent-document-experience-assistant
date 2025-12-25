import streamlit as st
import json
import os

st.set_page_config(
    page_title="Intelligent Document Experience Assistant",
    layout="wide"
)

st.title("📄 Intelligent Document Experience Assistant")
st.caption("Persona-aware document insights generated using enterprise-grade LLMs")

# ---- Load Kaggle-generated analysis ----
ARTIFACT_PATH = "artifacts/analysis_results.json"

if not os.path.exists(ARTIFACT_PATH):
    st.error("Analysis artifact not found. Please upload analysis_results.json.")
    st.stop()

with open(ARTIFACT_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

analysis = data["analysis"]

# ---- UI ----
persona = st.selectbox(
    "Select Persona",
    ["Author", "Reviewer", "End User"]
)

st.subheader(f"{persona} Insights")

st.markdown(analysis[persona]["text"])

st.info(
    f"Confidence score: {analysis[persona]['confidence']} "
    "(based on overlap with original document text)"
)

# ---- Explain architecture ----
with st.expander("How this analysis was generated"):
    st.markdown("""
- OCR performed on uploaded document
- Text processed offline on Kaggle using **Mistral-7B-Instruct**
- Persona-aware insights generated using GPU acceleration
- Results saved and loaded here for interactive review
- No live LLM calls in this demo (responsible & cost-free design)
""")
