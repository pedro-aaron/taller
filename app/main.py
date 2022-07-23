#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import Depends, FastAPI
from .routers import users

app = FastAPI()

# URL/users
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "API del Taller"}
