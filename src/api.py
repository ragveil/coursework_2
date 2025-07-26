from abc import ABC, abstractmethod
from typing import Any


class BaseApi(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_data(self, keyword: str) -> Any:
        pass

