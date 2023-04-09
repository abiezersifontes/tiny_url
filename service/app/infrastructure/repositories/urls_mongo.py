"""Mongo Class File"""
import asyncio
from datetime import datetime
from pymongo import MongoClient
from pymongo.results import DeleteResult
from service.settings import get_settings
from service.app.domain.repositories.store_repository import StoreRepository


class UrlsMongo(StoreRepository):
    """Mongo Class"""
    def __init__(self):
        self.client = MongoClient(host=get_settings().mongo_url)
        self.db = self.client.get_database('tinyurl')
        self.collection = self.db.urls

    async def save_url(self, short_url: str, long_url: str) -> None:
        await asyncio.to_thread(
            self.collection.insert_one,
            {
                "short_url": short_url,
                "long_url": long_url,
                "created": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
            }
        )

    def get_url(self, short_url: str) -> str:
        if result := self.collection.find_one({"short_url": short_url}):
            return result.get("long_url")
        return None

    async def delete_url(self, short_url: str) -> bool:
        result = self.collection.delete_one({"short_url":short_url})
        return result.deleted_count == 1

    def __del__(self):
        self.client.close()
