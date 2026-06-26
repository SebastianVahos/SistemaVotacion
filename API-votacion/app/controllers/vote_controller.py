from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.vote_schema import VoteCreate, VoteResponse, VoteStatisticsResponse
from app.services.vote_service import VoteService

router = APIRouter(
    prefix="/votes",
    tags=["Votes"]
)

service = VoteService()


@router.post(
    "",
    response_model=VoteResponse,
    status_code=201
)
def create_vote(
    vote: VoteCreate,
    db: Session = Depends(get_db)
):
    return service.create(db, vote)


@router.get(
    "",
    response_model=list[VoteResponse]
)
def get_votes(
    db: Session = Depends(get_db)
):
    return service.get_all(db)

@router.get(
    "/statistics",
    response_model=VoteStatisticsResponse
)
def get_statistics(
    db: Session = Depends(get_db)
):
    return service.get_statistics(db)