import os

import pandas as pd
from pandas._testing import assert_frame_equal

from src.vacancy import Vacancy
from src.xlsx_saver import ExcelSaver
from tests.test_saver import test_folder

xlsx_file = os.path.join(test_folder, "test_vacancies.xlsx")


def test_xlsx_saver_save(vacs: list[Vacancy]) -> None:
    saver = ExcelSaver(filename=xlsx_file)
    saver.save_to_file(vacs)
    df = pd.DataFrame(v.as_dict() for v in vacs)
    assert os.path.isfile(xlsx_file)
    assert_frame_equal(pd.read_excel(xlsx_file), df)
