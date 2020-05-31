'''
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». 
Это два абсолютно разных значения.
'''

# под "максимальным отрицательным" понимаю наибольшее отрицательное, то есть, то число, которое из отрицательных ближе к нулю


def max_negative(data: list) -> float:
    num, max_negative = float("-inf"), None
    for itm in data:
        if itm < 0 and itm > num:
            num = max_negative = itm
    return max_negative


if __name__ == "__main__":
    print(max_negative([0, 1, -3, -5, -3, -2, 5, 3, 2]))

    assert(max_negative([0, 1, -3, -5, -3, -2, 5, 3, 2])) == -2
    assert(max_negative([0, 1, -3, -5, -3, -2, -1.999, 5, 3, 2])) == -1.999
    assert(max_negative([0, 1, 3, 5, 3, 2, 5, 3, 2])) == None
    assert(max_negative([-2])) == -2
    assert(max_negative([])) == None
