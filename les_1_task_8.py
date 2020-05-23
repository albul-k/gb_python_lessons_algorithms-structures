'''
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''

num_1 = int(input('Введите число №1\n'))
num_2 = int(input('Введите число №2\n'))
num_3 = int(input('Введите число №3\n'))

if num_1 >= num_2:
    if num_1 <= num_3:
        print(num_1)
    else:
        print(num_2)
elif num_2 <= num_3:
    print(num_2)
else:
    print(num_3)
