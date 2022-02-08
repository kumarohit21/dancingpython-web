
from fastapi import APIRouter
from .v1.api import router
api_router = APIRouter()


router.include_router(router,prefix="/v1")

