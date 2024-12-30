from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router, prefix="/api/v1", tags=["sharepoints"])

@app.get('/')
async def CheckApplication():
    return {"message": "Application is running"}  # Return a message to the client