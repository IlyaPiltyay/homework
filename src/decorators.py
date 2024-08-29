from functools import wraps
from typing import Any, Callable


def log(filename: Any) -> Callable:
    """Логирует вызов функции и ее результат в файл или в консоль
    filename: Путь к файлу для записи логов. Если не указан, логи выводятся в консоль.
    :rtype: object
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok.")

            except Exception as ex:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error - {ex}.Inputs {args},{kwargs}")
                else:
                    print(f"{func.__name__} error - {ex}.Inputs {args},{kwargs}")
            return result
        return wrapper
    return decorator

@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
