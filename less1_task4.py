# Определить, является ли год,
# который ввел пользователь,
# високосным или не високосным

print('Введите номер года')
a = int(input())

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print('Год високосный')
        else:
            print('Год не високосный')
    else:
        print('Год не високосный')
else:
    print('Год не високосный')