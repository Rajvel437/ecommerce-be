from fastapi import FastAPI
from app.routes.api.v1.endpoints import user


app = FastAPI()

app.include_router(user.router, prefix="/api/v1/users", tags=["users"])


@app.get("/")
async def home():
    return {"msg":"App is running successfully"}


