# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.


a = int(input('введи число a: '))
b = int(input('введи число b: '))

if b < a:
    print('error') 
    False
else:
    for i in range(a, b+1):
        print(i)