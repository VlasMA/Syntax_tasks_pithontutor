# Дан список чисел. Выведите значение наибольшего элемента в списке,
#  а затем индекс этого элемента в списке. 
# Если наибольших элементов несколько, выведите индекс первого из них.

a = [int(i) for i in input().split()]
index_max = 0
max_el = a[0]
for i in range(0, len(a)):
    if a[i] > max_el:
        max_el = a[i]
        index_max = i
print(max_el, index_max)


