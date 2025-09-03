import json
import os
from abc import ABC, abstractmethod
from json import JSONDecodeError
from pprint import pprint
from typing import Any

from config import BASE_PATH


class Tools(ABC):
    """абстрактный класс для классов работающих с файлами"""

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def add_data(self, data):
        pass

    @abstractmethod
    def delete_data(self, data):
        pass


class JSON_Tool(Tools):
    """класс для работы с JSON файлами"""

    filename: str

    def __init__(self, filename="user_file.json"):
        self.__filename = f"{BASE_PATH}/data/{filename}"  # Приватный атрибут для имени файла

    def get_data(self) -> Any:
        """метод получения данных из JSON-файла."""

        if not os.path.exists(self.__filename):
            return []  # Возвращает пустой список, если файл не существует
        try:
            with open(self.__filename, encoding="utf-8") as f:
                return json.load(f)  # Загружает и возвращает данные из файла
        except JSONDecodeError:
            return []  # Возвращает пустой список, если файл не читается

    def add_data(self, data: dict):
        """метод записи данных в JSON-файл, предотвращая дублирование."""

        existing_data = self.get_data()  # Получаем существующие данные

        if data not in existing_data:  # Проверка на дублирование
            existing_data.append(data)  # Добавляем новые данные
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump(existing_data, f, ensure_ascii=False, indent=4)  # Сохраняем обновленные данные в файл

    def delete_data(self, data: dict):
        """метод удаления данных из JSON-файла, если они существуют."""

        existing_data = self.get_data()  # Получаем существующие данные

        if data in existing_data:  # Проверяем, есть ли данные для удаления
            existing_data.remove(data)  # Удаляем данные
            with open(self.__filename, "w", encoding="utf-8") as f:
                json.dump(existing_data, f, ensure_ascii=False, indent=4)  # Сохраняем обновленные данные в файл


if __name__ == "__main__":
    # handler = JSON_Tool()
    # vacancy_data = {
    #     "employment": {"id": "full", "name": "Полная занятость"},
    #     "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
    #     "has_test": False,
    #     "id": "93161709",
    #     "insider_interview": None,
    #     "is_adv_vacancy": False,
    #     "name": "Менеджер по работе с клиентами (МЕРКАТОР)",
    #     "premium": False,
    #     "professional_roles": [{"id": "70", "name": "Менеджер по продажам, менеджер по " "работе с клиентами"}],
    #     "published_at": "2024-02-13T17:06:04+0300",
    #     "relations": [],
    #     "response_letter_required": False,
    #     "response_url": None,
    #     "salary": {"currency": "RUR", "from": 2280000, "gross": True, "to": None},
    #     "schedule": {"id": "fullDay", "name": "Полный день"},
    #     "show_logo_in_search": None,
    #     "snippet": {
    #         "requirement": "Опыт в продажах или с клиентами. " "Грамотная речь. Активность. " "Коммуникабельность.",
    #         "responsibility": "Работа с клиентами. Контроль "
    #         "остатков инструмента на складе. "
    #         "Работа с дебиторской "
    #         "задолженностью. Отчетность в "
    #         "установленной форме (1С, Битрикс "
    #         "24).",
    #     },
    # }
    #
    # # Добавление вакансии
    # print("Добавление вакансии...")
    # handler.add_data(vacancy_data)
    #
    # # Получение данных из файла
    # print("Получение данных из файла...")
    # data = handler.get_data()
    # print(data)
    #
    # # Удаление вакансии
    # print("Удаление вакансии...")
    # handler.delete_data(vacancy_data)
    #
    # # Получение данных из файла после удаления
    # print("Получение данных после удаления...")
    # data_after_deletion = handler.get_data()
    # print(data_after_deletion)
    pprint(JSON_Tool("vacancies.json").get_data())
