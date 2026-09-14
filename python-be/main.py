from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.users import router as users_router

app = FastAPI()


# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# Root
# --------------------------------------------------

@app.get("/")
def home():
    return {
        "message": "Python REST API is running successfully! 🚀",
        "status": "OK",
        "api": "FastAPI",
        "version": "1.0.0",
    }


# --------------------------------------------------
# Health
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "message": "API is healthy",
        "status": "OK",
    }


# --------------------------------------------------
# Users Routes
# --------------------------------------------------

app.include_router(
    users_router,
    prefix="/users",
    tags=["Users"],
)