# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна
# сообщать об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления
# на ноль, если он ввел его в качестве делителя.

'''
https://drive.google.com/file/d/1a1QkdEvD2snQr7WgSJ9WvGDN35ryVP79/view
'''

def calculator(a, b, char):
    if char != '0' and char != '+' and char != '-' and char != '*' and char != '/':
        print('Введён некорректный знак операции. \n Введите 2 числа и знак операции')
        num1 = float(input('1-e число: '))
        num2 = float(input('2-e число: '))
        sign = input('Знак операции: ')
        calculator(num1, num2, sign)
    else:
        if char == '0':
            return ''
        elif char == '+':
            result = a + b
            print(result, '\n Введите 2 числа и знак операции')
            num1 = float(input('1-e число: '))
            num2 = float(input('2-e число: '))
            sign = input('Знак операции: ')
            calculator(num1, num2, sign)
        elif char == '-':
            result = a - b
            print(result, '\n Введите 2 числа и знак операции')
            num1 = float(input('1-e число: '))
            num2 = float(input('2-e число: '))
            sign = input('Знак операции: ')
            calculator(num1, num2, sign)
        elif char == '*':
            result = a * b
            print(result, '\n Введите 2 числа и знак операции')
            num1 = float(input('1-e число: '))
            num2 = float(input('2-e число: '))
            sign = input('Знак операции: ')
            calculator(num1, num2, sign)
        elif b == 0:
            print('айяйяй! На 0 делить нельзя', '\n Введите 2 числа и знак операции')
            num1 = float(input('1-e число: '))
            num2 = float(input('2-e число: '))
            sign = input('Знак операции: ')
            calculator(num1, num2, sign)
        else:
            result = a / b
            print(result, '\n Введите 2 числа и знак операции')
            num1 = float(input('1-e число: '))
            num2 = float(input('2-e число: '))
            sign = input('Знак операции: ')
            calculator(num1, num2, sign)


print('Введите 2 числа и знак операции')
num1 = float(input('1-e число: '))
num2 = float(input('2-e число: '))
sign = input('Знак операции: ')

calculator(num1, num2, sign)
