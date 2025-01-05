import requests
import os
from src.Utils import read_file
from dotenv import load_dotenv


load_dotenv('.env')
API_KEY = os.getenv('API_KEY')


def operation_code(transactions):
    """Функция принимает на вход транзакции и возвращает сумму транзакций в RUB."""
    rub_sum = 0
    usd_sum = 0
    eur_sum = 0
    for trans in transactions:
        currency_code = trans.get("operationAmount", {}).get("currency", {}).get("code")
        amount = trans.get("operationAmount", {}).get("amount")

        # Сумма для RUB и USD
        if currency_code == "RUB":
            rub_sum += float(amount)
        elif currency_code == "USD":
            usd_sum += float(amount)
        elif currency_code == "EUR":
            eur_sum += float(amount)
    print(f"Сумма транзакций в RUB: {round(rub_sum):}")
    print(f"Сумма транзакций в USD: {round(usd_sum):}")
    print(f"Сумма транзакций в EUR: {round(eur_sum):}")
    total_converted = usd_sum + eur_sum

    url = f"https://api.apilayer.com/currency_data/convert?to=RUB&from=USD&amount={total_converted}"
    headers = {"apikey": API_KEY}
    response = requests.get(url, headers=headers)
    result = response.json()
    converted_sum = result.get("result", 0)
    return f"Конвертированная сумма из USD в RUB: {converted_sum}"


PATH_TO_FILE = r"C:\Коды\pythonProject2\data\operations.json"
transactions = read_file(PATH_TO_FILE)
converted = operation_code(transactions)
print(converted)


