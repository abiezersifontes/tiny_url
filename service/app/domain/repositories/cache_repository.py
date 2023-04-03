from abc import ABC, abstractmethod

class CacheRepository(ABC):
    @abstractmethod
    async def connect(self):
        pass
    
    @abstractmethod
    async def disconnect(self):
        pass

    @abstractmethod
    def get(self, key: str) -> str:
        pass
    
    @abstractmethod
    def set(self, key: str, value: str, expire: int = None) -> None:
        pass

    @abstractmethod
    async def delete(self, key: str) -> None:
        pass
