# redis_client.py
# Purpose: single owner of the Redis connection/pool used by rate_limit middleware.

# async def get_redis_client() -> Redis:
#     - Creates (or returns cached) async Redis client from settings.redis_url
#     - Used as a dependency / imported singleton by middleware/rate_limit.py

# async def close_redis_client() -> None:
#     - Gracefully closes the connection pool
#     - Called from main.py's lifespan shutdown block
