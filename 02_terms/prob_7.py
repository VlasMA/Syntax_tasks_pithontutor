# Шахматная ладья ходит по горизонтали или вертикали.
#  Даны две различные клетки шахматной доски, определите, может ли ладья попасть с 
# первой клетки на вторую одним ходом. Программа получает на вход четыре числа от 1 до 8 каждое, 
# задающие номер столбца и номер строки сначала для первой клетки, потом для второй клетки. 
# Программа должна вывести YES, если из первой клетки ходом ладьи можно попасть во вторую или NO в противном случае.


num_1 = int(input('введи номер 1го столбца: '))
num_2 = int(input('введи номер 1ой строки: '))
num_3 = int(input('введи номер 2го столбца: '))
num_4 = int(input('введи номер 2ой строки: '))


if num_1 > 8 or num_1 < 1 or num_2 > 8 or num_2 < 1 or num_3 > 8 or num_3 < 1 or num_4 > 8 or num_4 < 1:
    print('error')
    False
else:
    if num_1 == num_3 or num_2 == num_4:
        print('yas')
    else:
        print('NO')