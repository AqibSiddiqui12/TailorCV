# test_extract.py
# Purpose: tests for /api/v1/extract endpoint.

# async def test_extract_valid_pdf(async_client):
#     - Uploads a small sample PDF fixture
#     - Asserts 200, resume_text non-empty, extraction_confidence between 0-1

# async def test_extract_oversized_file_rejected(async_client):
#     - Uploads a file > max_upload_mb
#     - Asserts 422

# async def test_extract_non_pdf_rejected(async_client):
#     - Uploads a .txt file disguised or wrong content-type
#     - Asserts 422

# def test_score_extraction_confidence_heuristic():
#     - Unit test on pdf_extractor.score_extraction_confidence() with
#       good text vs. garbage text, asserts expected relative scores
