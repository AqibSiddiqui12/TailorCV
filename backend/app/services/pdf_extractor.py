import io

import pdfplumber


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
        if item.lower().startswith(("page", "1/2")):
            continue

        clean_text.append(item)
    return "\n".join(clean_text)


def score_extraction_confidence(text: str) -> float:
    confidence = 0.0
    text = text.lower()

    if len(text) > 300:
        confidence += 0.3

    if "@" in text:
        confidence += 0.2

    if "experience" in text:
        confidence += 0.2

    if "education" in text:
        confidence += 0.2

    if "skills" in text:
        confidence += 0.1

    return min(confidence, 1.0)
