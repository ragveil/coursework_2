import pandas as pd

from src.saver import data_folder
from src.vacancy import Vacancy


class ExcelSaver:
    def __init__(self, filename: str) -> None:
        self.__filename = data_folder + filename + ".xlsx"

    def save_to_file(self, vacancies: list[Vacancy]) -> None:
        df = pd.DataFrame(v.as_dict() for v in vacancies)
        df.to_excel(self.__filename, index=False)
