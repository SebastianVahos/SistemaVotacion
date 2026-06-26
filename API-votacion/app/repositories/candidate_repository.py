from sqlalchemy.orm import Session

from app.models.candidate import Candidate
from app.schemas.candidate_schema import CandidateCreate

class CandidateRepository:

    def create(self, db: Session, candidate: CandidateCreate):
        new_candidate = Candidate(
            name = candidate.name,
            party = candidate.party,
            email = candidate.email,
        )

        db.add(new_candidate)
        db.commit()
        db.refresh(new_candidate)

        return new_candidate

    def get_by_email(self, db: Session, email: str):

        return (
            db.query(Candidate)
            .filter(Candidate.email == email)
            .first()
        )
    
    def get_all(self, db: Session):
        return db.query(Candidate).all()
    
    def get_by_id(self, db: Session, candidate_id: int):
        return (
            db.query(Candidate)
            .filter(Candidate.id == candidate_id)
            .first()
        )
    
    def delete(self, db: Session, candidate_id: int):
        candidate = self.get_by_id(db, candidate_id)
        if candidate:
            db.delete(candidate)
            db.commit()
        return candidate