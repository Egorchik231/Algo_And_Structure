# https://1drv.ms/u/s!AvciIcj13L2mmU4FIdHBpc1Zekq4 ссылка на БС

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

print('Введите трехзначное число: ')
a = int(input())
summ = a % 10
mult = a % 10
a //= 10

summ += a % 10
mult *= a % 10

a //= 10

summ += a % 10
mult *= a % 10

print(summ, mult)
