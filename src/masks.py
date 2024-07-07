def mask_card(card_number: str) -> str | None:
    """Функция которая маскерует номер карты"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:5]} {card_number[5:7]}{"*" * 2} {"*" * 4} {card_number[12:]}"
    else:
        return None


def mask_account(account_number: str) -> str | None:
    """Функиция которая маскерует счет"""
    if account_number.isdigit() and len(account_number) == 20:
        return f"Счет {'*' * 2}{account_number[-4::]}"
    else:
        return None
