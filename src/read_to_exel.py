import logging
import os

import pandas as pd

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger("read_to_Exel")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(r"logs\\logfile_Exel.log")
file_formater = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def read_financial_operations(file_path: str) -> list:
    """Функция принимает на вход путь к Exel файлу
    и возвращает данные с транзакциями."""
    try:
        logger.info("Чтение данных из Excel-файла ")
        data = pd.read_excel(file_path, engine="openpyxl")
        print(data.head())
        logger.info(f"Объем файла{data.shape}")
        logger.info("Преобразование данных в список словарей")
        operations = data.to_dict(orient="records")
        return operations
    except Exception as e:
        logger.error(f"Произошла ошибка при чтении файла: {e}")
        print(f"Произошла ошибка при чтении файла: {e}")
        return []


file_path = r"C:\Коды\pythonProject2\data\transactions_excel.xlsx"
financial_operations = read_financial_operations(file_path)
list_of_transaction = []
for operation in financial_operations:
    list_of_transaction.append(operation)
    print(list_of_transaction)
