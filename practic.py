"""ВЫВОДИМ УНИКАЛЬНЫЕ ЭЛЕМЕНТЫ"""
fruits = ["apple", "banana", "orange", "apple"]
def unick_fruits(set_fruits):
    return list(set(set_fruits))
print(unick_fruits(fruits))



"""ВЫВОДИМ СРЕДНЕЕ ЗНАЧЕНИЕ"""
number = [1, 2, 3, 4, 5]
def aver_number(sor_list):
    new_list = round(sum(sor_list) / len(sor_list))
    return [el for el in sor_list if el < new_list]
print(aver_number(number))



"""ВЫВОДИМ ОТСОРТИРОВАННУЮ ЦЕНУ ПО УБЫВАНИЮ"""

def sorted_product_by_price(my_list):
    sorted_product = sorted(my_list, key=lambda x: x[1], reverse=True)
    return sorted_product
print(sorted_product_by_price([("apple", 2.5), ("banana", 3.5), ("orange", 1.5)]))


"""ВЫВОДИМ ОТСОРТИРОВАННЫЙ СПИСОК ПО ЖАНРУ"""
films = [
    {"title": "The Shawshank Redemption","genre": "Drama","director": "Frank Darabont",},
    {"title": "The Godfather", "genre": "Crime", "director": "Francis Ford Coppola"},
    {"title": "The Dark Knight", "genre": "Action", "director": "Christopher Nolan"},
]
genre = "Drama"
def filter_by_gener(values, filter_by):
    filtered_films = []
    for i in values:
        if i.get("genre") == filter_by:
            filtered_films.append(i)
    return filtered_films

print(filter_by_gener(films, genre))
