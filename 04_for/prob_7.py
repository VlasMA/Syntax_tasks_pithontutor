# По данному натуральному n вычислите сумму 13+23+33+...+n3.

num = int(input('сколько будет кубов?: '))

sum = 0
for i in range(1,num+1):
    sum += i**3
print(sum)