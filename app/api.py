from fastapi import FastAPI

app = FastAPI()


@app.get('/', tags=["home"])
async def hello():
    return {"message": "Hello World"}


@app.get('/api', tags=["data"])
async def prueba():
    return {"message": "Hello World"}
