# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры


def count_sum(n, q, b1, res):
    if n == 0:
        return res
    else:
        res += b1
        b1 *= q
        n -= 1
        return count_sum(n,q,b1,res)


n = int(input('Введите количество членов послежовательности: '))

res = 0
Q = -0.5
b1 = 1

result = count_sum(n,Q,b1,res)
print(result)