import os

from config import ROOT_DIR
from src.saver import CSVSaver, JSONSaver
from src.vacancy import Vacancy

test_folder = os.path.join(ROOT_DIR, "tests/data/")
json_file = os.path.join(test_folder, "test_vacancies.json")
csv_file = os.path.join(test_folder, "test_vacancies.csv")


def test_json_saver_add(vacs: list[Vacancy]) -> None:
    saver = JSONSaver(filename=json_file)
    saver.add_vacancy(vacs[0])
    vacancies = saver.get_vacancies()
    assert vacancies[0].ids == vacs[0].ids


def test_json_saver_save(vacs: list[Vacancy]) -> None:
    saver = JSONSaver(filename=json_file)
    saver.save_to_file(vacs)
    vacancies = saver.get_vacancies()
    assert os.path.isfile(json_file)
    assert vacancies[0].ids == vacs[0].ids
    assert vacancies[1].ids == vacs[1].ids
    assert len(vacancies) == 3


def test_csv_saver_add(vacs: list[Vacancy]) -> None:
    saver = CSVSaver(filename=csv_file)
    saver.add_vacancy(vacs[0])
    vacancies = saver.get_vacancies()
    assert vacancies[0].ids == vacs[0].ids


def test_csv_saver_save(vacs: list[Vacancy]) -> None:
    saver = CSVSaver(filename=csv_file)
    saver.save_to_file(vacs)
    vacancies = saver.get_vacancies()
    assert os.path.isfile(csv_file)
    assert vacancies[0].ids == vacs[0].ids
    assert vacancies[1].ids == vacs[1].ids
    assert len(vacancies) == 3
