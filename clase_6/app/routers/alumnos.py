from fastapi import APIRouter

router = APIRouter()


@router.get('/{id}')
async def obtener_alumno(id: str, hola: str):
    print(id)
    alumno = None
    if id == "5":
        alumno = "Alejandro"
    return alumno + hola


@router.get('/all')
async def alumnos():
    return ["Alejandro", "Lucas"]
