# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте количество нулей 
# среди введенных чисел и выведите это количество. Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр.

n = int(input('введи сколько будет чисел: '))

sum = 0

for i in range(n):
    number = int(input())
    if number == 0:
        sum = sum + 1
    else:
        sum = sum + 0
print(sum)

