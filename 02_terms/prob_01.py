# Даны два целых числа. Выведите значение наименьшего из них.

num_1 = int(input('Введи перове число: '))
num_2 = int(input('Введи второе число: '))

if num_1 < num_2:
    print(f'{num_1} меньше')
elif num_2 < num_1:
    print(f'{num_2} меньше')
else:
    print('они равны')