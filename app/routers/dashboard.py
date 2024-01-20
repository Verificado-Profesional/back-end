from fastapi import APIRouter
from app.controllers.dashboard import DashboardController


router = APIRouter()


@router.get("/", tags=["dashboard"])
async def get_dashboard():
    return DashboardController.get()
