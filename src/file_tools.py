import json

from abc import ABC, abstractmethod
from json import JSONDecodeError
from typing import Any
from pprint import pprint

from config import BASE_PATH


class Tools(ABC):
    """абстрактный класс для классов работающих с файлами"""

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def write_file(self, data):
        pass

    @abstractmethod
    def append_file(self, data):
        pass


class Json_Tool(Tools):
    """класс для работы с json-файлами"""

    file_name: str

    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        """метод чтения файла"""

        try:
            with open(f"{BASE_PATH}/data/{self.file_name}", encoding='utf-8') as f:
                result = json.load(f)
        except FileNotFoundError:
            result = "ошибка файл не найден, проверьте путь и имя файла"
        except JSONDecodeError:
            result = "файл не читаем"

        return result

    def write_file(self, data: Any):
        """метод записи файла"""

        with open(f"{BASE_PATH}/data/{self.file_name}", "w", encoding='utf-8') as f:
            json.dump(data, f)

    def append_file(self, data: Any):
        """метод записи файла"""

        with open(f"{BASE_PATH}/data/{self.file_name}", "a", encoding='utf-8') as f:
            json.dump(data, f)


if __name__ == "__main__":
    j_file = Json_Tool("vacancies.json")
    pprint(j_file.read_file())

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

    j_file2 = Json_Tool("user_file.json")
    j_file2.write_file(vac1)
    j_file2.append_file(vac1)
