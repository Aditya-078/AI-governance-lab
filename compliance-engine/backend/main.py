
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.upload import router as upload_router
from app.routers.health import router as health_router
from app.routers.analysis import router as analysis_router

app = FastAPI(
    title="Compliance Engine API",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(analysis_router)

#$ python -m uvicorn main:app --reload --port 8000 TOO RUN BACKEND