from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return "server is up and running"