from typing import Any

list_of_id = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(information: list, state="EXECUTED") -> list:
    """Функция сортитрует значение ключа"""
    filtered_exe = []
    for i in information:
        if i.get("state") == state:
            filtered_exe.append(i)
    return filtered_exe


def sort_by_date(
        sorted_date: list[dict[str, Any]], reverse=True
) -> list[dict[str, Any]]:
    """функция сортирует дату"""
    sorted_time = sorted(sorted_date, key=lambda x: x.get("date", ""), reverse=reverse)
    return sorted_time


print(filter_by_state(list_of_id))
print(sort_by_date(list_of_id))
