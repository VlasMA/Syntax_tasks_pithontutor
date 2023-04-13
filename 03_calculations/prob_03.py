# Дано положительное действительное число X. Выведите его дробную часть.
import math

num = float(input('введи дробное число: '))


if num > 0: number = math.floor(num)
if num < 0: number = math.ceil(num)


result = num - number
print(round(result, 10))


