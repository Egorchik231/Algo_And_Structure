import random
import timeit

ITEMS_NUMBER = 10
MIN_ITEM = -100
MAX_ITEM = 99

my_array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(ITEMS_NUMBER)]
print(my_array)
my_array1 = my_array.copy()


def bubble_sort(array):
    n = 0
    while n < len(array):
        for k in range(len(array) - 1):
            if array[k + 1] > array[k]:
                array[k + 1], array[k] = array[k], array[k + 1]
        n += 1
    return array


def bubble_sort_upgraded(arr):
    k = 0
    while k < (len(arr) - 1):
        if arr[k + 1] > arr[k]:
            arr[k + 1], arr[k] = arr[k], arr[k + 1]
            k = -1
        k += 1
    return arr


print(bubble_sort(my_array))
print(bubble_sort_upgraded(my_array1))

print(timeit.timeit('bubble_sort(my_array)', number=10000, globals=globals())) # 0.1799909
print(timeit.timeit('bubble_sort_upgraded(my_array1)', number=10000, globals=globals())) #0.02974080000000001

# Second version is better (APPROVED)
