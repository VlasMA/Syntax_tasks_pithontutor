# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.
import math

a = int(input('1 katet: '))
b = int(input('2 katet: '))

c = math.sqrt((a**2)+(b**2))

print(c)