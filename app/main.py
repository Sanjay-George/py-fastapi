from fastapi import FastAPI
from app.libs.controllers import api

app = FastAPI()
app.include_router(api.router, prefix="/api")


@app.get("/")
def root():
    return {"message": "AI App running"}
