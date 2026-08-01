# main.py
# Purpose: FastAPI app entrypoint — wires together routers, middleware, lifespan.

# def create_app() -> FastAPI:
#     - Instantiates FastAPI()
#     - Registers CORS middleware (from middleware/cors.py)
#     - Registers rate-limit middleware (from middleware/rate_limit.py)
#     - Includes routers: tailor, extract, health (with /api/v1 prefix where relevant)
#     - Attaches lifespan context manager (startup: init redis client / logging;
#       shutdown: close redis connection)

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     - Startup: connect redis_client, configure structlog
#     - yield
#     - Shutdown: close redis connection cleanly

# app = create_app()
#     - Module-level app instance uvicorn points to (app.main:app)
