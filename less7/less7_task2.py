import random

ITEMS_NUMBER = 10
MIN_ITEM = 0
MAX_ITEM = 49

my_array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 3) for i in range(ITEMS_NUMBER)]
print(my_array)


def merge(left, right):
    final_li = []
    lli = rli = 0  # left_list_index, right_list_index
    for _ in range(len(left) + len(right)):
        if lli == len(left):
            final_li.append(right[rli])
            rli += 1
        elif rli == len(right):
            final_li.append(left[lli])
            lli += 1

        if lli < len(left) and rli < len(right):
            if left[lli] <= right[rli]:
                final_li.append(left[lli])
                lli += 1
            else:
                final_li.append(right[rli])
                rli += 1
    return final_li


def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left_arr = merge_sort(array[:mid])
    right_arr = merge_sort(array[mid:])

    return merge(left_arr, right_arr)


print(merge_sort(my_array))
