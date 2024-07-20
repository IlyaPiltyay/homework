import pytest

from src.masks import mask_account, mask_card


@pytest.mark.parametrize(
    "full_number, expected",
    [
        ("1596837868705199", "15968 37** **** 5199"),
        ("7158300734726758", "71583 00** **** 6758"),
        ("6831982476737658", "68319 82** **** 7658"),
        ("8990922113665229", "89909 22** **** 5229"),
        ("5999414228426353", "59994 14** **** 6353"),
    ],
)
def test_mask_number(full_number, expected):
    assert mask_card(full_number) == expected


@pytest.mark.parametrize(
    "full_card, expected",
    [
        ("73654108430135874305", "Счет **4305"),
        ("64686473678894779589", "Счет **9589"),
        ("35383033474447895560", "Счет **5560"),
    ],
)
def test_mask_account(full_card, expected):
    assert mask_account(full_card) == expected
