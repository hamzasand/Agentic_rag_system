from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse

app = FastAPI()

@app.get("/test", response_class= JSONResponse)
def test_endpoint():
    return {"test1": 1, "test2": 2, "test3": 3}

@app.get("/welcome", response_class= PlainTextResponse)
def home():
    return 'Welcome'