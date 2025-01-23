import csv
import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger("read_to_csv")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(r"logs\\logfile_CSV.log")
file_formater = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def read_csv_file(path: str) -> list:
    """Функция принимает на вход путь к CSV файлу и возвращает данные с транзакциями."""
    transactions = []
    with open(path, encoding="utf8") as file:
        reader = csv.DictReader(file)
        logger.info(f"Чтение файла {path}")
        for row in reader:
            transactions.append(row)
    return transactions


path_to_csv = r"C:\Коды\pythonProject2\data\transactions.csv"
result = read_csv_file(path_to_csv)
print(result)
