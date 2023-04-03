"""Environment Settings File"""
from functools import lru_cache
from typing import Type
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Environment Settings"""
    zookeeper_hosts: str
    zookeeper_path: str
    base_url: str
    mongo_url: str
    redis_url: str

@lru_cache
def get_settings() -> Type[Settings]:
    """Return the settings once"""
    return Settings()
