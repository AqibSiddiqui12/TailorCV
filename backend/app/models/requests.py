from app.models.enums import CVType, Language
from pydantic import BaseModel, Field


class TailorRequest(BaseModel):
    master_resume: str = Field(..., min_length=200, max_length=20000)
    job_description: str = Field(..., min_length=50, max_length=10000)
    cv_type: CVType
    language: Language
