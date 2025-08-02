import os  # pragma: no cover

from config import ROOT_DIR  # pragma: no cover

data_folder = os.path.join(ROOT_DIR, "data/")  # pragma: no cover
json_file = os.path.join(data_folder, "vacancies.json")  # pragma: no cover
csv_file = os.path.join(data_folder, "vacancies.csv")  # pragma: no cover
xlsx_file = os.path.join(data_folder, "vacancies.xlsx")  # pragma: no cover
