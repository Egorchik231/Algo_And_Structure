import random
from collections import deque

ITEMS_NUMBER = 5
MIN_ITEM = -100
MAX_ITEM = 100

my_array = [random.randint(MIN_ITEM, MAX_ITEM) for i in range(2 * ITEMS_NUMBER + 1)]
print(my_array)


def less_to_left_more_to_right(arr):
    mid_index = (len(arr) // 2)
    final_arr = deque([arr[mid_index]])

    for i, k in enumerate(arr):
        if i == mid_index:
            continue
        elif k < arr[mid_index]:
            final_arr.appendleft(k)
        elif k > arr[mid_index]:
            final_arr.append(k)
        elif i < mid_index:
            final_arr.appendleft(k)
        else:
            final_arr.append(k)

    return final_arr


print(less_to_left_more_to_right(my_array))
