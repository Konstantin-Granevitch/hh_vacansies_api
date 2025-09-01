from src.vacancy import Vacancy


def filter_by_salary(list_vacancies: list, end: (int, float), start: (int, float) = 0) -> list:
    """функция для поиска вакансий по диапазону з/п"""

    if isinstance(start, (int, float)) and isinstance(end, (int, float)): # проверка диапазона на числа
        result = []

        if end < start: # проверка на корректность диапазона
            end, start = start, end

        for vacancy in list_vacancies:
            if start <= vacancy.salary <= end:
                result.append(vacancy)

        return result
    else:
        print("значения диапазона должны быть числами!")
        return list_vacancies


def sort_top_n(list_vacancies: list, top_n: int = 20, revers: bool = True) -> list:
    """функция для поиска топ-n и сортировке вакансий по з/п"""

    if not(isinstance(top_n, int)):
        print("значение топ-n вакансий должно быть числом!")
        top_n = 20

    result = sorted(list_vacancies, key=lambda vacancy: vacancy.salary, reverse=revers)

    return result[: top_n]


if __name__ == "__main__":
    vac1 = Vacancy("name1", "resp1", 1000, "req1")
    vac2 = Vacancy("name2", "resp2", 2000, "req2")
    vac3 = Vacancy("name3", "resp3", 3000, "req3")
    vac4 = Vacancy("name4", "resp4", 2000, "req4")
    vac5 = Vacancy("name5", "resp5", 4000, "req5")
    vacancis = [vac1, vac2, vac3, vac4, vac5]

    sort = filter_by_salary(vacancis, 2000, 4000)
    # sort_n = sort_top_n(sort, 3)
    for i in sort:
        print(i)