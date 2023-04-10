"""Cache repository interface."""
from abc import ABC, abstractmethod

class CacheRepository(ABC):
    """Cache repository interface."""
    @abstractmethod
    async def connect(self):
        """Connect to cache."""

    @abstractmethod
    async def disconnect(self):
        """Disconnect from cache."""

    @abstractmethod
    async def get(self, key: str) -> str:
        """Get value from cache."""

    @abstractmethod
    async def set(self, key: str, value: str, expire: int = None) -> None:
        """Set value to cache."""

    @abstractmethod
    async def delete(self, key: str) -> None:
        """Delete value from cache."""
