import os
from dotenv import load_dotenv

load_dotenv()

REPOSITORY_TYPE = os.environ.get("REPOSITORY_TYPE")

if REPOSITORY_TYPE == "POSTGRE":
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
elif REPOSITORY_TYPE == "REDIS":
    REDIS_HOST = os.environ.get("REDIS_HOST")
    REDIS_PORT = os.environ.get("REDIS_PORT")
elif REPOSITORY_TYPE == "IN_MEMORY":
    pass
else:
    raise ValueError("Недопустимый тип репозитория")
