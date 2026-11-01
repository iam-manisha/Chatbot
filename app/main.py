from fastapi import FastAPI
from app.routes.health import router as health_router

app = FastAPI(title="Live Chat Support System")


@app.get("/")
def home():
    return {"message": "Welcome to Live Chat Support System!"}


app.include_router(health_router, prefix="/api/v1")