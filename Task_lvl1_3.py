# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
from typing import Counter


students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

students_count = {}
for student in students:
    name = student.get('first_name')
    if name not in students_count:
        students_count[name] = 1
    else:
      students_count[name] += 1
for name in students_count:
    print(f'{name}: {students_count.get(name)}')



# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]

students_count = {}
for student in students:
    name = student.get('first_name')
    if name not in students_count:
        students_count[name] = 1
    else:
        students_count[name] += 1
count = 0
for name in students_count:
    student_value = students_count.get(name)
    if student_value > count:
        count += 1
        student = name
print(f'Самое частое имя среди учеников: {student}')

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]

class_number = 0
for school_class in school_students:
    max_count = 0
    class_number += 1
    for student in school_class:
        name = student.get('first_name')
        count = students.count({'first_name': f'{name}'})
        if count > max_count:
            max_count = count
            frequent_name = name
    print(f'Самое частое имя в классе {class_number}: {frequent_name}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

for school_class in school:
    boys = 0
    girls = 0
    class_number = school_class.get('class')
    for students in school_class.get('students'):
        name = students.get('first_name')
        if is_male.get(name):
            boys += 1
        else:
            girls += 1
    print(f'В классе {class_number} {girls} девочки и {boys} мальчика ')

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
max_boys = 0
max_girls = 0
for school_class in school:
    boys = 0
    girls = 0
    class_number = school_class.get('class')
    for students in school_class.get('students'):
        name = students.get('first_name')
        if is_male.get(name):
            boys += 1
        else:
            girls += 1
    if max_boys < boys:
        max_boys = boys
        boys_answer = f'Больше всего мальчиков в классе {class_number}'
    if max_girls < girls:
        max_girls = girls
        girls_answer = f'Больше всего девочек в классе {class_number}'

print(f'{boys_answer}\n{girls_answer}')


# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a