import json


def read_file(path: str):
    """Функция принимает на вход путь к JSON файлу
    и возвращает данные с транзакциями."""
    try:
        with open(path, encoding="utf8") as file:
            operation = json.load(file)
        if not isinstance(operation, list):
            return []
        return operation
    except FileNotFoundError as f:
        print(f"Error: {f}")
        return []
