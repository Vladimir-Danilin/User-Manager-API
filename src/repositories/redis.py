import redis
from abc import ABC
from typing import Optional
from repositories.base import UserRepository
from users.models import User
from users.schemas import UserCreate, UserUpdate


class RedisUserRepository(UserRepository, ABC):
    def __init__(self, host: str, port: int):
        self.client = redis.Redis(host=host, port=port)

    async def create(self, user_create: UserCreate) -> User:
        user_id = self.client.incr("user_id_counter")
        user = User(id=user_id, name=user_create["name"])
        self.client.set(f"user:{user_id}", user.json())
        print(user)
        return user

    async def get(self, user_id: int) -> Optional[User]:
        user_data = self.client.get(f"user:{user_id}")
        if user_data:
            return User.model_validate_json(user_data)
        return None

    async def update(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        user_data = self.client.get(f"user:{user_id}")
        if user_data:
            user = User.model_validate_json(user_data)
            user.name = user_update["name"]
            self.client.set(f"user:{user_id}", user.json())
            return user
        return None

    async def delete(self, user_id: int) -> bool:
        return self.client.delete(f"user:{user_id}") == 1
