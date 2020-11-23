# Задача, решаемая алгоритмом:

# Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать,
# задаются вводом с клавиатуры.
import timeit
import cProfile
import random

SIZE1, SIZE2, SIZE3, SIZE4, SIZE5 = 100, 200, 400, 800, 900
MIN_ITEM = 100000
MAX_ITEM = 999999
array1 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE1)]
array2 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE2)]
array3 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE3)]
array4 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE4)]
array5 = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE5)]
TASK = 3


# Вариант 1
# *******************************************************#

def count_figure_in_number(number, count, task):
    if number % 10 == task:
        count += 1

    number //= 10
    if number == 0:
        return count
    else:
        return count_figure_in_number(number, count, task)


def count_figure_in_numbers(array, figure, count):
    for ind_k, k in enumerate(array):
        i = 0
        res = count_figure_in_number(k, i, figure)
        count += res
        return count_figure_in_numbers(array[ind_k + 1:], figure, count)
    else:
        return count


count = 0
print(timeit.timeit('count_figure_in_numbers(array1, TASK, count)', number=100, globals=globals()))
# 0.022380500000000005
count = 0
print(timeit.timeit('count_figure_in_numbers(array2, TASK, count)', number=100, globals=globals()))
# 0.04748780000000001

count = 0
print(timeit.timeit('count_figure_in_numbers(array3, TASK, count)', number=100, globals=globals()))
# 0.1347299

count = 0
print(timeit.timeit('count_figure_in_numbers(array4, TASK, count)', number=100, globals=globals()))
# 0.40763770000000005

count = 0
print(timeit.timeit('count_figure_in_numbers(array5, TASK, count)', number=100, globals=globals()))
# 0.5143346000000001

count = 0
cProfile.run('count_figure_in_numbers(array5, TASK, count)')
# 5400/900    0.004    0.000    0.004    0.000 less4_task1.py:25(count_figure_in_number)
#    901/1    0.010    0.000    0.015    0.015 less4_task1.py:36(count_figure_in_numbers)
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
    return count


print(timeit.timeit('count_figure_in_numbers_v2(array1, TASK)', number=100, globals=globals()))
# 0.005658900000000022
print(timeit.timeit('count_figure_in_numbers_v2(array2, TASK)', number=100, globals=globals()))
# 0.01125329999999991
print(timeit.timeit('count_figure_in_numbers_v2(array3, TASK)', number=100, globals=globals()))
# 0.022574399999999883
print(timeit.timeit('count_figure_in_numbers_v2(array4, TASK)', number=100, globals=globals()))
# 0.04485070000000002
print(timeit.timeit('count_figure_in_numbers_v2(array5, TASK)', number=100, globals=globals()))
# 0.05082370000000003

cProfile.run('count_figure_in_numbers_v2(array5, TASK)')
#        1    0.001    0.001    0.001    0.001 less4_task1.py:71(count_figure_in_numbers_v2)
print('*' * 50)

# Вариант 3
# *******************************************************#


def count_figure_in_numbers_v3(array, task, count):
    for ind_k, k in enumerate(array):
        while k != 0:
            if k % 10 == task:
                count += 1
            k //= 10
        return count_figure_in_numbers_v3(array[ind_k + 1:], task, count)
    else:
        return count


count = 0
print(timeit.timeit('count_figure_in_numbers_v3(array1, TASK, count)', number=100, globals=globals()))
# 0.012135000000000007

count = 0
print(timeit.timeit('count_figure_in_numbers_v3(array2, TASK, count)', number=100, globals=globals()))
# 0.0356183000000001

count = 0
print(timeit.timeit('count_figure_in_numbers_v3(array3, TASK, count)', number=100, globals=globals()))
# 0.1118112

count = 0
print(timeit.timeit('count_figure_in_numbers_v3(array4, TASK, count)', number=100, globals=globals()))
# 0.38695999999999997

count = 0
print(timeit.timeit('count_figure_in_numbers_v3(array5, TASK, count)', number=100, globals=globals()))
# 0.45274579999999975

cProfile.run('count_figure_in_numbers_v3(array5, TASK, count)')
# 901/1    0.006    0.000    0.006    0.006 less4_task1.py:106(count_figure_in_numbers_v3)



'''
1 Вариант
    Итак анализирую полученные данные по первому варианту можно сказать, что увеличивая данные на вход вдвое
    время на выполнение увеличивается почти втрое, а при последнем увеличении на 12,5% вермя возврасло на четверть.
    Значит тут уместно говорить о линейной зависимости времени выполнения алгоритма от ввдоимых данных O(n) {О(3n)}
    Слабые места можно отметить в рекурсивности, Вложенная функция была вызвана более 5 тыс. раз, что сильно 
    сказалось на скорости отработки
2 Вариант
    Во втором варианте алгоритма можно проследить практически идеальную линейную зависимость с коэфициентом 2.
    O(n) {О(2n)}  
    Из слабых мест только цикл, сам по себе он элементарен и упростить для получения ещё большей производительности
    нецелесообразно, если вообще возможно.
3 Вариант
    В данном решении можно отследить ту же линейную зависимость, но больше приближенную к первому варианту, при
    удвоении вводных данных алгоритм отрабатывает втрое дольше.
    Данный алгорит является средним между первым и вторым вариантом, поэтому из слабых мест, по прежнему осталась
    рекурсия, но разделять данный вариант, как и второй, на составные части невозможно, поэтому детальный разбор 
    слабых мест невозможен.
    
Итог
    Лучше и быстрее всего отработал Вариант 2, показав лучший результат скорости и линейной зависимости.
'''