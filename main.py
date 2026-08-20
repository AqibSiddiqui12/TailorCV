import base64
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from gemini import generate_tailored_cv
from docx_generator import create_docx

app = FastAPI(title="TailorCV Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["*"],
)
@app.get("/ping")
async def ping():
    return {"status": "awake"}
class GenerateRequest(BaseModel):
    master_cv: str  # Base64 Data URL string
    job_description: str

@app.post("/generate")
async def generate_cv(payload: GenerateRequest):
    try:
        raw_b64 = payload.master_cv.split(",", 1)[-1]
        pdf_bytes = base64.b64decode(raw_b64)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Base64 PDF data.")

    try:
        tailored_cv_model = generate_tailored_cv(
            pdf_bytes=pdf_bytes,
            job_description=payload.job_description
        )
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Gemini processing error: {str(e)}")

    try:
        docx_stream = create_docx(tailored_cv_model)
        
        # --- NEW: Format the dynamic filename ---
        safe_name = tailored_cv_model.name.replace(" ", "_")
        safe_company = tailored_cv_model.target_company.replace(" ", "_")
        file_name = f"{safe_name}_{safe_company}_CV.docx"
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"DOCX compilation error: {str(e)}")

    return StreamingResponse(
        docx_stream,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={
            "Content-Disposition": f'attachment; filename="{file_name}"',
            # We must expose this header so the Chrome extension can read it
            "Access-Control-Expose-Headers": "Content-Disposition" 
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
