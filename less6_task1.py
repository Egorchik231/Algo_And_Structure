# Задача, решаемая алгоритмом:

# Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать,
# задаются вводом с клавиатуры.
import struct
import random
from collections import Container, Mapping
from sys import getsizeof

SIZE3 = 3
MIN_ITEM = 100000
MAX_ITEM = 999999
array3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE3)]

TASK = 3


# Вариант 1
# *******************************************************#

def count_figure_in_number(number, count, task):
    if number % 10 == task:
        count += 1

    number //= 10
    if number == 0:

        return count, locals()
    else:

        return count_figure_in_number(number, count, task)


def count_figure_in_numbers(array, figure, count, counter_rec):
    for ind_k, k in enumerate(array):
        i = 0
        res, anali = count_figure_in_number(k, i, figure)
        count += res
        if counter_rec == 1:
            return locals()
        counter_rec += 1
        return count_figure_in_numbers(array[ind_k + 1:], figure, count, counter_rec)
    else:
        return count


count = 0
print('*' * 50)


# Вариант 2
# *******************************************************#


def count_figure_in_numbers_v2(array, task):
    count = 0
    for item in array:
        while item != 0:
            if item % 10 == task:
                count += 1
            item //= 10
    return locals()


# Вариант 3
# *******************************************************#


def count_figure_in_numbers_v3(array, task, count, counter_rec):
    for ind_k, k in enumerate(array):
        while k != 0:
            if k % 10 == task:
                count += 1
            k //= 10
        if counter_rec == 1:
            return locals()
        return count_figure_in_numbers_v3(array[ind_k + 1:], task, count, counter_rec)
    else:
        return count


count = 0
# count_figure_in_numbers(array3, TASK, count)
#
# count = 0
# count_figure_in_numbers_v2(array3, TASK, count)
#
# count = 0
# count_figure_in_numbers_v3(array3, TASK, count)


counter_rec = 1
end = count_figure_in_numbers(array3, TASK, count, counter_rec)


def deep_getsizeof(o, ids):
    d = deep_getsizeof
    if id(o) in ids:
        return 0

    r = getsizeof(o)
    ids.add(id(o))

    if isinstance(o, str):
        return r

    if isinstance(o, Mapping):
        return sum(d(k, ids) + d(v, ids) for k, v in o.items())

    if isinstance(o, Container):
        return sum(d(x, ids) for x in o)

    return r


# Вариант 1
a = deep_getsizeof(end['anali'], set()) - deep_getsizeof(end['anali']['number'], set()) - \
     deep_getsizeof(end['anali']['count'], set()) - deep_getsizeof(end['anali']['task'], set())

print(end)
print(deep_getsizeof(end, set()) - deep_getsizeof(end['counter_rec'], set()) - a)


# Вариант 2

print(count_figure_in_numbers_v2(array3, TASK))
print(deep_getsizeof(count_figure_in_numbers_v2(array3, TASK), set()))

# Вариант 3


print(count_figure_in_numbers_v3(array3, TASK, count, counter_rec))
print(deep_getsizeof(count_figure_in_numbers_v3(array3, TASK, count, counter_rec), set()))

# Самый оптимальный вариант с точки зрения потребления памяти номер 2.
# Самый неэффективный оказался вариант построенный полностью на рекурсия. 