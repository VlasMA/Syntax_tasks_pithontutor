# Последовательность состоит из натуральных чисел и завершается числом 0.
#  Определите, сколько элементов этой последовательности больше предыдущего элемента.

num = -1
len = -1
while num != 0:
    i = num
    num = int(input())
    if num > i:
        len +=1
print(len)