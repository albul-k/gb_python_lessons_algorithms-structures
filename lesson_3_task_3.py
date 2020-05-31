'''
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''


def change_min_and_max(data: list) -> list:
    min_num, max_num = float("inf"), float("-inf")
    min_num_ind, max_num_ind = 0, 0
    for ind, value in enumerate(data):
        if value < min_num:
            min_num = value
            min_num_ind = ind

        if value > max_num:
            max_num = value
            max_num_ind = ind
    data[max_num_ind], data[min_num_ind] = data[min_num_ind], data[max_num_ind]
    return data


if __name__ == "__main__":
    print(change_min_and_max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
    print(change_min_and_max([-30, 1, 20, 3, 4, 5, 6, 7, 8, 9]))

    assert(change_min_and_max([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])) == [
        9, 1, 2, 3, 4, 5, 6, 7, 8, 0]
    assert(change_min_and_max([9, 1, 2, 3, 4, 5, 6, 7, 8, 0])) == [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert(change_min_and_max(
        [-30, 1, 20, 3, 4, 5, 6, 7, 8, 9])) == [20, 1, -30, 3, 4, 5, 6, 7, 8, 9]
    assert(change_min_and_max([0, 1])) == [1, 0]
    assert(change_min_and_max([0, 0])) == [0, 0]
