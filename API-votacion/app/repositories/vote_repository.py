from sqlalchemy.orm import Session

from app.models.vote import Vote
from app.schemas.vote_schema import VoteCreate
from app.models.voter import Voter
from app.models.candidate import Candidate


class VoteRepository:

    def create(self, db: Session, vote: VoteCreate):

        new_vote = Vote(
            voter_id=vote.voter_id,
            candidate_id=vote.candidate_id
        )

        db.add(new_vote)
        db.commit()
        db.refresh(new_vote)

        return new_vote


    def get_all(self, db: Session):
        return db.query(Vote).all()
    
    def get_total_votes(self, db: Session):
        return db.query(Vote).count()

    def get_total_voters_voted(self, db: Session):
        return (
            db.query(Voter)
            .filter(Voter.has_voted == True)
            .count()
        )

    def get_votes_by_candidate(self, db: Session):
        return (
            db.query(
                Candidate.id,
                Candidate.name,
                Candidate.votes
            )
            .all()
        )
    
    