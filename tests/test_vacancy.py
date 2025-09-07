from src.vacancy import Vacancy


def test_init_vacancy():
    """тест инициализации класса вакансий"""

    vacancy = Vacancy("cleaner", "cleaning of premises", 25000, "punctuality")

    assert vacancy.name == "cleaner"
    assert vacancy.responsibility == "cleaning of premises"
    assert vacancy.salary == 25000
    assert vacancy.requirement == "punctuality"


def test_invalid_init_vacancy():
    """тест валидации данных при инициализации"""

    try:
        vacancy = Vacancy(12342, "eihrbgv", 0, 3443)
    except ValueError:
        e = "value_error"

    assert e == "value_error"


def test_create_vacancy(vacancy1):
    """тест создания вакансии из словаря"""

    vacancy = Vacancy.create_vacancy(vacancy1)

    assert vacancy.name == "Менеджер по работе с клиентами (МЕРКАТОР)"
    assert (
        vacancy.responsibility == "Работа с клиентами. Контроль "
        "остатков инструмента на складе. "
        "Работа с дебиторской "
        "задолженностью. Отчетность в "
        "установленной форме (1С, Битрикс "
        "24)."
    )
    assert vacancy.salary == 2280000
    assert (
        vacancy.requirement == "Опыт в продажах или с клиентами. " "Грамотная речь. Активность. " "Коммуникабельность."
    )


def test_new_salary_vacancy(vacancy2):
    """тест изменения з/п в вакансии"""

    vacancy = Vacancy.create_vacancy(vacancy2)
    vacancy.salary = 30000

    assert vacancy.salary == 30000


def test_str_vacancy(vacancy1):
    """тест строкового вывода"""

    vacancy = Vacancy.create_vacancy(vacancy1)

    assert (
        str(vacancy) == "вакансия - Менеджер по работе с клиентами (МЕРКАТОР), зарплата = 2280000, ответственность: "
        "Работа с клиентами. Контроль остатков инструмента на складе. Работа с дебиторской задолженностью. "
        "Отчетность в установленной форме (1С, Битрикс 24)."
    )


def test_comparison_vacancy(vacancy1, vacancy2):
    """тест сравнения вакансий по з/п"""

    vac1 = Vacancy.create_vacancy(vacancy1)
    vac2 = Vacancy.create_vacancy(vacancy2)
    comparison1 = vac1 < vac2
    comparison2 = vac1 > vac2
    comparison3 = vac1 == vac2

    assert comparison1 == False
    assert comparison2 == True
    assert comparison3 == False
