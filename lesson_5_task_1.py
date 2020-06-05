'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''

from collections import namedtuple

Company = namedtuple('Company', 'name, profit')

total = 0
comp_list = []
inp_num = int(input('Введите количество предприятий: '))
for i in range(1, inp_num + 1):
    inp_name = input('\nВведите название предприятия: ')
    inp_profit = int(input('Введите прибыль за четыре квартала: '))

    comp_list.append(Company(inp_name, inp_profit))
    total += inp_profit

average_total = round(total / inp_num)
print(f'\nСредняя прибыль: {average_total}')

comp_less_list, comp_more_list = [], []
for itm in comp_list:
    if itm.profit > average_total:
        comp_more_list.append(itm.name)
    else:
        comp_less_list.append(itm.name)

print(f'Список предприятий, чья прибыль меньше среднего: {comp_less_list}')
print(f'Список предприятий, чья прибыль больше среднего: {comp_more_list}')
