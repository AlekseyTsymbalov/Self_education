list_0 = []
list_0.extend("Bagration") # Если передать один аргумент, то метод выводит каждый элемент отдельно
list_1 = ["Filya", "Mysya"]
list_1.extend(["Gavrusha", True]) # Если поместить аргументы в [ ], то он их объединит
print(list_0)
print(list_1)
print("Mysya" in list_1)

mail_1 = "AlekseyTsymbalov@yahoo.com"
if "@" in mail_1:
    print(True)
else:
    print("Ошибка адреса")