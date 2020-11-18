# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

"""
[1 2 3 4 5 6 7 8 9 10 11 12 13 14 15]
[1 2 3 4 5 6 7 8 9  A  B  C  D  E  F]
"""

from collections import deque

BASE = 16

HEX_DEX = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
           '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
           'C': 12, 'D': 13, 'E': 14, 'F': 15,
           }
DEX_HEX = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6',
           7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
           13: 'D', 14: 'E', 15: 'F'
           }

first = deque(input('Enter first number: ').upper())
second = deque(input('Enter second number: ').upper())


def hex_sum(first_numb, second_numb):

    if len(first_numb) < len(second_numb):
        first_numb.appendleft('0' * (len(second_numb) - len(first_numb)))
        first_numb, second_numb = second_numb, first_numb
    elif len(first_numb) > len(second_numb):
        second_numb.appendleft('0' * (len(first_numb) - len(second_numb)))

    first_c = first_numb.copy()
    first_c.reverse()
    second_c = second_numb.copy()
    result = deque([])
    isOneInMind = 0

    for i in first_c:
        pre_res = HEX_DEX[i] + HEX_DEX[second_c.pop()] + isOneInMind
        if pre_res >= BASE:
            isOneInMind = 1
            pre_res -= BASE
        else:
            isOneInMind = 0

        result.appendleft(DEX_HEX[pre_res])
    if isOneInMind:
        result.appendleft(1)

    return result


def hex_mult(first_numb, second_numb):
    first_c = first_numb.copy()
    first_c.reverse()
    second_c = second_numb.copy()
    second_c.reverse()
    res_for_sum = []
    multiplicand = 0
    for i in second_c:
        SomeInMind = 0

        res_numbers = deque()
        for k in first_c:

            pre_res = HEX_DEX[i] * HEX_DEX[k] + SomeInMind

            if pre_res >= BASE:
                SomeInMind = pre_res // BASE
                pre_res %= BASE
            else:
                SomeInMind = 0

            res_numbers.appendleft(DEX_HEX[pre_res])

        if SomeInMind != 0:
            res_numbers.appendleft(str(SomeInMind))
        if multiplicand > 0:
            for j in range(multiplicand):
                res_numbers.append('0')

        res_for_sum.append(res_numbers)
        multiplicand += 1

    result = res_for_sum[0]
    for i in range(len(res_for_sum) - 1):
        result = hex_sum(result, res_for_sum[i+1])
    return result


print(hex_sum(first, second))
print(hex_mult(first, second))
