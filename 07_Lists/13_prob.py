# Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т. д.).
#  Если элементов нечетное число, то последний элемент остается на своем месте.

a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i], = a[i], a[i - 1]
print(' '.join([str(i) for i in a]) )

