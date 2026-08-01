# rate_limit.py
# Purpose: Redis-backed token bucket rate limiting on /api/v1/tailor.
# NOTE: no auth system exists, so this is per-IP, not truly per-user
# (deliberate tradeoff for a free tool — weaker under shared IPs/VPNs/NAT).

# async def rate_limit_middleware(request: Request, call_next):
#     - Extracts client IP (or API key if added later) as the bucket key
#     - Checks/decrements token bucket in Redis (via redis_client.get_redis_client())
#     - If bucket empty -> return 429 with Retry-After header, never queue silently
#     - Otherwise -> await call_next(request)

# def get_bucket_key(request: Request) -> str:
#     - Builds the Redis key, e.g. f"ratelimit:{client_ip}"
