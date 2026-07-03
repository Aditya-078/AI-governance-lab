from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.health import router as health_router

app = FastAPI(
    title="Compliance Engine API"
)

app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:3000"],   # If using Create React App
    allow_origins=["http://localhost:5173"], # If using Vite
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)