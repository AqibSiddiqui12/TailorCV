# health.py
# Purpose: liveness probe for Fly.io / CI / uptime checks.

# router = APIRouter(tags=["health"])

# @router.get("/healthz")
# async def health_check() -> dict:
#     - Returns {"status": "ok"}
#     - No auth, no dependencies — must always respond fast even if Redis/Claude are down
