import re
from abc import ABC, abstractmethod
from typing import Any


class BaseVacancy(ABC):  # pragma: no cover
    """
    Абстрактный класс.
    """

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


class Vacancy(BaseVacancy):
    """
    Класс вакансий. Для экономии ресурсов используются слоты.
    """

    __slots__ = {
        "__ids": "id вакансии",
        "__title": "Название вакансии",
        "__salary": "Заработная плата",
        "__url": "Ссылка",
        "__company": "Компания-работодатель",
        "__area": "Местоположение",
        "__requirements": "Требования",
        "__responsibility": "Описание деятельности",
        "__schedule": "График",
        "__experience": "Требуемый опыт",
        "__employment": "Вид занятости",
        "__period": "Период заработной платы",
    }

    def __init__(
        self,
        ids: int,
        title: str,
        salary: int,
        url: str,
        company: str,
        area: str,
        requirements: str,
        responsibility: str,
        schedule: str,
        experience: str,
        employment: str,
        period: str,
    ):
        self.__ids = self.__validate_ids(ids)
        self.__title = self.__validate_title(title)
        self.__salary = self.__validate_salary(salary)
        self.__url = self.__validate_url(url)
        self.__company = company
        self.__area = area
        self.__requirements = self.__validate_requirements(requirements)
        self.__responsibility = self.__validate_responsibility(responsibility)
        self.__schedule = schedule
        self.__experience = self.__validate_experience(experience)
        self.__employment = employment
        self.__period = period
        super().__init__()

    @staticmethod
    def __validate_salary(salary: int) -> int:
        try:
            return int(salary)
        except (ValueError, TypeError):
            return 0

    @staticmethod
    def __validate_ids(ids: int) -> int:
        return int(ids) if ids else 000000000

    @staticmethod
    def __validate_title(title: str) -> str:
        return title if title else "Вакансия без названия"

    @staticmethod
    def __validate_url(url: str) -> str:
        return url.lower() if url else "Нет ссылки"

    @staticmethod
    def __validate_requirements(requirements: str) -> str:
        pattern = r"<[a-zA-Z/]{4,}>"
        re.sub(pattern, "", requirements)
        return requirements if requirements else "Нет требований"

    @staticmethod
    def __validate_experience(experience: str) -> str:
        return experience if experience else "Опыт не указан"

    @staticmethod
    def __validate_responsibility(responsibility: str) -> str:
        pattern = r"<[a-zA-Z/]{4,}>"
        responsibility = re.sub(pattern, "", responsibility)
        return responsibility if responsibility else "Нет описания"

    @property
    def ids(self) -> int:
        return self.__ids

    @property
    def title(self) -> str:
        return self.__title

    @property
    def salary(self) -> int:
        return self.__salary

    @property
    def url(self) -> str:
        return self.__url

    @property
    def company(self) -> str:
        return self.__company

    @property
    def area(self) -> str:
        return self.__area

    @property
    def requirements(self) -> str:
        return self.__requirements

    @property
    def responsibility(self) -> str:
        return self.__responsibility

    @property
    def schedule(self) -> str:
        return self.__schedule

    @property
    def experience(self) -> str:
        return self.__experience

    @property
    def employment(self) -> str:
        return self.__employment

    @property
    def period(self) -> str:
        return self.__period.lower()

    def as_dict(self) -> dict:
        """
        Представление вакансии в виде словаря.
        :return:
        """
        return {
            "ids": self.ids,
            "title": self.title,
            "salary": self.salary,
            "url": self.url,
            "company": self.company,
            "area": self.area,
            "requirements": self.requirements,
            "responsibility": self.responsibility,
            "schedule": self.schedule,
            "experience": self.experience,
            "employment": self.employment,
            "period": self.period,
        }

    def __eq__(self, other: object) -> Any:
        if not isinstance(other, Vacancy):
            return NotImplemented
        if self.ids != other.ids:
            return self.salary == other.salary

    def __lt__(self, other: object) -> Any:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary < other.salary

    def __gt__(self, other: object) -> Any:
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary > other.salary

    def __str__(self) -> str:
        """
        Строковое представление вакансии.
        :return:
        """
        return (
            f"ID: {self.ids}"
            f"\nВакансия: {self.title}"
            f"\nЗарплата: {self.salary} {self.period}"
            f"\nСсылка: {self.url}"
            f"\nРаботодатель: {self.company}"
            f"\nМестоположение: {self.area}"
            f"\nТребования: {self.requirements}"
            f"\nОписание: {self.responsibility}"
            f"\nОпыт: {self.experience}"
            f"\nГрафик: {self.schedule}"
            f"\nВид занятости: {self.employment}\n"
        )

    @classmethod
    def from_json_to_list(cls, vacancies: list[dict]) -> list:
        """
        Метод для преобразования списка словарей в объекты класса.
        :param vacancies:
        :return:
        """
        result = []
        for vacancy in vacancies:
            start = vacancy.get("salary", {}).get("from")
            stop = vacancy.get("salary", {}).get("to")
            if start and start > 0:
                if stop and stop > 0:
                    salary = (start + stop) / 2
                else:
                    salary = start
            elif stop and stop > 0:
                salary = stop
            else:
                salary = 0
            result.append(
                cls(
                    vacancy.get("id", 0),
                    vacancy.get("name", ""),
                    salary,
                    vacancy.get("alternate_url", ""),
                    vacancy.get("employer", {}).get("name"),
                    vacancy.get("area", {}).get("name"),
                    vacancy.get("snippet", {}).get("requirement"),
                    vacancy.get("snippet", {}).get("responsibility"),
                    vacancy.get("schedule", {}).get("name"),
                    vacancy.get("experience", {}).get("name"),
                    vacancy.get("employment", {}).get("name"),
                    vacancy.get("salary_range", {}).get("mode").get("name"),
                )
            )
        return result
