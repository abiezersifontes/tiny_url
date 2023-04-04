"""Environment Settings File"""
import os
from functools import lru_cache
from typing import Type
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Environment Settings"""
    zookeeper_hosts: str = os.getenv("ZOOKEEPER_HOSTS", None)
    zookeeper_path: str = os.getenv("ZOOKEEPER_PATH", None)
    base_url: str = os.getenv("BASE_URL", None)
    mongo_url: str = os.getenv("MONGO_URL", None)
    redis_url: str = os.getenv("REDIS_URL", None)

@lru_cache
def get_settings() -> Type[Settings]:
    """Return the settings once"""
    return Settings()
