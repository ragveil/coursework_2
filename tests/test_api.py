from pytest_mock import MockerFixture

from src.api import HeadHunterApi


def test_headhunter_api(mocker: MockerFixture, data: list[dict]) -> None:
    mock_response = mocker.patch("requests.get")
    mock_response.return_value.status_code = 200
    mock_response.return_value.json.return_value = {"items": data}
    api = HeadHunterApi()
    vacancies = api.get_data("Без опыта")
    assert len(vacancies) == 3
    assert vacancies[0]["id"] == 12345678
    assert vacancies[0]["name"] == "Python Dev"
    assert vacancies[1]["id"] == 87654321
    assert vacancies[1]["name"] == "Разнорабочий"
    assert vacancies[2]["id"] == 88888888
    assert vacancies[2]["name"] == "Грузчик"
    assert isinstance(vacancies, list)
    mock_response.assert_called()
