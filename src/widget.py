import datetime

from src.masks import mask_account, mask_card

example_data = """ Maestro 1596837868705199
Счет 64686473678894779589#
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305 """


def process_input(input_str: str) -> str:
    if "Счет" in input_str:
        return mask_account(input_str.split()[1])
    else:
        new_card = mask_card(input_str.split()[-1])
        return input_str.replace(input_str.split()[-1], new_card)


if __name__ == "__main__":
    print(process_input("Maestro 1596837868705199"))
    print(process_input("MasterCard 7158300734726758"))
    print(process_input("Visa Classic 6831982476737658"))
    print(process_input("Visa Platinum 8990922113665229"))
    print(process_input("Visa Gold 5999414228426353"))
    print(process_input("Счет 73654108430135874305"))
    print(process_input("Счет 64686473678894779589"))
    print(process_input("Счет 35383033474447895560"))
    print(datetime.datetime(2024, 3, 11))
