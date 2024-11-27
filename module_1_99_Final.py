from statistics import mean
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'} # students_sort = sorted(students)
grades_digits_0 = mean(grades[0])
grades_digits_1 = mean(grades[1])
grades_digits_2 = mean(grades[2])
grades_digits_3 = mean(grades[3])
grades_digits_4 = mean(grades[4])
average_digits = [*[grades_digits_0], *[grades_digits_1], *[grades_digits_2], *[grades_digits_3], *[grades_digits_4]]
finaly = dict(zip(students, average_digits))
print(finaly)
# Функция mean() принимает список, кортеж или набор данных, содержащий числовые значения, в качестве параметра и
# возвращает среднее значение элементов данных