'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану. 
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
'''

import random
from statistics import median


def get_med(data: list) -> int:
    quotient, remainder = divmod(len(data), 2)
    print(remainder)
    # в нашем случае в else никогда попадать не будем, тк массив 2m + 1
    if remainder:
        return sorted(data)[quotient]
    else:
        return sum(sorted(data)[quotient - 1:quotient + 1]) / 2


if __name__ == "__main__":
    m = 10
    array = [random.randint(0, 50) for _ in range(2*m + 1)]
    print(f'Исходный список: {array}')
    print(
        f'Поиск медианы при помощи встроенной функции median: {median(array)}')
    print(f'Поиск медианы при помощи sorted: {get_med(array)}')
