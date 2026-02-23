from pydantic import BaseModel
from typing import Optional

class MoviePreferences(BaseModel):
    genre: str
    era: str  # "classic" or "modern"
    country: Optional[str]
    duration: str  # "short" or "long"

# reminder for later implementation: country can be any

class MovieResponse(BaseModel):
    recommendations: list[str]
