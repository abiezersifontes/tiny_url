"""Implementation of Generate Url"""
import json
from typing import List
from kazoo.client import KazooClient
from service.settings import get_settings
from service.app.domain.repositories.conf_repository import ConfigurationRepository


class ZookeeperRepo(ConfigurationRepository):
    """Implementation of Generate Url"""
    def __init__(self):
        self.zk = KazooClient(hosts=get_settings().zookeeper_hosts)
        self.zk.start()
        self.zk_path = get_settings().zookeeper_path
        self.counter, self.end_range = self._load_counter()

    def _load_counter(self) -> int:
        data, _ = self.zk.get(self.zk_path)
        result = json.loads(data.decode())
        return [int(result.get('start')), int(result.get('end'))]

    def get_range(self) -> List[int]:
        """Get range of numbers"""
        data, stat = self.zk.get(self.zk_path)
        data = json.loads(data.decode())
        start = data.get('start')
        end = data.get('end')
        return [start, end]

    def update_range(self) -> None:
        """udpate the range of numbers"""
        self.counter += 1
        range_data = {"start": self.counter, "end": self.end_range}
        return self.zk.set(self.zk_path, json.dumps(range_data).encode())

    def set_range(self, start: int, end: int) -> None:
        """Sets the range of numbers in ZooKeeper"""
        data = {"start": start, "end": end}
        return self.zk.set(self.zk_path, json.dumps(data).encode())

    def __del__(self):
        self.zk.stop()
