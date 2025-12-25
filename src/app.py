import streamlit as st
import json
import os
import glob

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Intelligent Document Experience Assistant",
    layout="wide"
)

# ---------------- Constants ----------------
ARTIFACT_DIR = "artifacts/analysis_results"
ANCHOR_LINE = "Respond clearly with bullet points where appropriate."

# ---------------- Helpers ----------------
@st.cache_data(show_spinner=False)
def load_documents():
    docs = {}
    files = sorted(glob.glob(os.path.join(ARTIFACT_DIR, "*.json")))
    for f in files:
        with open(f, "r", encoding="utf-8") as jf:
            payload = json.load(jf)
            docs[payload["doc_id"]] = payload
    return docs

def parse_text_blocks(text: str):
    """
    Returns:
    - extracted_text: everything before '\n\nTask:'
    - task_text: text between 'Task:' and anchor line
    - insights_text: text after anchor line
    """
    extracted_text = ""
    task_text = ""
    insights_text = ""

    if "\n\nTask:" in text:
        extracted_text, remainder = text.split("\n\nTask:", 1)
    else:
        extracted_text = text
        remainder = ""

    if ANCHOR_LINE in remainder:
        task_text, insights_text = remainder.split(ANCHOR_LINE, 1)
    else:
        task_text = remainder
        insights_text = ""

    return (
        extracted_text.strip(),
        task_text.strip(),
        insights_text.strip()
    )

def persona_overview(persona: str) -> str:
    if persona == "Author":
        return "An Author reviewing the document to improve clarity, structure, and tone."
    if persona == "Reviewer":
        return "A Reviewer evaluating the document for gaps, risks, and inconsistencies."
    if persona == "End User":
        return "An End User reading the document for simplified understanding."
    return ""

# ---------------- Load Data ----------------
documents = load_documents()
doc_ids = [""] + list(documents.keys())

# ---------------- Header ----------------
st.markdown("## 📄 Intelligent Document Experience Assistant")
st.caption(
    "Persona-aware document insights generated offline using enterprise-grade LLMs. "
    "Designed for clarity, review, and decision support."
)

st.markdown("---")

# ---------------- Controls ----------------
col1, col2 = st.columns([2, 1])

with col1:
    selected_doc = st.selectbox("Document", doc_ids, index=0)

with col2:
    persona = st.selectbox("Persona", ["", "Author", "Reviewer", "End User"], index=0)

if not selected_doc:
    st.info("Select a document to begin.")
    st.stop()

if not persona:
    st.info("Select a persona to view insights.")
    st.stop()

payload = documents[selected_doc]
analysis = payload["analysis"]
raw_text = analysis[persona]["text"]

extracted_text, task_text, insights_text = parse_text_blocks(raw_text)

st.markdown("---")

# ---------------- Layout ----------------
main, side = st.columns([3, 1])

# ---------------- Main Content ----------------
with main:
    st.markdown(f"### {persona} Insights")

    # Extracted Document Text
    if extracted_text:
        st.markdown("**Extracted Document Text**")
        st.markdown(extracted_text)
        st.markdown("")

    # Overview
    st.markdown("**Overview**")
    st.markdown(persona_overview(persona))
    st.markdown("")

    # Task
    if task_text:
        st.markdown("**Task**")
        st.markdown(task_text)
        st.markdown("")

    # Persona Insights
    st.markdown(f"**{persona} Insights**")
    st.markdown(insights_text)

# ---------------- Side Panel ----------------
with side:
    st.markdown("### Document Overview")
    st.markdown(f"**Name:** {selected_doc}")

    st.markdown("---")

    st.markdown("### Available Personas")
    st.markdown(
        "- **Author** – clarity, structure, tone\n"
        "- **Reviewer** – gaps, risks, consistency\n"
        "- **End User** – simplified understanding"
    )

    st.markdown("---")

    st.markdown("### Confidence Indicator")
    st.metric(
        label="Relevance Score",
        value=analysis[persona]["confidence"]
    )

    st.markdown("---")

    st.markdown("### Source Document")
    st.caption(
        "Original PDF processed offline using OCR and native text extraction. "
        "Live preview intentionally disabled for performance and stability."
    )

# ---------------- Footer ----------------
st.markdown("---")
st.caption(
    "Architecture: PDF → OCR/Text Extraction → Persona-aware LLM reasoning (Kaggle GPU) → "
    "Structured artifacts → Interactive review UI"
)
