# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).

def count_even_odd(number, even, odd):
    figure = number % 10
    if figure % 2 == 0:
        even += 1
    else:
        odd += 1

    number //= 10
    if number == 0:
        return f' чётных цифр: {even}, нечётных цифр: {odd}'
    else:
        return count_even_odd(number, even, odd)


a = int(input('Введите натуральное число: '))

even = 0
odd = 0

result = count_even_odd(a, even, odd)

print(result)