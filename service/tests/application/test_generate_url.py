"""test the generation of tiny url"""
from service.app.application.service_url import ServiceUrl
from service.app.domain.repositories.conf_repository import ConfigurationRepository
from service.app.domain.repositories.store_repository import StoreRepository
from service.app.domain.repositories.cache_repository import CacheRepository

def test_generate_url() -> None:
    """test the generation of tiny url"""
    repo = ServiceUrl(ConfigurationRepository, store=StoreRepository, cache=CacheRepository)
    assert isinstance(repo, ServiceUrl)
