import pytest

from src.utils import print_result, search_by_salary, search_vacancy, show_top, sort_by_salary
from src.vacancy import Vacancy


def test_sort_by_salary(vacs: list[Vacancy]) -> None:
    salaries = [v.salary for v in vacs]
    sorted_salaries = [v.salary for v in sort_by_salary(vacs)]
    assert sorted_salaries == sorted(salaries, reverse=True)


def test_show_top(vacs: list[Vacancy]) -> None:
    top_1 = show_top(vacs, 1)
    result = sort_by_salary(vacs)
    assert top_1[0].salary == result[0].salary
    assert top_1[0].ids == result[0].ids


def test_search_by_salary(vacs: list[Vacancy]) -> None:
    result = search_by_salary(vacs, 100000, 200000)
    assert result[0].ids == 12345678


def test_search_by_salary_incorrect(vacs: list[Vacancy]) -> None:
    result = search_by_salary(vacs, 200000, 100000)
    assert len(result) == len(vacs)


def test_search_vacancy(vacs: list[Vacancy]) -> None:
    result = search_vacancy(vacs, "Hard")
    assert result[0].ids == 12345678


def test_print_result(capsys: pytest.CaptureFixture, vacs: list[Vacancy], printed_result: str) -> None:
    result = show_top(vacs, 1)
    print_result(result)
    captured = capsys.readouterr()
    assert captured.out == printed_result
