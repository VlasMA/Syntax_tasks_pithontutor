# Даны два целых числа A и В, A>B. 
# Выведите все нечётные числа от A до B включительно, в порядке убывания.
#  В этой задаче можно обойтись без инструкции if.

a = int(input('a: '))
b = int(input('b: '))

for i in range(a, b-1,-1):
    if i % 2 != 0:
        print(i)
