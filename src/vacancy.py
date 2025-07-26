from abc import ABC, abstractmethod
from typing import Any


class BaseVacancy(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __lt__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __gt__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

