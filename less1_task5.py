# Вводятся три разных числа. Найти, какое из них является средним
# (больше одного, но меньше другого)

print('Введите три числа: ')
a = float(input())
b = float(input())
c = float(input())

if a > b:
    if a > c:
        if c > b:
            print(c)
        else:
            print(b)
    else:
        print(a)
else:
    if b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        print(b)