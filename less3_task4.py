# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче:
# пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.

import random

SIZE = 5
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(array)

my_min = None
for i in array:
    for _ in array:
        if _ < 0:
            my_min = _
            break

    if i < 0 and i > my_min:
        my_min = i

print(my_min)
