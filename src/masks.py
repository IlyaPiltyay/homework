import logging
import os

if not os.path.exists("logs"):
    os.makedirs("logs")

logger = logging.getLogger("Masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(r"logs\logfile_masks.log")
file_formater = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def mask_card(card_number: str) -> str:
    """Функция которая маскерует номер карты"""
    logger.info("Начинается маскировка карты")
    if card_number.isdigit() and len(card_number) == 16:
        full_card_number = f"{card_number[:5]} {card_number[5:7]}{'*' * 2} {'*' * 4} {card_number[12:]}"
        return full_card_number
    else:
        logger.warning("Некорректный номер карты")
        return None


def mask_account(account_number: str) -> str:
    """Функиция которая маскерует счет"""
    if account_number.isdigit() and len(account_number) == 20:
        logger.info("Начинается маскировка счета")
        full_account_number = f"Счет {'*' * 2}{account_number[-4:]}"
        return full_account_number
    else:
        logger.warning("Некорректный номер счета")
        return None
