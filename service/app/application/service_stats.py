from service.app.domain.repositories import StoreRepository

class ServiceStats:
    def __init__(self, store_repo: StoreRepository) -> None:
        self.store = store_repo

    def add_hit(self, url: str):
        self.store.add_hit(url)
    
    def add_miss(self, url: str):
        self.store.add_miss(url)
    
    def add_status_code(self, url: str, status_code: int):
        self.store.add_status_code(url, status_code)