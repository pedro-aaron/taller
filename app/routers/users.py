#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter
from .users_repository import UsersRepository
from .users_esquemas import RequestCreateUser, ResponseCreateUser
from ..common.log import configure_logging
import logging

logger = logging.getLogger(__name__)
# configure_logging("bitacora.log")


router = APIRouter(prefix="/users")


@router.post("/", tags=["users"], response_model=ResponseCreateUser)
async def create_user(user_data: RequestCreateUser):
    logger.info("start endpoint >> create_user")
    logger.info(f"--user_data -> {user_data.dict()}")
    repository = UsersRepository()
    await repository.configure()
    data = await repository.create_user(user_data.dict())
    logger.info(f"end endpoint create_user result -> {data['_id']}")
    return data


# @router.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "Rick"}, {"username": "Morty"}]


# @router.get("/users/me", tags=["users"])
# async def read_user_me():
#     return {"username": "fakecurrentuser"}


# @router.get("/users/{username}", tags=["users"])
# async def read_user(username: str):
#     return {"username": username}
