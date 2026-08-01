# logging.py
# Purpose: structlog configuration — JSON logs with request IDs / correlation IDs.

# def configure_logging() -> None:
#     - Sets up structlog processors: timestamp, log level, JSON renderer,
#       exception formatting
#     - Integrates with stdlib logging so third-party libs (uvicorn, httpx) also
#       flow through the same formatter
#     - Called once at app startup (main.py lifespan)

# def get_logger(name: str) -> BoundLogger:
#     - Returns a structlog bound logger for a given module
#     - Callers can .bind(request_id=..., endpoint=...) for per-request context

# def log_request_metrics(endpoint: str, duration_ms: float, status_code: int) -> None:
#     - Emits a structured log line per request for observability/alerting
