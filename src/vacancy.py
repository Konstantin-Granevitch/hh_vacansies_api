class Vacancy:
    """класс для работы с вакансиями"""

    __slots__ = ("name", "responsibility", "__salary", "requirement")
    name: str
    responsibility: str
    salary: int
    requirement: str

    def __init__(self, name, responsibility, salary, requirement):
        self.name = name
        self.responsibility = responsibility
        if salary == "" or salary is None or not (str(salary).isdigit()):
            salary = 0
        self.__salary = salary
        self.requirement = requirement

    @classmethod
    def create_vacancy(cls, vacancy: dict):
        """метод создания объекта вакансии из вложенного словаря"""

        salary = vacancy["salary"]
        salary_from = salary["from"] if salary and "from" in salary else 0

        obj = cls(
            vacancy["name"],
            vacancy["snippet"]["responsibility"],
            salary_from or salary,
            vacancy["snippet"]["requirement"],
        )

        return obj

    def __str__(self):
        """метод строкового представления объекта"""

        return f"вакансия - {self.name}, зарплата = {self.salary}, ответственность: {self.responsibility}"

    # сеттер и геттер для просмотра и изменения приватного метода с зарплатой
    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, new_salary: int):
        if new_salary == 0 or new_salary < 0 or new_salary == "" or new_salary is None:
            print("цена не должна быть равна или меньше 0")
        elif not (str(new_salary).isdigit()):
            print("цена должна быть числовым значением")
        else:
            self.__salary = new_salary

    # набор методов для сравнения вакансий по зарплате
    def __lt__(self, other):
        return self.__salary < other.__salary

    def __le__(self, other):
        return self.__salary <= other.__salary

    def __gt__(self, other):
        return self.__salary > other.__salary

    def __ge__(self, other):
        return self.__salary >= other.__salary

    def __eq__(self, other):
        return self.__salary == other.__salary

    def __ne__(self, other):
        return self.__salary != other.__salary


if __name__ == "__main__":

    vac1 = {
        "employment": {"id": "full", "name": "Полная занятость"},
        "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
        "has_test": False,
        "id": "93161709",
        "insider_interview": None,
        "is_adv_vacancy": False,
        "name": "Менеджер по работе с клиентами (МЕРКАТОР)",
        "premium": False,
        "professional_roles": [{"id": "70", "name": "Менеджер по продажам, менеджер по " "работе с клиентами"}],
        "published_at": "2024-02-13T17:06:04+0300",
        "relations": [],
        "response_letter_required": False,
        "response_url": None,
        "salary": {"currency": "RUR", "from": 2280000, "gross": True, "to": None},
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "show_logo_in_search": None,
        "snippet": {
            "requirement": "Опыт в продажах или с клиентами. " "Грамотная речь. Активность. " "Коммуникабельность.",
            "responsibility": "Работа с клиентами. Контроль "
            "остатков инструмента на складе. "
            "Работа с дебиторской "
            "задолженностью. Отчетность в "
            "установленной форме (1С, Битрикс "
            "24).",
        },
    }
    vac2 = {
        "employment": {"id": "full", "name": "Полная занятость"},
        "experience": {"id": "between3And6", "name": "От 3 до 6 лет"},
        "has_test": False,
        "id": "93254580",
        "insider_interview": None,
        "is_adv_vacancy": False,
        "name": "Машинист буровой установки RU-75",
        "premium": False,
        "professional_roles": [{"id": "63", "name": "Машинист"}],
        "published_at": "2024-02-15T08:00:54+0300",
        "relations": [],
        "response_letter_required": False,
        "response_url": None,
        "salary": {"currency": "RUR", "from": 228000, "gross": False, "to": 228000},
        "schedule": {"id": "flyInFlyOut", "name": "Вахтовый метод"},
        "show_logo_in_search": None,
        "snippet": {
            "requirement": "Квалификационное удостоверение "
            "машиниста буровой установки 5 разряда. "
            "Опыт работы на буровой установки "
            "RU-75., LM-75. Проведение текущих "
            "аварийных и...",
            "responsibility": "Бурение из буровых камер. Бурение "
            "согласно ГТН, умение подобрать "
            "породоразрушающий инструмент, "
            "монтаж на устье скважины.",
        },
    }

    vacancy1 = Vacancy.create_vacancy(vac1)
    vacancy2 = Vacancy.create_vacancy(vac2)
    vacancy3 = Vacancy("python developer", "python development", "kdjfbg", "development")

    print(vacancy1)
    print(vacancy3)

    vacancy1.salary = 100000  # изменение з/п в вакансии

    print(vacancy1.salary, vacancy2.salary)
    print(vacancy1 >= vacancy2)  # сравнение вакансий по з/п

    vac4 = {
        "accept_incomplete_resumes": False,
        "accept_temporary": False,
        "address": None,
        "adv_context": None,
        "adv_response_url": None,
        "alternate_url": "https://hh.ru/vacancy/93209001",
        "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=93209001",
        "archived": False,
        "area": {"id": "2759", "name": "Ташкент", "url": "https://api.hh.ru/areas/2759"},
        "contacts": None,
        "created_at": "2024-02-14T12:32:06+0300",
        "department": None,
        "employer": {
            "accredited_it_employer": False,
            "alternate_url": "https://hh.ru/employer/4621904",
            "id": "4621904",
            "logo_urls": {
                "240": "https://hhcdn.ru/employer-logo/3387666.png",
                "90": "https://hhcdn.ru/employer-logo/3387665.png",
                "original": "https://hhcdn.ru/employer-logo-original/736672.png",
            },
            "name": "«MY FREIGHTER» LLC",
            "trusted": True,
            "url": "https://api.hh.ru/employers/4621904",
            "vacancies_url": "https://api.hh.ru/vacancies?employer_id=4621904",
        },
        "employment": {"id": "full", "name": "Полная занятость"},
        "experience": {"id": "noExperience", "name": "Нет опыта"},
        "has_test": False,
        "id": "93209001",
        "insider_interview": None,
        "is_adv_vacancy": False,
        "name": "Бортпроводник",
        "premium": False,
        "professional_roles": [{"id": "159", "name": "Бортпроводник"}],
        "published_at": "2024-02-14T12:32:06+0300",
        "relations": [],
        "response_letter_required": False,
        "response_url": None,
        "salary": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "show_logo_in_search": None,
        "snippet": {
            "requirement": "Образование: среднее полное (11 "
            "классов), среднее специальное, высшее. "
            "Обязательное владение узбекским, "
            "русским и английским языками. "
            "Готовность работать согласно графику "
            "полетов. ",
            "responsibility": "Обеспечение безопасности на борту. "
            "Встреча и размещение пассажиров на "
            "борту. Инструктаж перед взлетом. "
            "Организация питания пассажиров во "
            "время полета. ",
        },
        "sort_point_distance": None,
        "type": {"id": "open", "name": "Открытая"},
        "url": "https://api.hh.ru/vacancies/93209001?host=hh.ru",
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
    }

    vacancy4 = Vacancy.create_vacancy(vac4)
    print(vacancy4)
