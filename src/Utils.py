import json
import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger("Utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(r"logs\\logfile.log")
file_formater = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def read_file(path: str):
    """Функция принимает на вход путь к JSON файлу
    и возвращает данные с транзакциями."""
    try:
        logger.info(f"Попытка прочитать файл: {path}")
        with open(path, encoding="utf8") as file:
            operation = json.load(file)
        if not isinstance(operation, list):
            logger.info("Объект не найден")
            return []
        return operation
    except FileNotFoundError as f:
        logger.error(f"Файл не найден: {f}")
        print(f"Error: {f}")
        return []
    except json.JSONDecodeError as f:
        logger.error(f"Ошибка декодирования JSON: {f}")
        print(f"Error: {f}")
        return []
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        print(f"Error: {e}")
        return []


PATH_TO_FILE = r"C:\Коды\pythonProject2\data\operations.json"
print(read_file(PATH_TO_FILE))
