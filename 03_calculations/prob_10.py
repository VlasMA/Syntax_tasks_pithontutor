# Дано натуральное число. Найдите число десятков в его десятичной записи.

number = int(input('введи число: '))

result = number % 100 // 10
print(result)