from fastapi import FastAPI
from contextlib import asynccontextmanager
import config
import users.router as user_router
from repositories.in_memory import InMemoryUserRepository
from repositories.postgresql import PostgreUserRepository
from repositories.redis import RedisUserRepository


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    if config.REPOSITORY_TYPE == "POSTGRE":
        repo = PostgreUserRepository(
            host=config.DB_HOST,
            port=config.DB_PORT,
            database=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASS,
        )
    elif config.REPOSITORY_TYPE == "REDIS":
        repo = RedisUserRepository(host=config.REDIS_HOST, port=config.REDIS_PORT)
    elif config.REPOSITORY_TYPE == "IN_MEMORY":
        repo = InMemoryUserRepository()
    app.state.repo = repo
    yield


app = FastAPI(lifespan=app_lifespan)

app.include_router(user_router.router)
