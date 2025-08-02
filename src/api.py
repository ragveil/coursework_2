from abc import ABC, abstractmethod
from typing import Any

import requests

from src.vacancy import Vacancy


class BaseApi(ABC):
    """
    Абстрактный класс.
    """

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_data(self, keyword: str) -> Any:
        pass


class HeadHunterApi(BaseApi):
    """
    Класс для получения данных с HeadHunter.
    """

    def __init__(self) -> None:
        """
        Инициализирует данные для api.
        """
        self.url = "https://api.hh.ru/vacancies"
        self.params: Any = {
            "text": "",
            "area": 113,
            "per_page": 10,
            "only_with_salary": True,  # Поиск по вакансиям, в которых указана зарплата.
        }
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.vacancies: list[Vacancy] = []
        super().__init__()

    def get_data(self, keyword: str | None) -> Any:
        """Формирует запрос и получает данные о вакансиях."""
        self.params["text"] = keyword
        response = requests.get(self.url, params=self.params, headers=self.headers)
        if response.status_code != 200:
            print(response.status_code)
            raise ConnectionError("Ошибка подключения")
        data = response.json()
        return data.get("items", [])
