"""MongoDB implementation of the stats repository"""
from datetime import datetime, timedelta
from pymongo import MongoClient
from service.settings import get_settings

class StatsRepository:
    """MongoDB implementation of the stats repository"""
    def __init__(self):
        self.client = MongoClient(host=get_settings().mongo_url)
        self.db = self.client.get_database('tinyurl')
        self.collection = self.db.stats

    async def add_hit(self, url: str, status_code: int) -> None:
        """Add a hit to the stats"""
        doc = {
            "url": url,
            "timestamp": datetime.utcnow(),
            "status_code": status_code,
            "type": "hit"
        }
        return self.collection.insert_one(doc)

    async def add_miss(self, url: str, status_code) -> None:
        """Add a miss to the stats"""
        doc = {
            "url": url,
            "timestamp": datetime.utcnow(),
            "status_code": status_code,
            "type": "miss"
        }
        return self.collection.insert_one(doc)

    async def get_stats(self):
        """Return the stats of the service"""
        now = datetime.utcnow()
        day_ago = now - timedelta(days=1)

        # Count the number of hits and misses by URL
        url_stats = self.collection.aggregate([
            {
                "$match": {
                    "timestamp": {"$gte": day_ago},
                    "type": {"$in": ["hit", "miss"]}
                }
            },
            {
                "$group": {
                    "_id": "$url",
                    "hits": {"$sum": {"$cond": [{"$eq": ["$type", "hit"]}, 1, 0]}},
                    "misses": {"$sum": {"$cond": [{"$eq": ["$type", "miss"]}, 1, 0]}}
                }
            }
        ])

        # Count the number of hits and misses by status code
        status_code_stats = self.collection.aggregate([
            {
                "$match": {
                    "timestamp": {"$gte": day_ago},
                    "type": {"$in": ["hit", "miss"]}
                }
            },
            {
                "$group": {
                    "_id": "$status_code",
                    "count": {"$sum": 1}
                }
            }
        ])


        # Combine the two sets of stats
        all_stats = {
            "urls": {stats["_id"]: {"hits": stats["hits"], "misses": stats["misses"]} for stats in url_stats},
            "status_codes": {stats["_id"]: {"count": stats["count"]} for stats in status_code_stats}
        }


        return all_stats
