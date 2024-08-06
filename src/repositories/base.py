from abc import ABC, abstractmethod
from typing import Optional, List
from users.models import User
from users.schemas import UserCreate, UserUpdate


class UserRepository(ABC):
    @abstractmethod
    def get(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def create(self, user_create: UserCreate) -> User:
        pass

    @abstractmethod
    def update(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass
