import users.models as models
import users.schemas as schemas
from fastapi import APIRouter, Request

router = APIRouter(prefix="/users", tags=["users"])


@router.post("")
async def create_user(request: Request, user: schemas.UserCreate):
    return await request.app.state.repo.create(user.model_dump())


@router.get("/{user_id}", response_model=models.User)
async def read_user(request: Request, user_id: int = 0):
    return await request.app.state.repo.get(user_id)


@router.put("/{user_id}")
async def update_user(request: Request, user_id: int, user: schemas.UserUpdate):
    return await request.app.state.repo.update(user_id, user.model_dump())


@router.delete("/{user_id}")
async def delete_user(request: Request, user_id: int):
    return await request.app.state.repo.delete(user_id)
