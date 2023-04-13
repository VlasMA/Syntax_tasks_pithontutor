# Дано трехзначное число. Найдите сумму его цифр.

num = int(input('Введи трехзначное число: '))

if num > 999 or num < 100:
    print('error')
    False
else:
    num_3 = num % 10
    num_2 = (num // 10) % 10
    num_1 = num // 100
    # print(f'сумма трех чисел: {num_1 + num_2 + num_3}')
    print(num_1 + num_2 + num_3)