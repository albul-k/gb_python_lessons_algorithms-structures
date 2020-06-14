'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
'''

import random
import operator


def merge(left: list, right: list, compare: any):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def my_merge_sort(data: list, compare: any) -> list:
    if len(data) < 2:
        return data[:]
    else:
        middle = int(len(data) / 2)
        left = my_merge_sort(data[:middle], compare)
        right = my_merge_sort(data[middle:], compare)
        return merge(left, right, compare)


if __name__ == "__main__":
    num = 30
    array = [round(random.randint(0, 49)*random.random(), 2)
             for _ in range(num)]
    print(array)
    print(my_merge_sort(array, operator.lt))
