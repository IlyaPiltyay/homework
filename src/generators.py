from typing import Dict, Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator[str]:
    """возвращение id со статусом USD"""
    # try:
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
    # except StopIteration:
    # if transaction not in transactions:
    # return 'валюты нет.'


def transaction_descriptions(transactions: Dict) -> Iterator[str]:
    """Типы операций"""
    try:
        for transaction in transactions:
            yield transaction["description"]
    except StopIteration:
        if transaction == []:
            return 'нет транзакций.'


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров кард в заданном параметре"""

    for number in range(start, stop + 1):
        number_str = f"{number:016}"
        formatted_number = (
            f"{number_str[:4]} {number_str[4:8]} {number_str[8:12]} {number_str[12:]}"
        )
        yield formatted_number


