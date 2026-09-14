from fastapi import APIRouter, HTTPException

from app.schemas.user import User
from data.users import users

router = APIRouter()


@router.get("/")
def get_users():
    return users


@router.get("/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(status_code=404, detail="User not found")


@router.post("/", status_code=201)
def create_user(user: User):
    new_id = max((item["id"] for item in users), default=0) + 1

    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email,
    }

    users.append(new_user)

    return new_user


@router.put("/{user_id}")
def update_user(user_id: int, user: User):
    for item in users:
        if item["id"] == user_id:
            item["name"] = user.name
            item["email"] = user.email

            return item

    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)

            return {
                "message": "User deleted successfully",
                "user": deleted_user,
            }

    raise HTTPException(status_code=404, detail="User not found")