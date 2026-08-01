# extract.py
# Purpose: /api/v1/extract endpoint — Phase 1, one-time PDF -> text extraction.

# router = APIRouter(prefix="/api/v1", tags=["extract"])

# @router.post("/extract", response_model=ExtractResponse)
# async def extract_resume(file: UploadFile = File(...)) -> ExtractResponse:
#     - 1. validate_file_size(file) — reject if > 5MB, raise 422
#     - 2. Read file bytes, pass to pdf_extractor.extract_text()
#     - 3. clean_extracted_text() to strip page numbers/repeated headers
#     - 4. score_extraction_confidence() on the cleaned text
#     - 5. Return ExtractResponse(resume_text=..., extraction_confidence=...)
