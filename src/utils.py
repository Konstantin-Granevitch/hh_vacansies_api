def filter_by_salary(list_vacancies: list, end: (int, float), start: (int, float) = 0) -> list:
    """функция для поиска вакансий по диапазону з/п"""

    if isinstance(start, (int, float)) and isinstance(end, (int, float)):  # проверка диапазона на числа
        result = []

        if end < start:  # проверка на корректность диапазона
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

    if not (isinstance(top_n, int)):
        print("значение топ-n вакансий должно быть числом!")
        top_n = 20

    result = sorted(list_vacancies, key=lambda vacancy: vacancy.salary, reverse=revers)

    return result[:top_n]
