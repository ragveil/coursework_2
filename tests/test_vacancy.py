from src.vacancy import Vacancy


def test_vacancy_init() -> None:
    vacancy = Vacancy(
        12345678,
        "Название",
        100000,
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
    assert vacancy.salary == 100000
    assert vacancy.ids == 12345678


def test_vacancy_valid() -> None:
    vacancy = Vacancy(
        "", "", "", "", "работодатель", "местоположение", "", "", "график", "", "вид занятости", "за месяц"
    )
    assert vacancy.salary == 0
    assert vacancy.ids == 00000000
    assert vacancy.responsibility == "Нет описания"
    assert vacancy.requirements == "Нет требований"
    assert vacancy.url == "Нет ссылки"


def test_from_json_to_list(data: list[dict]) -> None:
    vacancies = Vacancy.from_json_to_list(data)
    assert len(vacancies) == 3
    assert vacancies[0].ids == 12345678
    assert vacancies[0].title == "Python Dev"
    assert vacancies[1].ids == 87654321
    assert vacancies[1].title == "Разнорабочий"
    assert vacancies[2].ids == 88888888
    assert vacancies[2].title == "Грузчик"


def test_vacancy_as_dict() -> None:
    vacancy = Vacancy(
        12345678,
        "Название",
        100000,
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
    dict = vacancy.as_dict()
    assert dict["ids"] == 12345678
    assert dict["title"] == "Название"
    assert dict["salary"] == 100000


def test_vacancy_compare(data: list[dict]) -> None:
    vac1, vac2, vac3 = Vacancy.from_json_to_list(data)
    assert vac1 > vac2
    assert vac1 > vac3
    assert vac2 == vac3
