from pydantic import BaseModel

class VoteCreate(BaseModel):
    voter_id: int
    candidate_id: int


class VoteResponse(BaseModel):
    id: int
    voter_id: int
    candidate_id: int

    class Config:
        from_attributes = True

class CandidateStatistics(BaseModel):
    candidate_id: int
    candidate_name: str
    votes: int
    percentage: float


class VoteStatisticsResponse(BaseModel):
    total_votes: int
    total_voters_voted: int
    statistics: list[CandidateStatistics]