tuple_1 = 1, 7, 3, 4    # Всё это один и тот же кортеж
tuple_2 = (1, 7, 3, 4)  # Всё это один и тот же кортеж
tuple_3 = tuple([1, 7, 3, 4])   # Всё это один и тот же кортеж
print(tuple_1); print(tuple_2); print(tuple_3)
print(tuple_3)
tuple_9 = ([2, 5, 9], 18)
tuple_4 = ([1, 2, 3], [23, 17, 99], 9) # Создаём кортеж внутри которого будет два списка
print(tuple_4)
tuple_4[1][2] = 130 # Внесли изменение по индексу в список 1 картежа
print(tuple_4)
tuple_4 = ([1, 2, 3], [23, 17, 99], 9) + (47, 95)
print(tuple_4)
tuple_5 = (7, 9) * 2
print(tuple_5)
tuple_4[0][2] = "Z" # Изменил значения списка в кортеже по индексу ещё и другого типа
print(tuple_4)

immutable_var = 47, 95,"True", False # Неизменяемые данные в нём
print(immutable_var)

mutable_list = [47, 95,"True", False]
print(mutable_list)
mutable_list[3] = "Irisha"
mutable_list.append(157)
print(mutable_list)