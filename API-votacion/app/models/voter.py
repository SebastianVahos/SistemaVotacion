# como ya tengo el modelo de Voter en bd, puedo mapearlo con SQLAlchemy para poder hacer consultas y operaciones en la base de datos de manera más sencilla

# Vamos a decirle a SQLAlchemy que esta clase es un modelo de base de datos y que se corresponde con la tabla "voters" en la base de datos
from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

# El Base es la clase base de SQLAlchemy que nos permite definir modelos de base de datos. Al heredar de esta clase, 
# nuestra clase Voter se convierte en un modelo de base de datos y podemos usarla para realizar consultas y operaciones 
# en la tabla "voter" de la base de datos.
class Voter(Base):
    __tablename__ = "voter"

    id = Column(Integer, primary_key = True, index = True) # Index es para que la columna sea indexada y se pueda buscar más rápido
    name = Column(String(80), nullable = False)
    email = Column(String(50), unique = True, nullable = False)
    has_voted = Column(Boolean, default = False)
