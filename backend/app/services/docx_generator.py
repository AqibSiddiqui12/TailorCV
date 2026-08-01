# docx_generator.py
# Purpose: turn a validated TailorResponse into a styled .docx file (Phase 7).
# Locked styling: Tech CV -> Arial/Calibri, navy (#003366) headings.
#                 Business CV -> Garamond/Georgia, neutral dark headings.
#                 Both: 0.75in margins, 1.15x line spacing, 2pt space after bullets.

# def apply_cv_type_styling(doc: Document, cv_type: CVType) -> None:
#     - Sets font family, margins, heading color/weight based on cv_type
#     - Applied once at the top of generate_docx() before content is written

# def render_contact_block(doc: Document, contact_info: ContactBlock) -> None:
#     - Writes name/email/phone/location/links as the document header block

# def render_section(doc: Document, section: ResumeSection) -> None:
#     - Writes one section: heading (section_name) + entries in order
#     - For each ResumeEntry: title, subtitle, then bullets (python-docx bullet list style)

# def generate_docx(tailor_response: TailorResponse) -> bytes:
#     - Creates a new Document()
#     - apply_cv_type_styling(doc, tailor_response.cv_type)
#     - render_contact_block(doc, tailor_response.contact_info)
#     - Iterates tailor_response.sections sorted by order_index, calling render_section()
#     - Writes doc to an in-memory BytesIO buffer, returns .getvalue()
