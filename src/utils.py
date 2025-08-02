from src.vacancy import Vacancy


def sort_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """
    Сортирует список вакансий по заработной плате в порядке убывания.
    :param vacancies: Список вакансий, list{Vacancy}.
    :return:
    """
    return sorted(vacancies, key=lambda v: v.salary, reverse=True)


def show_top(vacancies: list[Vacancy], n: int) -> list[Vacancy]:
    """
    Отображает топ вакансий.
    :param vacancies: Список вакансий, list{Vacancy}.
    :param n: Количество вакансий для отображения в топе, int.
    :return:
    """
    return sorted(vacancies, key=lambda v: v.salary, reverse=True)[:n]


def search_vacancy(vacancies: list[Vacancy], keyword: str) -> list[Vacancy]:
    """
    Поиск среди вакансий по ключевому слову.
    :param vacancies: Список вакансий, list{Vacancy}.
    :param keyword: Ключевое слово, str.
    :return:
    """
    return list(filter(lambda v: keyword.lower() in v.responsibility.lower(), vacancies))


def search_by_salary(vacancies: list[Vacancy], start: int, stop: int) -> list[Vacancy]:
    """
    Поиск вакансии по размеру заработной платы.
    :param vacancies: Список вакансий, list{Vacancy}.
    :param start: Минимальная заработная плата, int.
    :param stop: Максимальная заработная плата, int.
    :return:
    """
    if start < stop:
        return list(filter(lambda v: start <= v.salary <= stop, vacancies))
    else:
        return vacancies


def print_result(vacancies: list[Vacancy]) -> None:
    """
    Выводит информацию о вакансиях в консоль.
    :param vacancies: Список вакансий, list{Vacancy}.
    :return:
    """
    for v in vacancies:
        print(v)
