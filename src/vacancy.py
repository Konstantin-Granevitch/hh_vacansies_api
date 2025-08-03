class Vacancy:
    """класс для работы с вакансиями"""

    __slots__ = ("name", "responsibility", "salary", "requirement")
    name: str
    responsibility: str
    salary: int
    requirement: str

    def __init__(self, name, responsibility, salary, requirement):
        self.name = name
        self.responsibility = responsibility
        self.salary = salary
        self.requirement = requirement

    @classmethod
    def create_vacancy(cls, vacancy):
        """метод создания объекта вакансии из вложенного словаря"""

        obj = cls(
            vacancy["name"],
            vacancy["snippet"]["responsibility"],
            vacancy["salary"]["from"],
            vacancy["snippet"]["requirement"],
        )

        if vacancy["salary"]["from"] is None or vacancy["salary"]["from"] == "":  # проверка на отсутствие з/п
            obj.salary = 0

        return obj

    def __str__(self):
        """метод строкового представления объекта"""

        return f"вакансия-{self.name}, зарплата={self.salary}, ответственность: {self.responsibility}"

    def __lt__(self, other):
        """метод сравнения объектов по зарплате"""

        return self.salary < other.salary


if __name__ == "__main__":

    vac1 = {'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between1And3', 'name': 'От 1 года до 3 лет'},
            'has_test': False,
            'id': '93161709',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Менеджер по работе с клиентами (МЕРКАТОР)',
            'premium': False,
            'professional_roles': [{'id': '70',
                                    'name': 'Менеджер по продажам, менеджер по '
                                            'работе с клиентами'}],
            'published_at': '2024-02-13T17:06:04+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': {'currency': 'RUR',
                       'from': 228000,
                       'gross': True,
                       'to': None},
            'schedule': {'id': 'fullDay', 'name': 'Полный день'},
            'show_logo_in_search': None,
            'snippet': {'requirement': 'Опыт в продажах или с клиентами. '
                                       'Грамотная речь. Активность. '
                                       'Коммуникабельность.',
                        'responsibility': 'Работа с клиентами. Контроль '
                                          'остатков инструмента на складе. '
                                          'Работа с дебиторской '
                                          'задолженностью. Отчетность в '
                                          'установленной форме (1С, Битрикс '
                                          '24).'}
    }
    vac2 = {'employment': {'id': 'full', 'name': 'Полная занятость'},
            'experience': {'id': 'between3And6', 'name': 'От 3 до 6 лет'},
            'has_test': False,
            'id': '93254580',
            'insider_interview': None,
            'is_adv_vacancy': False,
            'name': 'Машинист буровой установки RU-75',
            'premium': False,
            'professional_roles': [{'id': '63', 'name': 'Машинист'}],
            'published_at': '2024-02-15T08:00:54+0300',
            'relations': [],
            'response_letter_required': False,
            'response_url': None,
            'salary': {'currency': 'RUR',
                       'from': 228000,
                       'gross': False,
                       'to': 228000},
            'schedule': {'id': 'flyInFlyOut', 'name': 'Вахтовый метод'},
            'show_logo_in_search': None,
            'snippet': {'requirement': 'Квалификационное удостоверение '
                                       'машиниста буровой установки 5 разряда. '
                                       'Опыт работы на буровой установки '
                                       'RU-75., LM-75. Проведение текущих '
                                       'аварийных и...',
                        'responsibility': 'Бурение из буровых камер. Бурение '
                                          'согласно ГТН, умение подобрать '
                                          'породоразрушающий инструмент, '
                                          'монтаж на устье скважины.'}

    }

    vacancy1 = Vacancy.create_vacancy(vac1)
    vacancy2 = Vacancy.create_vacancy(vac2)

    print(vacancy1)
    print(vacancy1.salary, vacancy2.salary)
    print(vacancy1 == vacancy2)
