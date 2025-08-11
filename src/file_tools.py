import json

from abc import ABC, abstractmethod
from src.vacancy import Vacancy
from json import JSONDecodeError
from typing import Any

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

        result = []
        list_vacancies = []

        try:
            with open(f"{BASE_PATH}/data/{self.file_name}", encoding='utf-8') as f:
                json_data = json.load(f)
            for vacancy in json_data["items"][0:]:
                result.append(Vacancy.create_vacancy(vacancy))
        except FileNotFoundError:
            print("ошибка файл не найден, проверьте путь и имя файла")
        except JSONDecodeError:
            print("файл не читаем")

        return result

    def write_file(self, data: Any):
        """метод записи файла"""

        try:
            with open(f"{BASE_PATH}/data/{self.file_name}", "w", encoding='utf-8') as f:
                json.dump(data, f)
        except JSONDecodeError:
            print("ошибка в кодировке данных, проверьте ошибки")

    def append_file(self, data: Any):
        """метод записи файла"""
        try:
            with open(f"{BASE_PATH}/data/{self.file_name}", "a", encoding='utf-8') as f:
                json.dump(data, f)
        except JSONDecodeError:
            print("ошибка в кодировке данных, проверьте ошибки")

    def __delitem__(self, key):
        """метод для удаления информации в классе по ключу"""
        pass
        #if key in self


if __name__ == "__main__":
    j_file = Json_Tool("vacancies.json")
    list_vac = j_file.read_file()
    print(list_vac)
