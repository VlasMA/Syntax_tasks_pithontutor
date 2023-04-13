# В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка.
a = [int(i) for i in input().split()]
index_max = 0
index_min = 0
for i in range(1, len(a)):
    if a[i] > a[index_max]:
        index_max = i
    if a[i] <  a[index_min]:
        index_min = i
a[index_min], a[index_max] = a[index_max], a[index_min]
print(' '.join([str(i) for i in a]))








