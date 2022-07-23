from fastapi import APIRouter
from .users_repository import UsersRepository


router = APIRouter(prefix="/users")


@router.post("/", tags=["users"])
async def create_user():
    data_user_dummy = {"name": "pedro tres", "age": 30}
    repository = UsersRepository()
    await repository.configure()
    id = await repository.create_user(data_user_dummy)
    return {"id": str(id)}


# @router.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]


# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}


# @router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}
