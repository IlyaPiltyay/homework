import unittest
from unittest.mock import mock_open, patch

from src.read_to_csv import read_csv_file


class TestReadCsvFile(unittest.TestCase):

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data="id;state;date;amount;currency_name;currency_code;from;to;description\n"
        "650703;EXECUTED;2023-09-05T11:30:32Z;16210;"
        "Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации\n",
    )
    def test_read_csv_file(self, mock_file):
        # Вызов вашей функции
        read_csv_file("fake_path.csv")

        # Проверка, что open был вызван с правильными аргументами
        mock_file.assert_called_once_with("fake_path.csv", encoding="utf8")


# Запуск тестов
if __name__ == "__main__":
    unittest.main()
