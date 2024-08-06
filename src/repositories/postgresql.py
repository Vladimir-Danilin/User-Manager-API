import asyncpg
from abc import ABC
from typing import Optional
from repositories.base import UserRepository
from users.models import User
from users.schemas import UserCreate, UserUpdate


class PostgreUserRepository(UserRepository, ABC):
    def __init__(self, host: str, port: str, database: str, user: str, password: str):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password

    async def create(self, user_create: UserCreate) -> User:
        async with asyncpg.create_pool(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
        ) as pool:
            async with pool.acquire() as conn:
                result = await conn.fetchval("INSERT INTO users (name) VALUES ($1) RETURNING id", user_create["name"])
                return user_create if result else None

    async def get(self, user_id: int) -> Optional[User]:
        async with asyncpg.create_pool(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
        ) as pool:
            async with pool.acquire() as conn:
                result = await conn.fetchrow("SELECT * FROM users WHERE id = $1", user_id)
                return {"id": result["id"], "name": result["name"]} if result else None

    async def update(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        async with asyncpg.create_pool(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
        ) as pool:
            async with pool.acquire() as conn:
                result = await conn.execute("UPDATE users SET name = $1 WHERE id = $2", user_update["name"], user_id)
                return user_update if result == "UPDATE 1" else None

    async def delete(self, user_id: int) -> bool:
        async with asyncpg.create_pool(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
        ) as pool:
            async with pool.acquire() as conn:
                result = await conn.execute("DELETE FROM users WHERE id = $1", user_id)
                return result == "DELETE 1"
