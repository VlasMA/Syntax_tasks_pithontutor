# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. 
# Сколько яблок достанется каждому школьнику? Сколько яблок останется в корзинке? 
# Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).

n = int(input('Кол-во школьников: '))
k = int(input('Кол-во яблок: '))


ostatok_v_karzine = k%n
apple_for_stedent = k // n

print(f'по {apple_for_stedent} яблок получил каждый школьник, а в карзине осталось {ostatok_v_karzine} яблок')