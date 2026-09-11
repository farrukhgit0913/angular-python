from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root / API status
@app.get("/")
def home():
    return {
        "message": "Python REST API is running successfully! 🚀",
        "status": "OK",
        "api": "FastAPI",
        "version": "1.0.0"
    }


# Health check
@app.get("/health")
def health_check():
    return {
        "message": "API is healthy",
        "status": "OK"
    }


# Data model
class User(BaseModel):
    name: str
    email: str


# Temporary in-memory database
users = [
    {"id": 1, "name": "Farrukh Shahzad", "email": "farrukh@example.com"},
    {"id": 2, "name": "Ali Khan", "email": "ali@example.com"},
    {"id": 3, "name": "Ahmed Raza", "email": "ahmed@example.com"},
]

# GET all users
@app.get("/users")
def get_users():
    return users


# GET single user
@app.get("/users/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return users[user_id]


# POST - Create user
@app.post("/users", status_code=201)
def create_user(user: User):
    user_id = len(users) + 1

    users[user_id] = user.model_dump()

    return {
        "id": user_id,
        **users[user_id]
    }


# PUT - Update user
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    users[user_id] = user.model_dump()

    return {
        "id": user_id,
        **users[user_id]
    }


# DELETE user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    del users[user_id]

    return {
        "message": "User deleted successfully"
    }