from src.vacancy import Vacancy


def sort_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    return sorted(vacancies, key=lambda v: v.salary, reverse=True)


def show_top(vacancies: list[Vacancy], n: int) -> list[Vacancy]:
    return sorted(vacancies, key=lambda v: v.salary, reverse=True)[:n]


def search_vacancy(vacancies: list[Vacancy], keyword: str) -> list[Vacancy]:
    return list(filter(lambda v: keyword.lower() in v.responsibility.lower(), vacancies))


def search_by_salary(vacancies: list[Vacancy], start: int, stop: int) -> list[Vacancy]:
    if start < stop:
        return list(filter(lambda v: start <= v.salary <= stop, vacancies))
    elif start > stop:
        return list(filter(lambda v: stop <= v.salary <= start, vacancies))
    elif start == stop:
        return list(filter(lambda v: v.salary == start, vacancies))
    else:
        return vacancies


def print_result(vacancies: list[Vacancy]) -> None:
    for v in vacancies:
        print(v)
