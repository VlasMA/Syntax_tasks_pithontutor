# Обувная фабрика собирается начать выпуск элитной модели ботинок.
#  Дырочки для шнуровки будут расположены в два ряда, расстояние между рядами равно a,
#  а расстояние между дырочками в ряду b. Количество дырочек в каждом ряду равно N. 
# Шнуровка должна происходить элитным способом “наверх, по горизонтали в другой ряд, 
# наверх, по горизонтали и т.д.” (см. рисунок). Кроме того, чтобы шнурки можно было завязать элитным бантиком, 
# длина свободного конца шнурка должна быть l. Какова должна быть длина шнурка для этих ботинок?

# Программа получает на вход четыре натуральных числа a, b, l и N - именно в таком порядке - и должна вывести одно число - искомую длину шнурка.

a = int(input('a, расстояние между рядами: '))
b = int(input('b, расстояние между дырочками в ряду: '))
l = int(input('l, длина свободного конца шнурка: '))
N = int(input('N, koличество дырочек в каждом ряду: '))



l1 = (N * a) + ((N - 1) * b)
l2 = ((N - 1) * b) + ((N - 1) * a)
l3 = l * 2
l4 = l1 + l2 + l3
print(l4)