import pytest

from src.widget import format_data, mask_account_card


@pytest.mark.parametrize(
    "first_inf, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 15968 37** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 71583 00** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 68319 82** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 89909 22** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 59994 14** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_elements(first_inf, expected_result):
    assert mask_account_card(first_inf) == expected_result


@pytest.mark.parametrize(
    "data,correct_data", [("2024-03-11T02:26:18.671407", "11.03.2024")]
)
def test_data(data, correct_data):
    assert format_data(data) == correct_data
