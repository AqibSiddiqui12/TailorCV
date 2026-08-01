# cors.py
# Purpose: allow the Chrome extension origin to call the backend.
# NOTE: must allow chrome-extension://<extension-id>, not a normal domain,
# or requests fail in-browser before reaching FastAPI.

# def configure_cors(app: FastAPI) -> None:
#     - app.add_middleware(CORSMiddleware,
#         allow_origins=[settings.allowed_origin],
#         allow_methods=["POST"],
#         allow_headers=["Content-Type"])
#     - Called once from main.py's create_app()
