# Условие
# Даны три целых числа. Выведите значение наименьшего из них.

n_1 = int(input('enter 1 number: '))
n_2 = int(input('enter 2 number: '))
n_3 = int(input('enter 3 number: '))
n_4 = int(input('enter 4 number: '))
n_5 = int(input('enter 5 number: '))
n_6 = int(input('enter 6 number: '))

min = n_1

if n_2 < min: min = n_2
if n_3 < min: min = n_3
if n_4 < min: min = n_4
if n_5 < min: min = n_5
if n_6 < min: min = n_6

print(f'minimal - {min}')
