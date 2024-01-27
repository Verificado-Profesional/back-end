from fastapi import FastAPI
import uvicorn
from .routers import dashboard

app = FastAPI()
app.include_router(dashboard.router)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


@app.get("/")
def root():
    return {"message": "Hola, Verificados!"}
