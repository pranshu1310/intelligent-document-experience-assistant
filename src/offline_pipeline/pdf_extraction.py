# pdf_extraction.py
import pdfplumber
import fitz
import pytesseract
from PIL import Image
import io, re, os

def extract_text_from_pdf(pdf_path, max_pages=3):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages[:max_pages]:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print("pdfplumber failed:", e)

    if len(text.strip()) > 300:
        return re.sub(r'\s+', ' ', text).strip()

    # Fallback to OCR via PyMuPDF
    print("⚠️ Falling back to OCR for:", os.path.basename(pdf_path))
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc[:max_pages]:
        pix = page.get_pixmap(dpi=200)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        text += pytesseract.image_to_string(img) + "\n"

    return re.sub(r'\s+', ' ', text).strip()
