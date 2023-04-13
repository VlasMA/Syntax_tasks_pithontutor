# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
#  Элементы нужно выводить в том порядке, в котором они встречаются в списке.

a = [int(i) for i in input().split()]
for i in range(len(a)):
    s = a.count(a[i])
    if s == 1:
        print(a[i])



# Метод count() возвращает количество раз, когда указанный элемент появляется в списке.


# решение разрабов
a = [int(s) for s in input().split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i], end=' ')