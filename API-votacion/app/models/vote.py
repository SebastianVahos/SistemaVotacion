from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base


class Vote(Base):
    __tablename__ = "vote"

    id = Column(Integer, primary_key=True, index=True)
    voter_id = Column(Integer, ForeignKey("voter.id"), unique=True)
    candidate_id = Column(Integer, ForeignKey("candidate.id"))