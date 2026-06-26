from sqlalchemy.orm import Session

from app.models.candidate import Candidate


class CandidateRepository:

    def get_by_email(self, db: Session, email: str):

        return (
            db.query(Candidate)
            .filter(Candidate.email == email)
            .first()
        )