import unittest
from unittest.mock import MagicMock, patch

from src.hh import HH


class TestHH(unittest.TestCase):
    """класс для тестирования класса HH"""

    @patch("requests.get")
    def test_connect_API(self, mock_get):
        """тест подключения к API"""

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"items": []}
        mock_get.return_value = mock_response
        hh = HH()
        response = hh._connect()

        mock_get.assert_called_once_with(
            "https://api.hh.ru/vacancies", headers={"User-Agent": "HH-User-Agent"}, params={"text": "", "per_page": 1}
        )

        self.assertEqual(response.status_code, 200)

    @patch("requests.get")
    def test_failed_connect(self, mock_get):
        """тест на подключение с ошибкой"""

        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        hh = HH()

        with self.assertRaises(Exception) as e:
            hh._connect()

        self.assertEqual(str(e.exception), "Ошибка подключения к API hh.ru: 404")

    @patch("requests.get")
    def test_get_vacancies(self, mock_get):
        """тест получения списка вакансий по ключевому слову"""

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "items": [{"id": "1", "name": "python developer"}, {"id": "2", "name": "java developer"}]
        }
        mock_get.return_value = mock_response
        hh = HH()
        hh.get_vacancies("developer", per_page=2)

        self.assertEqual(
            hh.vacancies, [{"id": "1", "name": "python developer"}, {"id": "2", "name": "java developer"}]
        )
