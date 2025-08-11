import requests

from abc import ABC, abstractmethod


class Parser(ABC):
    """абстрактный класс для создания классов с API"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HH(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            vacancies = response.json()["items"]
            self.vacancies.extend(vacancies)
            self.__params["page"] += 1

    def __str__(self):
        return f"список вакансий: {self.vacancies}"

if __name__ == "__main__":
    h1 = HH
    h1.load_vacancies = "developer"
    print(h1())