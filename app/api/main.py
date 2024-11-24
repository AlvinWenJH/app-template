from fastapi import FastAPI
from .routers import testAPI

app = FastAPI()
app.include_router(testAPI.router)


@app.get("/")
def root():
    return {"message": "This is TEST API"}
