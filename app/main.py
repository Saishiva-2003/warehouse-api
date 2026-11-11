# Starting point of the API. Run with:  uvicorn app.main:app --reload
from fastapi import FastAPI

app = FastAPI(title="Warehouse API")


@app.get("/")
def home():
    return {"message": "Warehouse API is running"}
