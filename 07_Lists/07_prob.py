# Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

a = input().split()
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        print(a[i])


# #  решение разрабов
# a = [int(i) for i in input().split()]
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i])