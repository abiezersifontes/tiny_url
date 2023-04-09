import abc
from typing import Dict

class StoreRepository(abc.ABC):
    @abc.abstractmethod
    def save_url(self, short_url: str, long_url: str) -> bool:
        """save url"""

    @abc.abstractmethod
    def get_url(self, short_url: str) -> Dict:
        """get url"""

    @abc.abstractmethod
    async def delete_url(self, short_url: str) -> bool:
        """delete url"""