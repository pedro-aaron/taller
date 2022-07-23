#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import APIRouter
from .users_repository import UsersRepository
from ..common.log import configure_logging
import logging

logger = logging.getLogger(__name__)
# configure_logging("bitacora.log")


router = APIRouter(prefix="/users")


@router.post("/", tags=["users"])
async def create_user():
    logger.info("start endpoint >> create_user")
    data_user_dummy = {"name": "pedro tres", "age": 30}
    repository = UsersRepository()
    await repository.configure()
    id = await repository.create_user(data_user_dummy)
    logger.info(f"end endpoint create_user result -> {id}")
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
