from abc import ABC, abstractmethod
from pprint import pprint

import requests


class Parser(ABC):
    """абстрактный класс для создания классов с API"""

    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def get_vacancies(self, keyword, per_page):
        pass


class HH(Parser):
    """класс работающий с API hh.ru"""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "per_page": 1}
        self.vacancies = []

    def _connect(self):
        """Приватный метод подключения к API hh.ru, проверяющий статус-код ответа."""

        response = requests.get(self.__base_url, headers=self.__headers, params=self.params)

        if response.status_code != 200:
            raise Exception(f"Ошибка подключения к API hh.ru: {response.status_code}")

        return response

    def get_vacancies(self, keyword: str, per_page: int = 20):
        """
        Метод получения данных о вакансиях по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий.
        :param per_page: Количество вакансий на странице (по умолчанию 20).
        :return: Список вакансий.
        """

        # Формируем параметры для запроса
        self.params = {"text": keyword, "per_page": per_page}

        # Запрос на получение вакансий
        response = self._connect()

        if response.status_code == 200:
            self.vacancies = response.json().get("items", [])
        else:
            print(f"Ошибка при получении данных: {response.status_code}")


if __name__ == "__main__":
    client = HH()
    client.get_vacancies("python")
    pprint(client.vacancies)
