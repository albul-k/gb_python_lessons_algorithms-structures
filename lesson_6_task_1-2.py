'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''

# https://pypi.org/project/memory-profiler/
# pip install -U memory_profiler


def isEven(itm):
    if itm & 1 == 0:
        return True
    else:
        return False


@profile
def even_num_indexes(data: list) -> list:
    return [ind for ind, value in enumerate(data) if isEven(value) == True]


if __name__ == "__main__":
    file_data = 'data.txt'
    try:
        with open(file_data, 'r', encoding='UTF-8') as f_in:
            data = list(map(lambda itm: int(itm), f_in.readline().split()))
    except IOError:
        print("Произошла ошибка ввода/вывода файла")

    even_num_indexes(data)


# python -m memory_profiler .\lesson_6_task_1-2.py
# Filename: .\lesson_6_task_1-2.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     17   50.719 MiB   50.719 MiB   @profile
#     18                             def even_num_indexes(data: list) -> list:
#     19   70.055 MiB    0.758 MiB       return [ind for ind, value in enumerate(data) if isEven(value) == True]
