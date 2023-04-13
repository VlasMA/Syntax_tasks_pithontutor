# Цикл while (“пока”) позволяет выполнить одну и ту же последовательность действий, 
# пока проверяемое условие истинно. 
# Условие записывается до тела цикла и проверяется до выполнения тела цикла.
#  Как правило, цикл while используется,
#  когда невозможно определить точное значение количества проходов исполнения цикла.

# ри выполнении цикла while сначала проверяется условие. 
# Если оно ложно, то выполнение цикла прекращается и управление передается на
#  следующую инструкцию после тела цикла while. Если условие истинно,
#  то выполняется инструкция, после чего условие проверяется снова и снова выполняется инструкция.
#  Так продолжается до тех пор, пока условие будет истинно. 
# Как только условие станет ложно, работа цикла завершится и управление передастся следующей инструкции после цикла.

# Например, следующий фрагмент программы напечатает на экран квадраты всех целых чисел от 1 до 10. 
# Видно, что цикл while может заменять цикл for ... in range(...):

i = 1
while i <= 10:
    print(i ** 2)
    i += 1

#  этом примере переменная i внутри цикла изменяется от 1 до 10. 
# Такая переменная, значение которой меняется с каждым новым проходом цикла, 
# называется счетчиком. Заметим, что после выполнения этого фрагмента значение переменной i будет равно 11,
#  поскольку именно при i == 11 условие i <= 10 впервые перестанет выполняться.

# Вот еще один пример использования цикла while для определения количества цифр натурального числа n:

n = int(input())
length = 0
while n > 0:
    n //= 10  # это эквивалентно n = n // 10
    length += 1
print(length)

# В этом цикле мы отбрасываем по одной цифре числа, начиная с конца,
#  что эквивалентно целочисленному делению на 10 (n //= 10),
#  при этом считаем в переменной length, сколько раз это было сделано.

# В языке Питон есть и другой способ решения этой задачи: length = len(str(i)).