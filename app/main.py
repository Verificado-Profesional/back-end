from fastapi import FastAPI
from .routers import dashboard

app = FastAPI()

app.include_router(dashboard.router)

@app.get("/")
def root():
    return {"message": "Hola, Verificados!"} 


@app.get("/dashboard")
def dashboard():
    return {"message": "Hola, Verificados!"} 
