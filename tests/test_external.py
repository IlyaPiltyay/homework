
import os
from unittest.mock import patch
from src.external_api import operation_code  # Измените на актуальный путь к вашему модулю


@patch('requests.get')
@patch('src.Utils.read_file')
def test_operation_code(mock_read_file, mock_requests_get):
    # Пример транзакций
    mock_transactions = [
        {
            "operationAmount": {
                "currency": {"code": "RUB"},
                "amount": "100.00"
            }
        },
        {
            "operationAmount": {
                "currency": {"code": "USD"},
                "amount": "50.00"
            }
        },
        {
            "operationAmount": {
                "currency": {"code": "EUR"},
                "amount": "20.00"
            }
        }
    ]

    # Настройка мока для read_file
    mock_read_file.return_value = mock_transactions

    # Настройка мока для requests.get
    mock_requests_get.return_value.json.return_value = {"result": 5000.0}  # Мокаем ответ с API

    # Вызываем тестируемую функцию
    result = operation_code(mock_transactions)

    # Проверка результата
    assert result == "Конвертированная сумма из USD в RUB: 5000.0"

    # Ожидаемая сумма USD и EUR
    expected_usd_sum = 50.0
    expected_eur_sum = 20.0
    total_converted = expected_usd_sum + expected_eur_sum

    # Проверка, что requests.get был вызван один раз с правильными параметрами
    expected_url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from=USD&amount={total_converted}"

    mock_requests_get.assert_called_once_with(expected_url, headers={"apikey": os.getenv('API_KEY')})

