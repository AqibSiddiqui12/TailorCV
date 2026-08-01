# test_tailor.py
# Purpose: tests for /api/v1/tailor endpoint.

# async def test_tailor_success(async_client):
#     - Mocks claude_client.call_claude_with_retry to return a fixed valid dict
#     - Posts a valid TailorRequest payload
#     - Asserts 200 + correct docx media_type in response

# async def test_tailor_invalid_payload_returns_422(async_client):
#     - Posts payload missing required fields / too-short resume
#     - Asserts 422, and that Claude was never called (mock not invoked)

# async def test_tailor_claude_failure_returns_502(async_client):
#     - Mocks claude_client to raise after retries exhausted
#     - Asserts 502 response

# async def test_tailor_each_cv_type_language_combo(async_client):
#     - Parametrized over (CVType.TECH/BUSINESS) x (Language.EN/DE)
#     - Asserts correct system prompt conventions were applied (via mock inspection)
