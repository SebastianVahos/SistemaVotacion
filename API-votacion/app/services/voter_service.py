from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.voter_repository import VoterRepository
from app.schemas.voter_schema import VoterCreate
from app.repositories.candidate_repository import CandidateRepository

voter_repository = VoterRepository()
candidate_repository = CandidateRepository()

class VoterService:

    def create(self, db: Session, voter: VoterCreate):

        existing_voter = voter_repository.get_by_email(
            db,
            voter.email
        )

        if existing_voter:
            raise HTTPException(
                status_code = 409,
                detail = "Ya existe un votante con ese correo."
            )

        existing_candidate = candidate_repository.get_by_email(
            db,
            voter.email
        )

        if existing_candidate:
            raise HTTPException(
                status_code = 409,
                detail = "Ese correo pertenece a un candidato."
            )

        return voter_repository.create(db, voter)

    def get_all(self, db: Session):
        voter = voter_repository.get_all(db)
        if not voter:
            raise HTTPException(
                status_code = 404,
                detail = "No hay votantes registrados."
            )

        return voter

    def get_by_id(self, db: Session, voter_id: int):
        voter = voter_repository.get_by_id(db, voter_id)

        if voter is None:
            raise HTTPException(
                status_code = 404,
                detail = "Votante no encontrado."
            )

        return voter

    def delete(self, db: Session, voter_id: int):
        # Primero, verificamos si el votante existe antes de intentar eliminarlo. Si no existe, devolvemos None.
        voter = voter_repository.get_by_id(db, voter_id)
    
        if voter is None:
            raise HTTPException(
                status_code = 404,
                detail = "Votante no encontrado."
            )
        
        return voter_repository.delete(db, voter_id)