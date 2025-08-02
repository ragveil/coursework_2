import csv
import json
import os
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class Saver(ABC):
    """
    Абстрактный класс для работы с файлами.
    """

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def get_vacancies(self) -> list[Vacancy]:
        pass


class JSONSaver(Saver):
    """
    Класс для работы с файлами в формате JSON.
    """

    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def get_vacancies(self) -> list[Vacancy]:
        if not os.path.exists(self.__filename):
            return []
        else:
            with open(self.__filename, "r", encoding="UTF-8") as f:
                data = json.load(f)
                return [Vacancy(**item) for item in data]

    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
        self.save_to_file(vacancies)

    def remove_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        vacancies = list(filter(lambda v: v != vacancy, vacancies))
        self.save_to_file(vacancies)

    def save_to_file(self, vacancies: list[Vacancy]) -> None:
        with open(self.__filename, "w", encoding="UTF-8") as f:
            json.dump([v.as_dict() for v in vacancies], f, ensure_ascii=False, indent=4)


class CSVSaver(Saver):
    """
    Класс для работы файлами в формате CSV.
    """

    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def get_vacancies(self) -> list[Vacancy]:
        if not os.path.exists(self.__filename):
            return []
        vacancies = []
        with open(self.__filename, "r", encoding="UTF-8") as f:
            data = csv.DictReader(f)
            for row in data:
                vacancy = Vacancy(**row)
                vacancies.append(vacancy)
            return vacancies

    def add_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        if vacancy not in vacancies:
            vacancies.append(vacancy)
            self.save_to_file(vacancies)

    def remove_vacancy(self, vacancy: Vacancy) -> None:
        vacancies = self.get_vacancies()
        vacancies = list(filter(lambda v: v != vacancy, vacancies))
        self.save_to_file(vacancies)

    def save_to_file(self, vacancies: list[Vacancy]) -> None:
        with open(self.__filename, "w", newline="", encoding="UTF-8") as f:
            fields = csv.DictWriter(f, fieldnames=vacancies[0].as_dict().keys())
            fields.writeheader()
            for v in vacancies:
                fields.writerow(v.as_dict())
