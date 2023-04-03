"""Repository of Configurations"""
import abc
from typing import List


class ConfigurationRepository(abc.ABC):
    """Repository for key store values """

    @abc.abstractmethod
    def get_range(self) -> List[int]:
        """Get the range of ascii charaters to generate a unique key"""

    @abc.abstractmethod
    def update_range(self) -> None:
        """Get range of numbers"""
