# tailor.py
# Purpose: /api/v1/tailor endpoint — orchestrates the full Phase 2-7 pipeline.

# router = APIRouter(prefix="/api/v1", tags=["tailor"])

# @router.post("/tailor", response_class=Response)  # returns raw .docx bytes
# async def tailor_resume(payload: TailorRequest) -> Response:
#     - 1. Build system + user prompt via prompt_builder.build_system_prompt/build_user_prompt
#     - 2. Call claude_client.call_claude_with_retry(system_prompt, user_prompt)
#     - 3. Validate raw tool output -> TailorResponse via claude_client.parse_and_validate
#     - 4. Pass validated TailorResponse into docx_generator.generate_docx()
#     - 5. Return docx bytes with correct media_type
#         ("application/vnd.openxmlformats-officedocument.wordprocessingml.document")
#     - 6. On Claude failure after retries -> raise HTTPException(502)
