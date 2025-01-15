import datetime

from src.masks import mask_account, mask_card

example_data = """ Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305 """


def mask_account_card(input_str: str) -> str:
    """Функция маскирует номер счета/карты,оставляя название название"""
    if "Счет" in input_str:
        return mask_account(input_str.split()[-1])
    else:
        new_card = mask_card(input_str.split()[-1])
        return input_str.replace(input_str.split()[-1], new_card)


if __name__ == "__main__":
    print(mask_account_card("Maestro 1596837868705199"))
    print(mask_account_card("MasterCard 7158300734726758"))
    print(mask_account_card("Visa Classic 6831982476737658"))
    print(mask_account_card("Visa Platinum 8990922113665229"))
    print(mask_account_card("Visa Gold 5999414228426353"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(mask_account_card("Счет 64686473678894779589"))
    print(mask_account_card("Счет 35383033474447895560"))

date_str = "2024-03-11T02:26:18.671407"


def format_data(date_str):
    """Функция преобразование строки в дату"""
    date_obj = datetime.datetime.fromisoformat(date_str)
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date


print(format_data(date_str))
