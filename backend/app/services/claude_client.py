# claude_client.py
# Purpose: async Anthropic SDK wrapper — forced tool-calling for guaranteed structured output.
# Locked decision: tool_choice forces the "format_resume" tool so output is never
# markdown-fenced JSON that could fail json.loads().

# async def call_claude(system_prompt: str, user_prompt: str) -> dict:
#     - Calls client.messages.create() with:
#         model=settings.claude_model, max_tokens=8192 (NOT 4096 — long resumes truncate),
#         tools=[{"name": "format_resume", "input_schema": TailorResponse.model_json_schema()}],
#         tool_choice={"type": "tool", "name": "format_resume"}
#     - Checks response.stop_reason == "max_tokens" -> raise/log explicitly instead of
#       silently returning truncated JSON
#     - Returns response.content[0].input (the raw tool-call dict)

# async def call_claude_with_retry(system_prompt: str, user_prompt: str) -> dict:
#     - Wraps call_claude() with exponential backoff (via utils/retry.py)
#     - Retries on 429/529 from Anthropic, capped at ~3 attempts
#     - Explicit timeout (~30s) so a hung call doesn't hold a worker indefinitely

# def parse_and_validate(tool_input: dict) -> TailorResponse:
#     - Pydantic-validates the raw tool call dict against TailorResponse
#     - Raises a clear validation error if Claude's output doesn't match schema
