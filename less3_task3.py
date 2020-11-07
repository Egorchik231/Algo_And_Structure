# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)
my_max, my_min = array[0], array[0]

for i in array:
    if i > my_max:
        my_max = i
    if i < my_min:
        my_min = i

array[array.index(my_max)] = my_min
array[array.index(my_min)] = my_max

print(array)
