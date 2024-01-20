from fastapi import HTTPException

class DashboardController:
    @staticmethod
    def get():
        return "pong"