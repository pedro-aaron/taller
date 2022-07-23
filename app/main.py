#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastapi import Depends, FastAPI
from .routers import users
from .common.log import configure_logging
import logging

logger = logging.getLogger(__name__)
configure_logging("bitacora.log")

logger.info("---------------Starting API------------------")

app = FastAPI()

# URL/users
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "API del Taller"}
