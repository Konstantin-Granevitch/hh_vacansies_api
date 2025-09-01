import pytest


@pytest.fixture(scope="module")
def vacancy1():
    return {
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


@pytest.fixture(scope="module")
def vacancy2():
    return {
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
