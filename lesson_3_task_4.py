'''
4. Определить, какое число в массиве встречается чаще всего.
'''


def most_used_num(data: list) -> int:
    data_set = set(data)
    i, num = float("-inf"), None
    for itm in data_set:
        _t = data.count(itm)
        if _t > i:
            i = _t
            num = itm
    # если все элементы в исходном массиве встречаются единожды, возвращаем первый элемент
    if i == 1:
        return data[0]
    else:
        return num


if __name__ == "__main__":
    print(most_used_num([1, 2, 2, 3, 3, 3]))

    assert(most_used_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == 1
    assert(most_used_num([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 0])) == 2
    assert(most_used_num(
        [10, 23, 54, 45, 76, 23, 54, 65, 34, 34, 54, 54, 56])) == 54
