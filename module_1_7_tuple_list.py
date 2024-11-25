# list_0 = []
# list_0.extend("Bagration") # Если передать один аргумент, то метод выводит каждый элемент отдельно
# list_1 = ["Filya", "Mysya"]
# list_1.extend(["Gavrusha", True]) # Если поместить аргументы в [ ], то он их объединит
# list_01 = ["Яблоня", "Груша", "Слива", "Абрикос"]
# print(list_01); print("Черешня" not in list_01)
# list_01[0] = "Черешня"
# print(list_01)
# print("Черешня" not in list_01)
# print(list_0)
# print(list_1)
# print("Mysya" in list_1)
# list_002 = ["Филя", "Муся", "Гаврюша", "Кот"]
# print(list_002[0:3])

mail_1 = input("Enter you mail adress: ")
if "@" in mail_1 and mail_1.endswith((".com", ".ru", ".net")): #
    print(True)
else:
    print("Ошибка адреса")