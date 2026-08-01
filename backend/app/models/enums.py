from enum import StrEnum


class Language(StrEnum):
    ENGLISH = "en"
    GERMAN = "de"


class CVType(StrEnum):
    TECH = "tech"
    BUSINESS_NON_TECHNICAL = "business_non_technical"
