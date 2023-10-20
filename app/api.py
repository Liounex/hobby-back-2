from fastapi import FastAPI

app = FastAPI()


@app.get('/', tags=["home"])
async def hello():
    return {"message": "Hello World"}