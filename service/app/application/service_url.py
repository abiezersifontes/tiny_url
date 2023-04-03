""" Logic of the Generation of the Tiny-URL"""
import string
import asyncio
from service.settings import get_settings
from service.app.domain.repositories.conf_repository import ConfigurationRepository
from service.app.domain.repositories.store_repository import StoreRepository
from service.app.domain.repositories.cache_repository import CacheRepository

class ServiceUrl:
    """Class with th Logic to Generate the Tiny URL"""

    def __init__(self, conf_repository: ConfigurationRepository, store: StoreRepository, cache: CacheRepository) -> None:
        self.conf_repository = conf_repository
        self.ascii_chars = string.ascii_letters + string.digits + '-._~!$\'()*+,;=:@'
        self.num_chars = len(self.ascii_chars)
        self.store = store
        self.cache = cache

    def generate_url(self, url: str) -> str:
        """Generate the tiny url"""
        start, end = self.conf_repository.get_range()
        sequence = ""
        index = start
        for _ in range(6):
            index, remainder = divmod(index, self.num_chars)
            sequence += self.ascii_chars[remainder]
        short_url = f"{get_settings().base_url}{sequence}"
        self.conf_repository.update_range()
        asyncio.create_task(self.store.save_url(short_url=short_url, long_url=url))
        return short_url

    async def get_url(self, url_str) -> str:
        url = f"{get_settings().base_url}{url_str}"
        print(url)
        cached_url = await self.cache.get(key=url)
        if cached_url is not None:
            return cached_url
        db_url = await self.store.get_url(url)
        if db_url is not None:
            await self.cache.set(key=url, value=db_url, expire=3600)
        return db_url

    def delete_url(self, url_str) -> bool:
        url = f"{get_settings().base_url}{url_str}"
        return self.store.delete_url(url)