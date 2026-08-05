import asyncio
from anthropic import AsyncAnthropic, RateLimitError, InternalServerError
from app.config import settings
from app.models.responses import TailorResponse
from pydantic import ValidationError



async def call_claude(system_prompt: str, user_prompt: str) -> dict:

    client = AsyncAnthropic(api_key=settings.anthropic_api_key)
    response = await client.messages.create(
        model=settings.claude_model,
        max_tokens=8192,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
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
    for attempt in range(3):
        try:
            return await asyncio.wait_for(
                call_claude(system_prompt, user_prompt), timeout=30
            )
        except (RateLimitError, InternalServerError):
            if attempt == 2:
                raise
            await asyncio.sleep(2**attempt)


def parse_and_validate(tool_input: dict) -> TailorResponse:
    try:
        return TailorResponse.model_validate(tool_input)
    except ValidationError as e:
        raise ValueError("Claude's output doesn't match schema")
