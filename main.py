from src.hh import HH
from src.utils import filter_by_salary, sort_top_n
from src.vacancy import Vacancy


def user_interaction():
    """функция взаимодействия с пользователем"""

    search_query = input("Введите поисковый запрос:\n")

    vacancies = HH()
    vacancies.get_vacancies(search_query)
    list_vacancies = []

    for vacancy in vacancies.vacancies[0:3]:
        list_vacancies.append(Vacancy.create_vacancy(vacancy))

    top_n = int(input("Введите количество вакансий для вывода в топ N:\n"))

    revers = input("Отфильтровать по возрастанию з/п?\n")
    if revers.islower() == "да":
        revers = False
    else:
        revers = True

    salary_range = input("Введите диапазон зарплат:\n")  # Пример: 100000 - 150000

    salary_range_start = float(salary_range.split("-")[0])
    salary_range_end = float(salary_range.split("-")[1])

    ranged_vacancies = filter_by_salary(list_vacancies, salary_range_end, salary_range_start)
    sorted_vacancies = sort_top_n(ranged_vacancies, top_n, revers)

    for vacancy in sorted_vacancies:
        print(vacancy)


if __name__ == "__main__":
    user_interaction()
