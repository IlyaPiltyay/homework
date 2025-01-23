import unittest
from unittest.mock import patch

import pandas as pd

from src.read_to_exel import read_financial_operations


class TestReadFinancialOperations(unittest.TestCase):

    @patch("pandas.read_excel")
    def test_read_financial_operations(self, mock_read_excel):
        # Создаем тестовые данные
        test_data = {
            "id": [1, 2],
            "amount": [100, 200],
            "currency": ["USD", "EUR"],
            "description": ["Операция 1", "Операция 2"],
        }
        # Преобразуем в DataFrame
        test_df = pd.DataFrame(test_data)

        # Настраиваем мок, чтобы он возвращал наш DataFrame
        mock_read_excel.return_value = test_df

        # Путь к тестовому файлу - он не используется, так что можно указать любое значение
        test_file_path = "test.xlsx"

        # Вызываем функцию
        result = read_financial_operations(test_file_path)

        # Проверяем, что результат соответствует ожидаемому
        expected_result = [
            {"id": 1, "amount": 100, "currency": "USD", "description": "Операция 1"},
            {"id": 2, "amount": 200, "currency": "EUR", "description": "Операция 2"},
        ]
        self.assertEqual(result, expected_result)


# Запускаем тесты
if __name__ == "__main__":
    unittest.main()
