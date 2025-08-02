import os
from typing import Generator

import pytest

from src.vacancy import Vacancy


@pytest.fixture
def data() -> list[dict]:
    return [
        {
            "id": 12345678,
            "name": "Python Dev",
            "alternate_url": "url",
            "salary": {"from": 100000, "to": 200000},
            "employer": {"name": "Microsoft CORP."},
            "area": {"name": "Moscow"},
            "snippet": {"requirement": "Python", "responsibility": "Hard coding"},
            "schedule": {"name": "Полный рабочий день"},
            "experience": {"name": "Без опыта"},
            "employment": {"name": "Полная занятость"},
            "salary_range": {"mode": {"name": "За месяц"}},
        },
        {
            "id": 87654321,
            "name": "Разнорабочий",
            "alternate_url": "url2",
            "salary": {"from": 50000, "to": 80000},
            "employer": {"name": "Ёшки-Матрёшки"},
            "area": {"name": "Кукуево"},
            "snippet": {"requirement": "Начальное образование", "responsibility": "Всё, везде и одновременно"},
            "schedule": {"name": "Полный рабочий день"},
            "experience": {"name": "Без опыта"},
            "employment": {"name": "Полная занятость"},
            "salary_range": {"mode": {"name": "За месяц"}},
        },
        {
            "id": 88888888,
            "name": "Грузчик",
            "alternate_url": "url3",
            "salary": {"from": 50000, "to": 80000},
            "employer": {"name": "Кирпичи и ко"},
            "area": {"name": "Чертокуличинск"},
            "snippet": {"requirement": "Начальное образование", "responsibility": "Скажи спине 'ДО СВИДАНИЯ'"},
            "schedule": {"name": "Полный рабочий день"},
            "experience": {"name": "Без опыта"},
            "employment": {"name": "Полная занятость"},
            "salary_range": {"mode": {"name": "За месяц"}},
        },
    ]


@pytest.fixture
def vacs(data: list[dict]) -> list[Vacancy]:
    return Vacancy.from_json_to_list(data)


@pytest.fixture
def printed_result() -> str:
    return (
        "ID: 12345678\n"
        "Вакансия: Python Dev\n"
        "Зарплата: 150000 за месяц\n"
        "Ссылка: url\n"
        "Работодатель: Microsoft CORP.\n"
        "Местоположение: Moscow\n"
        "Требования: Python\n"
        "Описание: Hard coding\n"
        "Опыт: Без опыта\n"
        "График: Полный рабочий день\n"
        "Вид занятости: Полная занятость\n"
        "\n"
    )


@pytest.fixture
def addition_vacs(data: list[dict]) -> Vacancy:
    return Vacancy(
        12345678,
        "Название",
        200000,
        "ссылка",
        "работодатель",
        "местоположение",
        "требования",
        "описание",
        "график",
        "опыт",
        "вид занятости",
        "за месяц",
    )


@pytest.fixture
def temporary_json() -> Generator[str, None, None]:
    import tempfile

    with tempfile.NamedTemporaryFile(mode="w", suffix=".json") as f:
        filename = f.name
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


@pytest.fixture
def temporary_csv() -> Generator[str, None, None]:
    import tempfile

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv") as f:
        filename = f.name
    yield filename
    if os.path.exists(filename):
        os.remove(filename)
