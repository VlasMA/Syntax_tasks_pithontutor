# Дано натуральное число A. Определите, каким по счету числом Фибоначчи оно является,
#  то есть выведите такое число n, что φn = A. Если А не является числом Фибоначчи, выведите число -1.

fib1 = 1
fib2 = 1 
n = int(input()) 
i = 0
if n == 0:
    print(0)
else:
    while fib2 != n:
        fib_sum = fib1 + fib2
        if fib_sum > n:
            print(-1)
            break
        fib1 = fib2
        fib2 = fib_sum
        i += 1
    else:
        print(i+2)


# ответ с сайта
# x=0
# x1=1
# x2=0
# i=0
# n=int(input())
# while x <= n:
#     x = x1 + x2
#     x1, x2 = x, x1
#     i += 1
# if (n == x2):
#     print(i)
# else:
#     print(-1)