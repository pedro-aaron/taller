#!/usr/bin/env python
# -*- coding: utf-8 -*-

import motor.motor_asyncio
from .singleton import SingletonMeta


class UsersRepository(metaclass=SingletonMeta):
    def __init__(self):
        self.client = None
        self.db = None
        self.collection = None

    def is_configured(self):
        return (
            self.client is not None
            and self.db is not None
            and self.collection is not None
        )

    async def configure(self):
        if not self.is_configured():
            conn_str = "mongodb+srv://pedro:pedro@cluster0.whl1sxe.mongodb.net/?retryWrites=true&w=majority"
            # set a 5-second connection timeout
            self.client = motor.motor_asyncio.AsyncIOMotorClient(
                conn_str, serverSelectionTimeoutMS=5000
            )

            try:
                print(await self.client.server_info())
            except Exception:
                print("Unable to connect to the server.")

            self.db = self.client.users
            self.collection = self.db.users
            print("UsersRepository configured")
        else:
            print("UsersRepository already configured")

    async def create_user(self, data):
        result = await self.collection.insert_one(data)
        print(f"create_user result -> {result.inserted_id}")
        return result.inserted_id
