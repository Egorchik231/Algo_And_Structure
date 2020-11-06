# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

def turn_over_number(numb, res):
    figure = numb % 10
    res = f'{res}{figure}'
    numb //= 10
    if numb == 0:
        return res
    else:
        return turn_over_number(numb, res)


result = ''
a = int(input('Введите натуральное число: '))
res = turn_over_number(a, result)
print(res)