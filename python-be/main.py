from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr

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
        "version": "1.0.0"
    }


# --------------------------------------------------
# Health
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "message": "API is healthy",
        "status": "OK"
    }


# --------------------------------------------------
# Model
# --------------------------------------------------

class User(BaseModel):
    name: str
    email: EmailStr


# --------------------------------------------------
# Temporary in-memory database
# --------------------------------------------------

users = [
    {
        "id": 1,
        "name": "Farrukh Shahzad",
        "email": "farrukh@example.com"
    },
    {
        "id": 2,
        "name": "Ali Khan",
        "email": "ali@example.com"
    },
    {
        "id": 3,
        "name": "Ahmed Raza",
        "email": "ahmed@example.com"
    },
]


# --------------------------------------------------
# GET ALL USERS
# --------------------------------------------------

@app.get("/users")
def get_users():
    return users


# --------------------------------------------------
# GET SINGLE USER
# --------------------------------------------------

@app.get("/users/{user_id}")
def get_user(user_id: int):

    user = next(
        (user for user in users if user["id"] == user_id),
        None
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# --------------------------------------------------
# CREATE USER
# --------------------------------------------------

@app.post("/users", status_code=201)
def create_user(user: User):

    new_id = max(
        (user["id"] for user in users),
        default=0
    ) + 1

    new_user = {
        "id": new_id,
        **user.model_dump()
    }

    users.append(new_user)

    return new_user


# --------------------------------------------------
# UPDATE USER
# --------------------------------------------------

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):

    existing_user = next(
        (user_item for user_item in users if user_item["id"] == user_id),
        None
    )

    if existing_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    existing_user["name"] = user.name
    existing_user["email"] = user.email

    return existing_user


# --------------------------------------------------
# DELETE USER
# --------------------------------------------------

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    user_index = next(
        (
            index
            for index, user in enumerate(users)
            if user["id"] == user_id
        ),
        None
    )

    if user_index is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    deleted_user = users.pop(user_index)

    return {
        "message": "User deleted successfully",
        "user": deleted_user
    }