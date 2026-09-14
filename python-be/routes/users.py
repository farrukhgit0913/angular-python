from fastapi import APIRouter, HTTPException

from models.user import User
from data.users import users


router = APIRouter()


# --------------------------------------------------
# GET ALL USERS
# GET /users
# --------------------------------------------------

@router.get("/")
def get_users():
    return users


# --------------------------------------------------
# GET SINGLE USER
# GET /users/{user_id}
# --------------------------------------------------

@router.get("/{user_id}")
def get_user(user_id: int):

    user = next(
        (
            user
            for user in users
            if user["id"] == user_id
        ),
        None,
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    return user


# --------------------------------------------------
# CREATE USER
# POST /users
# --------------------------------------------------

@router.post("/", status_code=201)
def create_user(user: User):

    new_id = max(
        (
            user["id"]
            for user in users
        ),
        default=0,
    ) + 1

    new_user = {
        "id": new_id,
        **user.model_dump(),
    }

    users.append(new_user)

    return new_user


# --------------------------------------------------
# UPDATE USER
# PUT /users/{user_id}
# --------------------------------------------------

@router.put("/{user_id}")
def update_user(
    user_id: int,
    user: User,
):

    existing_user = next(
        (
            existing_user
            for existing_user in users
            if existing_user["id"] == user_id
        ),
        None,
    )

    if existing_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    existing_user["name"] = user.name
    existing_user["email"] = user.email

    return existing_user


# --------------------------------------------------
# DELETE USER
# DELETE /users/{user_id}
# --------------------------------------------------

@router.delete("/{user_id}")
def delete_user(user_id: int):

    user_index = next(
        (
            index
            for index, user in enumerate(users)
            if user["id"] == user_id
        ),
        None,
    )

    if user_index is None:
        raise HTTPException(
            status_code=404,
            detail="User not found",
        )

    deleted_user = users.pop(user_index)

    return {
        "message": "User deleted successfully",
        "user": deleted_user,
    }