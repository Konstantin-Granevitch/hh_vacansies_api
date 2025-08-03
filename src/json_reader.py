import json
from pprint import pprint
from config import BASE_PATH


def json_reader(json_file: str) -> list[dict]:
    """
    функция принимает на вход имя файла и возвращает данные из него в виде списка словарей
    """

    try:
        with open(f"{BASE_PATH}/data/{json_file}") as f:
            list_data = json.load(f)
    except FileNotFoundError:
        list_data = []
    except json.JSONDecodeError:
        list_data = []
    except OSError:
        list_data = []

    return list_data


if __name__ == "__main__":
    file = json_reader("vacancies.json")
    pprint(file)
