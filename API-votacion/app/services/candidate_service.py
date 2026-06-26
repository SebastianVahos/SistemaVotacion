from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.candidate_repository import CandidateRepository
from app.schemas.candidate_schema import CandidateCreate
from app.repositories.voter_repository import VoterRepository

candidate_repository = CandidateRepository()
voter_repository = VoterRepository()        

class CandidateService:

    def create(self, db: Session, candidate: CandidateCreate):

        existing_candidate = candidate_repository.get_by_email(
            db,
            candidate.email
        )

        if existing_candidate:
            raise HTTPException(
                status_code = 409,
                detail = "Ya existe un candidato con ese correo."
            )

        existing_voter = voter_repository.get_by_email(
            db,
            candidate.email
        )

        if existing_voter:
            raise HTTPException(
                status_code = 409,
                detail = "Ese correo pertenece a un votante."
            )

        return candidate_repository.create(db, candidate)

    def get_all(self, db: Session):
        candidates = candidate_repository.get_all(db)
        if not candidates:
            raise HTTPException(
                status_code = 404,
                detail = "No hay candidatos registrados."
            )

        return candidates

    def get_by_id(self, db: Session, candidate_id: int):
        candidate = candidate_repository.get_by_id(db, candidate_id)

        if candidate is None:
            raise HTTPException(
                status_code = 404,
                detail = "Candidato no encontrado."
            )

        return candidate

    def delete(self, db: Session, candidate_id: int):
        candidate = candidate_repository.get_by_id(db, candidate_id)

        if candidate is None:
            raise HTTPException(
                status_code = 404,
                detail = "Candidato no encontrado."
            )

        return candidate_repository.delete(db, candidate_id)