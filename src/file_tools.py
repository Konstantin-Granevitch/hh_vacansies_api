from abc import ABC, abstractmethod
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

    file_name: str
    mode: str

    def __init__(self, file_name, mode="r"):
        self.file_name = f"{BASE_PATH}/data/{file_name}"
        self.mode = mode

    def __enter__(self):
        self.f = open(self.file_name, self.mode)
        return self.f

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()


if __name__ == "__main__":
    with Json_Tool("vacancies.json", "r") as f:
        print(f.read())
