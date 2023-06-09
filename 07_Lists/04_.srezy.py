                                               # 4. Срезы
# Со списками, так же как и со строками, можно делать срезы. А именно:


# A[i:j]  срез из j-i элементов A[i], A[i+1], ..., A[j-1].
# A[i:j:-1]  срез из i-j элементов A[i], A[i-1], ..., A[j+1] (то есть меняется порядок элементов).
# A[i:j:k]  срез с шагом k: A[i], A[i+k], A[i+2*k],... . Если значение k<0, то элементы идут в противоположном порядке.
# Каждое из чисел i или j может отсутствовать, что означает “начало строки” или “конец строки”

# Списки, в отличии от строк, являются изменяемыми объектами: 
# можно отдельному элементу списка присвоить новое значение. Но можно менять и целиком срезы. Например:

A = [1, 2, 3, 4, 5]
A[2:4] = [7, 8, 9]
print(A)    #[1, 2, 7, 8, 9, 5]



b = [1, 2, 3, 4, 5, 6,  7]
b[::-2] = [10, 20, 30, 40]
print(b)   #[40, 2, 30, 4, 20, 6, 10]

# Получится список [40, 2, 30, 4, 20, 6, 10].
#  Здесь A[::-2] — это список из элементов A[-1], A[-3], A[-5], A[-7], 
# которым присваиваются значения 10, 20, 30, 40 соответственно.

                        # Операции со списками
# x in A	Проверить, содержится ли элемент в списке. Возвращает True или False
# x not in A	То же самое, что not(x in A)
# min(A)	Наименьший элемент списка
# max(A)	Наибольший элемент списка
# A.index(x)	Индекс первого вхождения элемента x в список, при его отсутствии генерирует исключение ValueError
# A.count(x)	Количество вхождений элемента x в список