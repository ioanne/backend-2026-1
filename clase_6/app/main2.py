from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def home():
    return "hello friends!"


@app.get('/suckers')
async def home2():
    return "Hola suckers"