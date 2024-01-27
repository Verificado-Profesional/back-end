from fastapi import APIRouter
from app.controllers.dashboard import DashboardController


router = APIRouter()


@router.get("/dashboard/", tags=["dashboard"])
async def get_dashboard():
    return DashboardController.get()
