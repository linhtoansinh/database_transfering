from fastapi import APIRouter, HTTPException, status

from backend.models.connector import Connector
from backend.repositories.source_repository import SourceRepository
from backend.services.source_service import SourceService

router = APIRouter(tags=["source-connectors"], prefix="/source-connectors")

sourceService = SourceService()

@router.post("/")
async def createSource(connector: Connector) -> Connector:
    try:
        return sourceService.create(connector)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))