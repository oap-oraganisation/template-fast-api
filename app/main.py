from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI(title="template-fast-api", version="1.0.0")


class HealthResponse(BaseModel):
    status: str


class NameResponse(BaseModel):
    name: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@app.get("/api/v1/name", response_model=NameResponse)
def get_name(name: str = Query(..., min_length=1)) -> NameResponse:
    return NameResponse(name=name)
