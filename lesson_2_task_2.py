'''
2. Посчитать четные и нечетные цифры введенного натурального числа. 
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''

num_inp = input('Введите натуральное число: ')
even, odd = 0, 0
for itm in num_inp:
    num = int(itm)
    if num & 1 == 0:
        even += 1
    else:
        odd += 1
print(f'Введенное число: {num_inp}, четных цифр: {even}, нечетных: {odd}')
