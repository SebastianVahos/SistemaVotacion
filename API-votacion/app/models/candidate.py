from sqlalchemy import Column, Integer, String
from app.database import Base


class Candidate(Base):
    __tablename__ = "candidate"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False)
    party = Column(String(100), nullable=True)
    votes = Column(Integer, default=0, nullable=False)
    email = Column(String(50), unique=True, nullable=False)