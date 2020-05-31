'''
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
'''


def sum_num_beetween_min_and_max(data: list) -> int:
    min_num, max_num = float("inf"), float("-inf")
    min_num_ind, max_num_ind = 0, 0
    for ind, value in enumerate(data):
        if value < min_num:
            min_num = value
            min_num_ind = ind

        if value > max_num:
            max_num = value
            max_num_ind = ind
    # минимальный элемент в массиве находится после максимального => не ищем сумму
    if min_num_ind >= max_num_ind:
        return 0
    else:
        my_sum = 0
        for i in range(min_num_ind + 1, max_num_ind):
            my_sum += data[i]
        return my_sum


if __name__ == "__main__":
    print(sum_num_beetween_min_and_max([0, 1, 2, 3]))

    assert(sum_num_beetween_min_and_max([0, 1, 2, 3])) == 3
    assert(sum_num_beetween_min_and_max([1, 1, 2, 3])) == 3
    assert(sum_num_beetween_min_and_max([1, 1, 3, 3])) == 1
    assert(sum_num_beetween_min_and_max([1, 3, 3, 3])) == 0
    assert(sum_num_beetween_min_and_max([3, 2, 1, 0])) == 0
