from fastapi import APIRouter, Depends, Request, Response
from sqlalchemy.ext.asyncio import AsyncSession
from src.database.core import get_async_db

registration_router = APIRouter(tags=["Registration"])


@registration_router.get("/register")
async def register(
    request: Request,
    response: Response,
    db_session: AsyncSession = Depends(get_async_db),
):
    return "Registration Page"


@registration_router.post("/register/")
async def register_new_user(
    request: Request,
    response: Response,
    db_session: AsyncSession = Depends(get_async_db),
):
    return "Create new user in the database"
