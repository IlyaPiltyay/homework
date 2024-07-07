import os

from src.masks import mask_account,mask_card


def mask_account_cart(type_and_number_cart: str) -> str:


current_directory = os.getcwd()
print(current_directory)

if __name__ == "__main__":
    print(mask_card("7000792289606361"))
    print(mask_account("73654108430135874305"))


cart_and_account_numbers = """ Maestro 1596837868705199
Счет 64686473678894779589
MasterCard 7158300734726758
Счет 35383033474447895560
Visa Classic 6831982476737658
Visa Platinum 8990922113665229
Visa Gold 5999414228426353
Счет 73654108430135874305 """

date = "2018-07-11T02:26:18.671407"
