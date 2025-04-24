from fastapi import APIRouter, HTTPException, status

from backend.models.source_connector import SourceConnector
from backend.requests.source_connector_create import SourceConnectorCreate
from backend.services.source_service import SourceService

router = APIRouter(tags=["source-connectors"], prefix="/source-connectors")

sourceService = SourceService()

@router.post("/")
async def createSource(connector: SourceConnectorCreate) -> SourceConnector:
    try:
        return sourceService.create(connector)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))