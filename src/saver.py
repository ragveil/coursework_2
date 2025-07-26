import os
from abc import ABC, abstractmethod

from config import ROOT_DIR
from src.vacancy import Vacancy

data_folder = os.path.join(ROOT_DIR, "data/")


class Saver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        pass

