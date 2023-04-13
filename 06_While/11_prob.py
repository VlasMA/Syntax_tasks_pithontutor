# Последовательность состоит из натуральных чисел и завершается числом 0. 
# Определите значение наибольшего элемента последовательности.

num = int(input())
max_el = num
while num != 0:
    num = int(input())
    if num > max_el:
        max_el = num
print(max_el)
