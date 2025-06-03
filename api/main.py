# api/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router

app = FastAPI(
    title="SeAQuEn API",
    description="Self-Adaptive Quantization Engine for LLM inference",
    version="1.0.0"
)

app.add_middleware( # allow this for testing purposes
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(router)
