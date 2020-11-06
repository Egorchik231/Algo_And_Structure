# Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать,
# задаются вводом с клавиатуры.


def count_figure_in_number(number, count, task):
    figure = number % 10

    if figure == task:
        count += 1

    number //= 10
    if number == 0:
        return count
    else:
        return count_figure_in_number(number, count, task)


def count_figure_in_numbers(n, figure, count):
    if n == 0:
        return count
    else:
        n -= 1
        number = int(input('Введите число'))
        i = 0
        res = count_figure_in_number(number, i, figure)
        count += res
        return count_figure_in_numbers(n, figure, count)


count = 0
n = int(input('Введите количество чисел: '))
figure = int(input('Введите цифру, которую хотите посчитать: '))

result = count_figure_in_numbers(n, figure, count)
print(result)