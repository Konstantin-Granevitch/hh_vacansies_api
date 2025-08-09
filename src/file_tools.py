import json

from abc import ABC, abstractmethod
from json import JSONDecodeError

from config import BASE_PATH


class Tools(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __enter__(self):
        pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


class Json_Tool(Tools):
    """класс для работы с файлами"""

    data: str
    file_name: str

    def __init__(self, data, file_name):
        self.data = data
        self.file_name = file_name

    def json_read(self, file_name):
        try:
            with open(f"{BASE_PATH}/data/{self.file_name}") as f:
                file_data = json.load(f)
        except FileNotFoundError as e:
            print(e)
            file_data = {}
        except JSONDecodeError as e:
            print(e)
            file_data = {}
        return file_data


if __name__ == "__main__":
    print(Json_Tool.json_read(file_name="vacancies.json"))
