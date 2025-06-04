# src/backend/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="EncryptHealth Backend API",
    description="API for encrypted health data management and practitioner workflows",
    version="0.1.0"
)

# Example data storage (in-memory)
practitioners = []

# Pydantic model for Practitioner
class Practitioner(BaseModel):
    id: int
    name: str
    email: str
    specialty: str

@app.get("/")
async def root():
    return {"message": "Welcome to EncryptHealth API"}

@app.get("/practitioners", response_model=List[Practitioner])
async def get_practitioners():
    return practitioners

@app.post("/practitioners", response_model=Practitioner, status_code=201)
async def add_practitioner(practitioner: Practitioner):
    # Simple check to avoid duplicate IDs
    if any(p.id == practitioner.id for p in practitioners):
        raise HTTPException(status_code=400, detail="Practitioner ID already exists")
    practitioners.append(practitioner)
    return practitioner

@app.get("/practitioners/{practitioner_id}", response_model=Practitioner)
async def get_practitioner(practitioner_id: int):
    for p in practitioners:
        if p.id == practitioner_id:
            return p
    raise HTTPException(status_code=404, detail="Practitioner not found")
