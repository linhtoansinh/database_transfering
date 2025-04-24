from fastapi import FastAPI

from backend.apis.connector_api import router as connector_router

app = FastAPI()

app.include_router(connector_router)