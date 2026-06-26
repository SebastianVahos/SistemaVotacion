from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.candidate_schema import CandidateCreate, CandidateResponse
from app.services.candidate_service import CandidateService

router = APIRouter(
    prefix="/candidates",
    tags=["Candidates"],
)

service = CandidateService()

@router.post(
    "",
    response_model = CandidateResponse,
    status_code = 201,
)
def create_candidate(
    candidate: CandidateCreate, 
    db: Session = Depends(get_db)
):
    return service.create(db, candidate)

@router.get(
    "",
    response_model = list[CandidateResponse]
)
def get_candidates(
    db: Session = Depends(get_db)
):
    return service.get_all(db)

@router.get(
    "/{candidate_id}",
    response_model = CandidateResponse
)
def get_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):
    return service.get_by_id(db, candidate_id)

@router.delete(
    "/{candidate_id}",
)
def delete_candidate(
    candidate_id: int,
    db: Session = Depends(get_db)
):
    service.delete(db, candidate_id)

    return {
        "message": "Candidato eliminado correctamente."
    }