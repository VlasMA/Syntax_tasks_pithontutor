
# print(abs(-6))


# Шахматный ферзь ходит по диагонали, горизонтали или вертикали. 
# Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом.


num_1 = int(input('введи номер 1го столбца: '))
num_2 = int(input('введи номер 1ой строки: '))
num_3 = int(input('введи номер 2го столбца: '))
num_4 = int(input('введи номер 2ой строки: '))


if num_1 > 8 or num_1 < 1 or num_2 > 8 or num_2 < 1 or num_3 > 8 or num_3 < 1 or num_4 > 8 or num_4 < 1:
    print('error')
    False
else:
    if abs(num_1 - num_3) == abs(num_2 - num_4) or num_1 == num_3 or num_2 == num_4:
        print('YES')
    else:
        print('NO')