from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def index():
    return "server is up and running"

@app.get('/greet/{name}')
async def greet(name):
    return f"Hi {name}"

@app.get('/feature2')
async def feature2():
    return "Feature 2"