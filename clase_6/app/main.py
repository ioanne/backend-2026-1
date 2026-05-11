from fastapi import FastAPI
from routers import usuarios, alumnos

app = FastAPI()

# @app.get('/')
# async def home():
#     return "Hola amigos jeje!"


app.include_router(usuarios.router, prefix='/usuarios')
app.include_router(alumnos.router, prefix='/alumnos')

@app.get('/hola-enemigos')
async def home2():
    return "Hola enemigos!"