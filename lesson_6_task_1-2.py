'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''

# https://pypi.org/project/memory-profiler/
# pip install -U memory_profiler


@profile
def isEven(itm):
    if itm & 1 == 0:
        return True
    else:
        return False


@profile
def even_num_indexes(data: list) -> list:
    return [ind for ind, value in enumerate(data) if isEven(value) == True]


if __name__ == "__main__":
    even_num_indexes([8, 3, 15, 6, 4, 2])


# python -m memory_profiler .\lesson_6_task_1-2.py
# Filename: .\lesson_6_task_1-2.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     10   42.383 MiB   42.383 MiB   @profile
#     11                             def isEven(itm):
#     12   42.383 MiB    0.000 MiB       if itm & 1 == 0:
#     13   42.383 MiB    0.000 MiB           return True
#     14                                 else:
#     15   42.383 MiB    0.000 MiB           return False


# Filename: .\lesson_6_task_1-2.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     18   42.383 MiB   42.383 MiB   @profile
#     19                             def even_num_indexes(data: list) -> list:
#     20   42.383 MiB   42.383 MiB       return [ind for ind, value in enumerate(data) if isEven(value) == True]
