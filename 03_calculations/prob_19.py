# Процентная ставка по вкладу составляет P процентов годовых, 
# которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек. 
# Определите размер вклада через год.
# Программа получает на вход целые числа P, X, Y и должна вывести два числа: 
# величину вклада через год в рублях и копейках. Дробная часть копеек отбрасывается.
import math

p = int(input('procent: '))
x = int(input('rub: '))
y = int(input('kop: '))

procent = p / 100
# print(procent)
result_procent = x * 100 + y
# print(result_procent)

ansver = result_procent * procent
# print(ansver)

itog = ansver + result_procent
# print(math.floor(itog))

rub = itog // 100
# print(math.floor(rub))

kop = itog % 100
# print(math.floor(kop))

print(math.floor(rub), math.floor(kop))


