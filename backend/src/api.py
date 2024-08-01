from fastapi import APIRouter
from src.auth.router import auth_router
from src.core.router import core_router
from src.registration.router import registration_router

api_router = APIRouter()

api_router.include_router(core_router)
api_router.include_router(registration_router)
api_router.include_router(auth_router)
