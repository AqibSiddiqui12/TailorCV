# Dockerfile
# Purpose: multi-stage build — builder stage installs deps, runtime stage is slim.

# FROM python:3.12-slim AS builder
#   - Install uv, copy pyproject.toml + uv.lock, run `uv sync --no-dev`

# FROM python:3.12-slim AS runtime
#   - Copy only the built venv/site-packages from builder (COPY --from=builder)
#   - Copy app/ source
#   - Create + switch to a non-root user
#   - EXPOSE 8000
#   - CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#   - HEALTHCHECK CMD curl -f http://localhost:8000/healthz || exit 1
