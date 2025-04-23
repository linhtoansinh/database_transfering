from fastapi import FastAPI

from backend.apis.source_api import router as source_router

app = FastAPI()

app.include_router(source_router)