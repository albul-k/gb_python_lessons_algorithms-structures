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
    file_data = 'data.txt'
    try:
        with open(file_data, 'r', encoding='UTF-8') as f_in:
            data = list(map(lambda itm: int(itm), f_in.readline().split()))
    except IOError:
        print("Произошла ошибка ввода/вывода файла")

    even_num_indexes(data)


# python -m memory_profiler .\lesson_6_task_1-1.py
# Filename: .\lesson_6_task_1-1.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     10   50.539 MiB   50.539 MiB   @profile
#     11                             def even_num_indexes(data: list) -> list:
#     12   69.840 MiB    0.391 MiB       return [ind for ind, value in enumerate(data) if value & 1 == 0]
