# pdf_extractor.py
# Purpose: turn an uploaded PDF resume into clean plain text (Phase 1).
# Locked decision: pdfplumber with layout=True — avoids jumbling multi-column resumes.

# def extract_text(file_bytes: bytes) -> str:
#     - Opens PDF via pdfplumber.open(io.BytesIO(file_bytes))
#     - Joins page.extract_text(layout=True) across all pages
#     - Returns raw extracted text (pre-cleaning)


import pdfplumber
import io


#     
def extract_text(file_bytes: bytes) -> str:
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        raw_text = ""

        for page in pdf.pages:
            page_content = page.extract_text(layout=True)

            if page_content:
                raw_text += page_content + "\n"

    return raw_text

def clean_extracted_text(raw_text: str) -> str:
    raw_text = raw_text.splitlines()
    clean_text = []
    for item in raw_text:
        item = item.strip()
        if not item:
            continue
        if item.lower().startswith(("page", "page 1", "1/2")):
            continue

        clean_text.append(item)
    return "\n".join(clean_text)


# def score_extraction_confidence(text: str) -> float:
#     - Heuristic 0-1 score: checks text length, presence of expected resume
#       keywords (e.g. "experience", "education", email pattern)
#     - Low score -> flag to user that the PDF parse may be unreliable
def score_extraction_confidence(text: str) -> float:
    pass
