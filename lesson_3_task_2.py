'''
2. Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
'''


def even_num_indexes(data: list) -> list:
    return [ind for ind, value in enumerate(data) if value & 1 == 0]


if __name__ == "__main__":
    print(even_num_indexes([8, 3, 15, 6, 4, 2]))

    assert(even_num_indexes([8, 3, 15, 6, 4, 2])) == [0, 3, 4, 5]
    assert(even_num_indexes([7, 3, 15, 5, 7, 1])) == []
    assert(even_num_indexes([7, 8, 15, 6, 4, 2])) == [1, 3, 4, 5]
