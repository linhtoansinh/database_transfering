from typing import TypeVar, Type, Optional
from pydantic import BaseModel
from backend.database import db
from pymongo.collection import Collection

T = TypeVar('T', bound=BaseModel)

class BaseRepository:
    model: Type[T]
    collection: Collection

    def __init__(self, collection_name: str, model: Type[T]):
        
        self.collection = db[collection_name]
        self.model = model

    def create(self, document:dict) -> str:
        try: 
            result = self.collection.insert_one(document)
            return result.inserted_id
        except Exception:
            raise

    def update(self, id: str, document: dict) -> str:
        try:
            result = self.collection.update_one({"_id": id}, {"$set": document})
            return result.upserted_id
        except Exception:
            raise

    def get_all(self) -> list[T]:
        try:
            records = self.collection.find()
            return [self.model.model_validate(record) for record in records]
        except Exception:
            raise

    def get(self, id: str) -> Optional[T]:
        try:
            record = self.collection.find_one({"_id": id})
            return self.model.model_validate(record) if record else None
        except Exception:
            raise

    def remove(self, id: str):
        try:
            self.collection.delete_one({"_id": id})
        except Exception:
            raise