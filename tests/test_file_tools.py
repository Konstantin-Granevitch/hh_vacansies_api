from src.file_tools import JSON_Tool


def test_json_get_data_empty(mocker):
    """тестирование получения данных из пустого JSON файла"""

    json_test_data = []
    mocker.patch("src.file_tools.JSON_Tool.get_data", return_value=json_test_data)
    json_data = JSON_Tool()
    data_file = json_data.get_data()

    assert data_file == []


def test_json_get_data(mocker):
    """тестирование получения данных из JSON файла"""

    json_test_data = ["data1", "data2", "data3"]
    mocker.patch("src.file_tools.JSON_Tool.get_data", return_value=json_test_data)
    json_data = JSON_Tool()
    data_file = json_data.get_data()

    assert data_file == ["data1", "data2", "data3"]


def test_json_add_data(mocker):
    """тестирование добавления данных в JSON файл"""

    json_test_data1 = ["data1", "data2"]
    json_test_data2 = ["data3", "data4"]
    mocker.patch("src.file_tools.JSON_Tool.get_data", return_value=json_test_data1)
    json_data = JSON_Tool()
    mock = mocker.patch("src.file_tools.JSON_Tool.add_data", return_value=json_test_data2)
    json_data.add_data(json_test_data2)

    mock.assert_called_once_with(json_test_data2)


def test_json_delete_data(mocker):
    """тестирование удаления данных из JSON файла"""

    json_test_data = ["data1", "data2"]
    mocker.patch("src.file_tools.JSON_Tool.get_data", return_value=json_test_data)
    json_data = JSON_Tool()
    mock = mocker.patch("src.file_tools.JSON_Tool.delete_data", return_value=json_test_data)
    json_data.delete_data(json_test_data)

    mock.assert_called_once_with(json_test_data)
