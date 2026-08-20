import os
from typing import List, Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

class ContactInfo(BaseModel):
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    links: List[str] = Field(default_factory=list)

class ExperienceItem(BaseModel):
    company: str
    title: str
    dates: str
    bullets: List[str]

class ProjectItem(BaseModel):
    name: str
    bullets: List[str]

class EducationItem(BaseModel):
    institution: str
    degree: str
    dates: str

# NEW: Category schema for skills
class SkillCategory(BaseModel):
    category: str
    items: List[str]

class TailoredCV(BaseModel):
    name: str
    target_company: str  # <--- NEW FIELD
    contact: ContactInfo
    summary: str
    experience: List[ExperienceItem]
    projects: List[ProjectItem]
    education: List[EducationItem]
    skills: List[SkillCategory]

SYSTEM_INSTRUCTION = """
You are an expert professional resume writer.

The master CV provided as an attached PDF is the ONLY source of truth about the candidate.
Read the complete master CV and the target job description.
Generate a complete, professional CV tailored specifically to the target job.

Rules:
1. Every factual claim must be backed by the master CV.
2. You MAY rewrite wording, adapt phrasing, reorder bullets, improve the summary, and emphasize relevant skills and achievements.
3. You MUST NOT invent employers, dates, titles, skills, certifications, metrics, responsibilities, achievements, technologies, projects, or qualifications.
4. Group skills into logical categories (e.g., Languages, Infrastructure, Databases, Tools).
5. Return ONLY structured data conforming to the supplied schema.
6. Preserve section order exactly as given in the master CV (e.g. Education, Experience, Projects, Skills). Only reorder content within a section, never the sections themselves.
7. Adding a new skill or keyword to the Skills section requires it to already appear, in substance, somewhere in the master CV. Never add a skill inferred from the job description alone, even if it seems like a safe guess.
8. Mirror the job description's specific, recurring vocabulary throughout the tailored bullets, not just once, so the tailored CV reads in the employer's own language wherever a truthful match exists. Do not force a keyword match where no genuine underlying fact supports it.
9. If the job description asks for a skill, tool, or domain not present in the master CV, omit it entirely from the tailored CV rather than implying it through vague or adjacent language.
10. Every bullet in the tailored output must read as a genuine, compelling, specific claim, not a generic restatement. Avoid filler adjectives unconnected to a concrete fact from the master CV.
11. Do not fabricate or estimate quantitative metrics (percentages, dollar amounts, team sizes, time savings) unless that exact figure appears in the master CV.
12. If the master CV does not contain enough relevant material to credibly address a major requirement in the job description, do not compensate by overweighting a loosely related bullet, leave the gap visible rather than papered over.
"""

def generate_tailored_cv(pdf_bytes: bytes, job_description: str) -> TailoredCV:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=[
            types.Part.from_bytes(
                data=pdf_bytes,
                mime_type="application/pdf"
            ),
            f"TARGET JOB DESCRIPTION:\n{job_description}"
        ],
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            response_mime_type="application/json",
            response_schema=TailoredCV,
            temperature=0.2,
        )
    )

    if response.parsed:
        return response.parsed

    return TailoredCV.model_validate_json(response.text)