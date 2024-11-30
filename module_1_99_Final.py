from statistics import mean
# Функция mean() принимает список, кортеж или набор данных, содержащий числовые значения, в качестве параметра и
# возвращает среднее значение элементов данных
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'})
average = []

for digits in grades:
    average.append(mean(digits))


print(dict(zip(students, average)))