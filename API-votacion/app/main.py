from fastapi import FastAPI
from app.controllers.voter_controller import router as voter_router
from app.controllers.candidate_controller import router as candidate_router
from app.controllers.vote_controller import router as vote_router

app = FastAPI(
    title="Sistema de Votación API",
    version="1.0"
)

app.include_router(voter_router)
app.include_router(candidate_router)
app.include_router(vote_router)