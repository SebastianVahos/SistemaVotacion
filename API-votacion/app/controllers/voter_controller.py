from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.voter_schema import VoterCreate, VoterResponse
from app.services.voter_service import VoterService

router = APIRouter(
    prefix="/voters",
    tags=["Voters"],
)

service = VoterService()

@router.post(
    "",
    response_model = VoterResponse,
    status_code = 201,
)
def create_voter(
    voter: VoterCreate, 
    db: Session = Depends(get_db)
):
    return service.create(db, voter)

@router.get(
    "",
    response_model = list[VoterResponse]
)
def get_voters(
    db: Session = Depends(get_db)
):
    return service.get_all(db)

@router.get(
    "/{voter_id}", 
    response_model = VoterResponse
)
def get_voter(
    voter_id: int,
    db: Session = Depends(get_db)
):
    return service.get_by_id(db, voter_id)

@router.delete(
    "/{voter_id}",
)
def delete_voter(
    voter_id: int,
    db: Session = Depends(get_db)
):
    service.delete(db, voter_id)

    return {
        "message": "Votante eliminado correctamente."
    }