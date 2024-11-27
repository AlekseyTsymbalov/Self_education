phone_book = {"Irina": 89616930833, "Alexsey": 89963576864, "Sasha": 89692915867}
print(phone_book)
# print(phone_book["Irina"]) # Выводим значение по ключу
# phone_book["Irina"] = 89176403198 # Произвели замену значения по ключу
# phone_book["Filya"] = 89608841102 # Если обратиться к несуществующему ключу, то он появится в словаре
# print(phone_book)
# del phone_book["Alexsey"] # Оператором del удалили значение по ключу
# print(phone_book)
# phone_book.update({"Alex": 89054348747, "Sanches": 89050643346}) # Метод добавления ключ-значение
# print(phone_book)
# print(phone_book.get("Irina")) # Выводит значение по умолчания ключа. ВАЖНО вернёт None если ключа нет. Новый не создаст
# # print(phone_book["Kamila"]) будет ошибка, такого ключа нет А если get
# print(phone_book.get("Kamila")) # Просто укажет что None, ошибки не будет ИЛИ
# print(phone_book.get("Kamila", "Такого ключа нет!")) # Выводит текст справа.
# print(phone_book)
# #phone_book.pop("Alex") # Извлекает из словаря ключ-значение и сохраняет его. В последствии можно использовать.
# print(phone_book)
# name_pop = phone_book.pop("Alex")
# print(phone_book)
# print(name_pop)
# print(phone_book.keys()) # Позволяет получить коллекцию ключей в нашем словаре
# print(phone_book.values()) # Позволяет вернуть значения из словаря
# print(phone_book.items(),"\n") # Позволяет вернуть парные ключ-значение
# user_login = {"Irina": 9051945} # --- ?
# print("set - Множества: \n")
# set_01 = {1, 2, 3, 4, 9, 2, 11, 4}
# print(set_01)
# set_02 = {1, 2, 3, 4, 5, 1, 2, 3, "String", True, (1, 2, 3), "String", (1, 2, 3)}
# print(set_02) # print(set_02[0]) обращение по индексу выдаст ошибку.
# list_009 = [1, 1, 1, 1, 2, 2, 3, 3, 2, 3]
# # print(set(list_009)) # Команда set преобразовала список во множество.
# list_009 = set(list_009) # Или так полная замена
# print(list_009, "\n")
# print("Метод : discard")
# print(list_009.discard(1)) # Не выдаёт ошибки если обратится к несуществующему элементу
# print(list_009, "\n")
# print("Метод : add")
# print(list_009.add(4)) # Добавляет один элемент
# print(list_009)
# list_009.update((79, 15, 99)) # Добавляет несколько элементов
# print(list_009)
#
# print(None)

# print("Работа со словарём!")
# my_dict = {"Filya": 2019, "Mysya": 2011, "Gavrusha": 1998}
# print("Изначальный словарь: ", my_dict)
# print(f"Существующее значение: {my_dict["Filya"]}")
# print(f"Несуществующее значение: {my_dict.get("Barsik"), "Такого ключа Barsik нет"}")
# delet_name = my_dict.pop("Gavrusha")
# print(f"Deleted value: {delet_name}")
# my_dict.update({"Murka": 1994, "Pirat": 1993})
# print("Изменённый словарь: ", my_dict)
#
# print(None)
#
print("Работа с множеством!")
my_set = {1, "Яблоко", 42.314,1, "Яблоко", 42.314,} # Сохраняет неповторяющиеся значения
print("Set: ", my_set)
my_set.add("Черешня")
my_set.update((5.6, 99, 15))
my_set.discard(15) # Извлечь указанное значение
print("Изменённое множество: ", my_set)

bus_ = 17, 99, 78
my_set.add(bus_)
print(my_set)
my_set.add((105, 210))
print(my_set)
# Принимает один аргумент update
my_set.update([777, 999, 444]) # Метод этот добавляет всё по элементно... Список или кортеж не добавить через update
print(my_set)