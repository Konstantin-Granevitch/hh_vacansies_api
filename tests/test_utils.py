from src.utils import filter_by_salary, sort_top_n


def test_filter_by_salary(list_vacancies):
    """тест фильтра по з/п на работу по правильному диапазону"""

    result1 = filter_by_salary(list_vacancies, 3000, 2000)  # проверка правильного диапазона
    result2 = filter_by_salary(list_vacancies, 1000)  # проверка не полного диапазона
    result3 = filter_by_salary(list_vacancies, 4000, 2000)  # проверка правильного диапазона
    result4 = filter_by_salary(list_vacancies, 4000.9, 2000.99)  # проверка дробного диапазона
    result5 = filter_by_salary(list_vacancies, 1000, 4000)  # проверка перевернутого диапазона

    assert len(result1) == 3
    assert len(result2) == 1
    assert len(result3) == 4
    assert len(result4) == 2
    assert len(result5) == 5


def test_filter_by_salary_incorrect(list_vacancies, capsys):
    """тест фильтра по з/п на работу с не корректным диапазоном"""

    filter_by_salary(list_vacancies, "dhf")
    captured = capsys.readouterr()

    assert captured.out == "значения диапазона должны быть числами!\n"


def test_sort_top_n(list_vacancies):
    """тест на нормальную работу сортировки"""

    result1 = sort_top_n(list_vacancies)  # проверка на сортировку без указания количества вакансий
    result2 = sort_top_n(list_vacancies, 3)  # проверка на сортировку с указанием количества вакансий
    result3 = sort_top_n(list_vacancies, 4, False)  # проверка на сортировку с реверсом

    assert result1[0].salary == 4000 and len(result1) == 5
    assert result2[0].salary == 4000 and len(result2) == 3
    assert result3[0].salary == 1000 and len(result3) == 4


def test_sort_top_n_incorrect(list_vacancies, capsys):
    """тест сортировки с не корректным топ-n значением"""

    sort_top_n(list_vacancies, "dhf")
    captured = capsys.readouterr()

    assert captured.out == "значение топ-n вакансий должно быть числом!\n"
