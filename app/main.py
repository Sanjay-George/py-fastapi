from fastapi import FastAPI
from app.endpoints import api

app = FastAPI()
app.include_router(api.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "AI App running"}
