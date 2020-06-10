'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''

# https://pypi.org/project/memory-profiler/
# pip install -U memory_profiler


@profile
def even_num_indexes(data: list) -> list:
    return [ind for ind, value in enumerate(data) if value & 1 == 0]


if __name__ == "__main__":
    even_num_indexes([8, 3, 15, 6, 4, 2])


# python -m memory_profiler .\lesson_6_task_1-1.py
# Filename: .\lesson_6_task_1-1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     10   42.484 MiB   42.484 MiB   @profile
#     11                             def even_num_indexes(data: list) -> list:
#     12   42.484 MiB    0.000 MiB       return [ind for ind, value in enumerate(data) if value & 1 == 0]
