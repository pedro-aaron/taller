from fastapi import APIRouter

router = APIRouter()


@router.post("/users/", tags=["users"])
async def create_user():
    data_user_created = {"_id": "aksaskjdhfg", "name": "John", "age": 30}
    return data_user_created


# @router.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]


# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}


# @router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}
