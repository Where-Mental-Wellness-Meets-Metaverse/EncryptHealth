from fastapi import FastAPI, HTTPException
from src.routes import encryption, practitioner

app = FastAPI()

# ✅ Mount routes
app.include_router(encryption.router)
app.include_router(practitioner.router)

