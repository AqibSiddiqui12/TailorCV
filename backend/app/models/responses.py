from app.models.enums import CVType, Language
from pydantic import BaseModel, Field


class ContactBlock(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None
    location: str | None = None
    links: list[str] = Field(default_factory=list)


class EducationEntry(BaseModel):
    institution: str
    degree: str
    dates: str | None = None


class ResumeEntry(BaseModel):
    title: str
    subtitle: str | None = None
    bullets: list[str]


class ResumeSection(BaseModel):
    section_name: str
    order_index: int
    entries: list[ResumeEntry]


class TailorResponse(BaseModel):
    contact_info: ContactBlock
    education: list[EducationEntry] 
    sections: list[ResumeSection]
    cv_type: CVType
    language: Language


class ExtractResponse(BaseModel):
    resume_text: str
    extraction_confidence: float
