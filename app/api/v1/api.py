
from fastapi import APIRouter
from .router import employees_router
router = APIRouter()

router.include_router(employees_router.router,prefix="/employees", tags=["employees"])

