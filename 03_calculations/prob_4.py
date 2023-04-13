# Дано положительное действительное число X. Выведите его первую цифру после десятичной точки.
import math

num = float(input('введи дробное число: '))


if num > 0: number = math.floor(num)
# print(num)
if num < 0: number = math.ceil(num)
# print(num)


result = int((num - number)*10)

print(round(result))