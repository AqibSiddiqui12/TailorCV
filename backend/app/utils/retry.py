# retry.py
# Purpose: generic exponential backoff wrapper, used by claude_client.py.

# async def retry_with_backoff(fn: Callable, *args, max_attempts: int = 3,
#                               retry_on: tuple[type[Exception], ...], **kwargs):
#     - Calls fn(*args, **kwargs)
#     - On an exception matching retry_on (e.g. rate-limit/server errors) ->
#       wait with exponential backoff (e.g. 2**attempt seconds) and retry
#     - After max_attempts, re-raises the last exception
#     - Used to wrap the raw Anthropic API call, not the whole route
