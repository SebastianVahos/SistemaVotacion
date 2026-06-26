# El repository es la capa que habla con la base de datos, es decir, es la capa que se encarga de hacer 
# las consultas a la base de datos y devolver los resultados a la capa de servicios.

from sqlalchemy.orm import Session
from app.models.voter import Voter
from app.schemas.voter_schema import VoterCreate

class VoterRepository:
    
    def create(self, db: Session, voter: VoterCreate):
        
        new_voter = Voter(
            name = voter.name,
            email = voter.email,
        )

        db.add(new_voter)
        db.commit()
        db.refresh(new_voter)

        return new_voter
    
    def get_by_email(self, db: Session, email: str):

        return (
            db.query(Voter)
            .filter(Voter.email == email)
            .first()
        )

    # def get_all(self, db: Session):
    #     return db.query(Voter).all()
    
    def get_by_id(self, db: Session, voter_id: int):
        return( 
            db.query(Voter)
            .filter(Voter.id == voter_id)
            .first()
        )
    
    def delete(self, db: Session, voter_id: int):
        voter = self.get_by_id(db, voter_id)
        if voter:
            db.delete(voter)
            db.commit()
        return voter


    # EXTRAS PAGINACION Y FILTRADO
    def get_all_filter(
        self,
        db: Session,
        name: str = None,
        skip: int = 0,
        limit: int = 10
    ):

        query = db.query(Voter)

        # Filtrar por nombre
        if name:
            query = query.filter(
                Voter.name.ilike(f"%{name}%")
            )

        # Paginación
        return (
            query
            .offset(skip)
            .limit(limit)
            .all()
        )