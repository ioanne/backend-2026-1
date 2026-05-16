from pydantic import BaseModel
from typing import Optional


# REQUEST
class UsuarioCreateRequest(BaseModel):
    nombre: Optional[str] = None
    email: str


"""
    {"nombre": "Juan", "email": "juan@gmail.com"}
"""

class AlumnoCreateRequest(BaseModel):
    carrera: Optional[str] = None
    usuario_id: int

"""
    {"carrera": "TSDS", "usuario_id": 1}
"""

# RESPONSE
class UsuarioResponse(BaseModel):
    id: int
    nombre: Optional[str]
    email: str

    class Config:
        orm_mode = True


class AlumnoResponse(BaseModel):
    id: int
    carrera: Optional[str]
    usuario: UsuarioResponse
    class Config:
        orm_mode = True
