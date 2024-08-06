from abc import ABC
from typing import Optional
from repositories.base import UserRepository
from users.models import User
from users.schemas import UserCreate, UserUpdate


class InMemoryUserRepository(UserRepository, ABC):
    def __init__(self):
        self.users = {}
        self.counter = 1

    async def create(self, user_create: UserCreate) -> User:
        user = User(id=self.counter, name=user_create["name"])
        self.users[self.counter] = user
        self.counter += 1
        return user

    async def get(self, user_id: int) -> Optional[User]:
        return self.users.get(user_id)

    async def update(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        if user_id in self.users:
            user = self.users[user_id]
            user.name = user_update["name"]
            self.users[user_id] = user
            return user
        return None

    async def delete(self, user_id: int) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
