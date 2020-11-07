# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 5
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
my_max, my_min = array[0], array[0]
for i in array:
    if i > my_max:
        my_max = i
    if i < my_min:
        my_min = i

print(my_min, my_max)
my_sum = 0
for i in array:
    if i != my_min:
        if i != my_max:
            my_sum += i

print(my_sum)
