# El schema de votante define la estructura de los datos que se esperan para un votante en la aplicación de votación. 
# El schema se utiliza para validar y serializar los datos de entrada y salida en las operaciones relacionadas con los votantes.
from pydantic import BaseModel, EmailStr

# Cuando se hace post al votante, se espera que se envíe un objeto JSON con los campos "name" y "email". esos dos 
# ya que el id es autoincrementable y el has_voted esta por defecto en False
class VoterCreate(BaseModel):
    name: str
    email: EmailStr

# Cuando se hace get al votante, se espera que se devuelva un objeto JSON con los campos "id", "name", "email" y "has_voted".
class VoterResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    has_voted: bool

    #Cuando uses este modelo, sigue las siguientes reglas, y le dice, no es un diccionario, es un objeto 
    # que tiene atributos, y que se pueden acceder como atributos de la clase.
    class Config:
        from_attributes = True