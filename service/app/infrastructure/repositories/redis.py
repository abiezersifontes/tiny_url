"""Redis repository."""
import aioredis
from service.settings import get_settings
from service.app.domain.repositories.cache_repository import CacheRepository


class RedisRepo(CacheRepository):
    """Redis repository."""
    def __init__(self):
        self.redis = None

    async def connect(self):
        """Connect to redis."""
        self.redis = await aioredis.from_url(get_settings().redis_url, encoding='utf-8', decode_responses=True)

    async def disconnect(self):
        """Disconnect from redis."""
        self.redis.close()
        await self.redis.wait_closed()

    async def get(self, key: str) -> str:
        """Get value from redis."""
        if self.redis is None:
            await self.connect()
        return await self.redis.get(key)

    async def set(self, key: str, value: str, expire: int = None) -> None:
        """Set value to redis."""
        if self.redis is None:
            await self.connect()
        if expire is not None:
            await self.redis.setex(key, expire, value)
        else:
            await self.redis.set(key, value)

    async def delete(self, key: str) -> None:
        """Delete value from redis."""
        if self.redis is None:
            await self.connect()
        await self.redis.delete(key)
