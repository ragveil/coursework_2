from src.api import HeadHunterApi  # pragma: no cover
from src.constants import csv_file, json_file, xlsx_file  # pragma: no cover
from src.saver import CSVSaver, JSONSaver  # pragma: no cover
from src.utils import print_result, search_by_salary, search_vacancy, show_top, sort_by_salary  # pragma: no cover
from src.vacancy import Vacancy  # pragma: no cover
from src.xlsx_saver import ExcelSaver  # pragma: no cover


def user_interaction():  # pragma: no cover
    """
    Основная функция программы, объединяющая все модули.
    :return:
    """
    global saver
    hh_api = HeadHunterApi()
    message = "Нет сохраненных вакансий."
    print("Выберите предпочитаемый формат файла для дальнейшей работы.")
    extension = input('Введите "JSON" или "CSV" для выбора.').upper()
    while extension != "JSON" and extension != "CSV":
        extension = input('Введите "JSON" или "CSV" для выбора.').upper()
    if extension == "JSON":
        saver = JSONSaver(json_file)
    elif extension == "CSV":
        saver = CSVSaver(csv_file)

    while True:
        print("Меню:")
        print("1. Поиск вакансий")
        print("2. Топ вакансий по зарплате")
        print("3. Поиск вакансии по диапазону зарплат")
        print("4. Поиск вакансии по ключевому слову в описании")
        print("5. Удаление вакансии из списка по id")
        print("6. Сформировать таблицу вакансий в XLSX")
        print("7. Просмотр сохраненных вакансий")
        print("8. Завершение работы")

        user_choice = input("Выберите подходящий пункт из меню.")
        while user_choice not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            user_choice = input("Выберите подходящий пункт из меню.")

        if user_choice == "1":
            keyword = input("Введите ключевое слово для поиска вакансий.")
            try:
                got_vacancies = hh_api.get_data(keyword)
                listed_vacancies = Vacancy.from_json_to_list(got_vacancies)
            except Exception as e:
                print(f"Возникла ошибка в работе api: {type(e).__name__}")
            else:
                if_sort = input('Отсортировать вакансии по заработной плате? Введите "да" для сортировки.').lower()
                if if_sort == "да":
                    listed_vacancies = sort_by_salary(listed_vacancies)
                for item in listed_vacancies:
                    saver.add_vacancy(item)
                print(f"Найдено {len(listed_vacancies)} вакансий. Результат сохранён.")

        elif user_choice == "2":
            vacancies = saver.get_vacancies()
            if not vacancies:
                print(message)
                continue
            print(f"Всего вакансий: {len(vacancies)}.")
            choice = input("Введите количество вакансий для отображения")
            try:
                choice = int(choice)
            except ValueError:
                print("Введены некорректные данные, сформировать топ невозможно.")
                continue
            else:
                if choice < len(vacancies):
                    top_vacancies = show_top(vacancies, choice)
                    print_result(top_vacancies)
                else:
                    print("Введены некорректные данные, сформировать топ невозможно.")

        elif user_choice == "3":
            vacancies = saver.get_vacancies()
            if not vacancies:
                print(message)
                continue
            start = input("Введите минимальный порог зарплаты (только цифры).")
            stop = input("Введите максимальный порог зарплаты (только цифры).")
            try:
                start = int(start)
                stop = int(stop)
            except ValueError:
                print("Введены некорректные данные.")
                continue
            salary_range = search_by_salary(vacancies, start, stop)
            if salary_range:
                print_result(salary_range)
            else:
                print("Нет вакансий, соответствующих Вашим запросам.")

        elif user_choice == "4":
            vacancies = saver.get_vacancies()
            if not vacancies:
                print(message)
                continue
            keyword = input("Введите ключевое слово для поиска в описании вакансии.")
            filtered_vacancies = search_vacancy(vacancies, keyword)
            if filtered_vacancies:
                print_result(filtered_vacancies)
            else:
                print("Не найдено подходящих вакансий.")

        elif user_choice == "5":
            vacancies = saver.get_vacancies()
            if not vacancies:
                print(message)
                continue
            ids = input("Введите id вакансии для удаления.")
            try:
                ids = int(ids)
            except ValueError:
                print("Введены некорректные данные.")
                continue
            v_to_remove = [v for v in vacancies if v.ids == ids]
            if not v_to_remove:
                print("Указанный id не найден.")
                continue
            for v in v_to_remove:
                saver.remove_vacancy(v)
            print("Вакансия удалена.")

        elif user_choice == "6":
            vacancies = saver.get_vacancies()
            if not vacancies:
                print(message)
                continue
            ExcelSaver(xlsx_file).save_to_file(vacancies)
            print("Таблица вакансий в XLSX успешно сформирована.")

        elif user_choice == "7":
            vacancies = saver.get_vacancies()
            if not vacancies:
                print(message)
                continue
            print_result(vacancies)

        elif user_choice == "8":
            print("Программа завершает свою работу. Всего доброго!")
            break

        else:
            print("парам-пам-пам")


if __name__ == "__main__":  # pragma: no cover
    user_interaction()
