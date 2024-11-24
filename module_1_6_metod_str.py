my_string = input("Введи что-нибудь: ")

print(f"Длина введённой строки: ",len(my_string))
print(f"Строка вся заглавная: ",my_string.upper())
print(f"Строка вся строчная: ",my_string.lower())
print(f"Строка вся без пробелов: ",my_string.replace(" ", ""))
print(f"Первый символ строки: ",my_string[0])
print(f"Последний символ строки: ",my_string[-1])