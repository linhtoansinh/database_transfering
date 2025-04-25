import json
from fastapi import APIRouter, HTTPException, Response, status

from backend.enums.connector_actions import ConnectorAction
from backend.models.connector import Connector
from backend.services.connector_service import ConnectorService

router = APIRouter(tags=["connectors"], prefix="/connectors")

connectorService = ConnectorService()

@router.post("/")
async def createConnector(connector: Connector) -> Connector:
    try:
        return connectorService.create(connector)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.put("/")
async def createOrUpdateConnector(connector: Connector) -> Connector:
    try:
        return connectorService.upsert(connector)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
    
@router.delete("/{connector_name}")
async def deleteConnector(connector_name: str):
    try:
        connectorService.delete(connector_name=connector_name)

        return Response(
            content=json.dumps({"name": connector_name}),
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.post("/{connector_name}/stop")
async def stopConnector(connector_name: str):
    try:
        connectorService.execute_kafka_connector_action(ConnectorAction.stop, connector_name=connector_name)

        return Response(
            content=json.dumps({"name": connector_name}),
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.post("/{connector_name}/restart")
async def restartConnector(connector_name: str):
    try:
        connectorService.execute_kafka_connector_action(ConnectorAction.restart, connector_name=connector_name)

        return Response(
            content=json.dumps({"name": connector_name}),
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    
@router.post("/{connector_name}/resume")
async def resumeConnector(connector_name: str):
    try:
        connectorService.execute_kafka_connector_action(ConnectorAction.resume, connector_name=connector_name)

        return Response(
            content=json.dumps({"name": connector_name}),
            status_code=status.HTTP_200_OK,
            media_type="application/json",
        )

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))