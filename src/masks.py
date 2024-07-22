def mask_card(card_number: str) -> str:
    """Функция которая маскерует номер карты"""
    if card_number.isdigit() and len(card_number) == 16:
        full_card_number = f"{card_number[:5]} {card_number[5:7]}{'*' * 2} {'*' * 4} {card_number[12:]}"
        return full_card_number
    else:
        return "Некорректный номер карты"


def mask_account(account_number: str) -> str:
    """Функиция которая маскерует счет"""
    if account_number.isdigit() and len(account_number) == 20:
        full_account_number = f"Счет {'*' * 2}{account_number[-4:]}"
        return full_account_number
    else:
        return "Некорректный номер счета"
