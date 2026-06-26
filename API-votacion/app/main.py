from fastapi import FastAPI
from app.controllers.voter_controller import router as voter_router

app = FastAPI(
    title="Sistema de Votación API",
    version="1.0"
)

app.include_router(voter_router)