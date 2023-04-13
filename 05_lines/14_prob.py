# Дана строка. Замените в этой строке все появления буквы h на букву H,
#  кроме первого и последнего вхождения.

s = input()

n1  = s.find('h')
n2 = s.rfind('h')

t = s[n1+1:n2]
t1 = s[:n1+1]
t2 = s[n2:]

print(t1 + t.replace('h', 'H') + t2)


# Красивое решение

# x= str(input())
# a = x.find('h')
# b = x.rfind('h')

# print(x[:a+1] + x[a+1:b].replace('h','H')+ x[b:])