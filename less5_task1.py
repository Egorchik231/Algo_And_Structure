# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал
# (т.е. 4 числа) для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import deque, namedtuple

more_less_average = deque([None])
companies_number = int(input('Введите кол-во предприятий: '))
average_all = 0
Company = namedtuple('Company', 'name, average_profit')
comp_base = []

for company in range(companies_number):
    name = input('Enter name: ')
    average_profit = 0
    for i in range(4):
        profit = int(input(f'Enter profit of {i + 1} quarter: '))
        average_profit += profit
    average_all += average_profit
    comp = Company(name, average_profit/4)
    comp_base.append(comp)

average_all /= companies_number * 4

for comp in comp_base:
    if comp.average_profit < average_all:
        more_less_average.appendleft(comp.name)
    elif comp.average_profit > average_all:
        more_less_average.append(comp.name)

text = 'less'
for comp in more_less_average:

    if comp is None:
        text = 'more'
    else:
        print(f'Average profit of {comp} {text} than all average profit')
