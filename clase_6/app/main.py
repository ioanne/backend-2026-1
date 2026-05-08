from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def home():
    return "Hola amigos jeje!"

@app.get('/hola-enemigos')
async def home2():
    return "Hola enemigos!"