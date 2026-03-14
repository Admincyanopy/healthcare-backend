from fastapi import FastAPI
from app.routes import auth_routes

from app.database import engine, Base
from app.models import user_model


app = FastAPI(title="Healthcare Backend API")


# Create database tables
Base.metadata.create_all(bind=engine)


# Register auth routes
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])


@app.get("/")
def home():
    return {"message": "Healthcare Backend Running"}