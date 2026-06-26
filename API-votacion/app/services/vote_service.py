from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.vote_repository import VoteRepository
from app.repositories.voter_repository import VoterRepository
from app.repositories.candidate_repository import CandidateRepository

from app.schemas.vote_schema import VoteCreate

vote_repository = VoteRepository()
voter_repository = VoterRepository()
candidate_repository = CandidateRepository()


class VoteService:

    def create(self, db: Session, vote: VoteCreate):

        voter = voter_repository.get_by_id(db, vote.voter_id)

        if not voter:
            raise HTTPException(
                status_code = 404,
                detail = "El votante no existe."
            )

        if voter.has_voted:
            raise HTTPException(
                status_code = 409,
                detail = "El votante ya emitió su voto."
            )

        candidate = candidate_repository.get_by_id(
            db,
            vote.candidate_id
        )

        if not candidate:
            raise HTTPException(
                status_code = 404,
                detail = "El candidato no existe."
            )

        voter.has_voted = True

        return vote_repository.create(db, vote)


    def get_all(self, db: Session):

        vote = vote_repository.get_all(db)
        if not vote:
            raise HTTPException(
                status_code = 404,
                detail = "No hay votos registrados."
            )

        return vote
        
    def get_statistics(self, db: Session):

        total_votes = vote_repository.get_total_votes(db)

        if total_votes == 0:
            raise HTTPException(
                status_code = 404,
                detail = "Aún no se han emitido votos, no hay estadísticas disponibles."
            )

        total_voters_voted = vote_repository.get_total_voters_voted(db)

        candidates = vote_repository.get_votes_by_candidate(db)

        if not candidates:
            raise HTTPException(
                status_code=404,
                detail="No hay candidatos registrados."
            )

        statistics = []

        for candidate in candidates:

            percentage = 0

            if total_votes > 0:
                percentage = round(
                    (candidate.votes / total_votes) * 100,
                    2
                )

            statistics.append(
                {
                    "candidate_id": candidate.id,
                    "candidate_name": candidate.name,
                    "votes": candidate.votes,
                    "percentage": percentage
                }
            )

        return {
            "total_votes": total_votes,
            "total_voters_voted": total_voters_voted,
            "statistics": statistics
        }