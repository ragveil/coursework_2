import pandas as pd

from src.vacancy import Vacancy


class ExcelSaver:
    """
    Самостоятельный класс для создания таблицы и сохранения ее в файл XLSX.
    """

    def __init__(self, filename: str) -> None:
        self.__filename = filename

    def save_to_file(self, vacancies: list[Vacancy]) -> None:
        df = pd.DataFrame(v.as_dict() for v in vacancies)
        df.to_excel(self.__filename, index=False)
