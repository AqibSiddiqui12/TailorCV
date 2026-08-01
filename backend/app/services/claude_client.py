from anthropic import AsyncAnthropic
from app.config import settings
from app.models.responses import TailorResponse


async def call_claude(system_prompt: str, user_prompt: str) -> dict:

    # async def call_claude(system_prompt: str, user_prompt: str) -> dict:
    #     - Calls client.messages.create() with:
    #         model=settings.claude_model, max_tokens=8192 (NOT 4096 — long resumes truncate),
    #         tools=[{"name": "format_resume", "input_schema": TailorResponse.model_json_schema()}],
    #         tool_choice={"type": "tool", "name": "format_resume"}
    #     - Checks response.stop_reason == "max_tokens" -> raise/log explicitly instead of
    #       silently returning truncated JSON
    #     - Returns response.content[0].input (the raw tool-call dict)
    client = AsyncAnthropic(api_key=settings.anthropic_api_key)
    response = await client.messages.create(
        model=settings.claude_model,
        max_tokens=8192,
        system=system_prompt,
        user={
            "role":"user",
            "content": user_prompt
        },
        tools=[
            {
                "name": "format_resume",
                "input_schema": TailorResponse.model_json_schema(),
            }
        ],
        tool_choice={"type": "tool", "name": "format_resume"},
    )
    if response.stop_reason == "max_tokens":
        raise ValueError("Claude response was truncated because it reached max_tokens.")

    return response.content[0].input


async def call_claude_with_retry(system_prompt: str, user_prompt: str) -> dict:
    pass


# async def call_claude_with_retry(system_prompt: str, user_prompt: str) -> dict:
#     - Wraps call_claude() with exponential backoff (via utils/retry.py)
#     - Retries on 429/529 from Anthropic, capped at ~3 attempts
#     - Explicit timeout (~30s) so a hung call doesn't hold a worker indefinitely


def parse_and_validate(tool_input: dict) -> TailorResponse:
    pass


# def parse_and_validate(tool_input: dict) -> TailorResponse:
#     - Pydantic-validates the raw tool call dict against TailorResponse
#     - Raises a clear validation error if Claude's output doesn't match schema
