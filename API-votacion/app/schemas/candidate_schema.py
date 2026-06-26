from pydantic import BaseModel, EmailStr
from typing import Optional

class CandidateCreate(BaseModel):
    name: str
    party: Optional[str] = None
    email: EmailStr

class CandidateResponse(BaseModel):
    id: int
    name: str
    party: Optional[str]
    votes: int
    email: EmailStr
    
    class Config:
        from_attributes = True
    