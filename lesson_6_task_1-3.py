'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
'''

# https://pypi.org/project/memory-profiler/
# pip install -U memory_profiler


@profile
def even_num_indexes(data: list) -> list:
    def recur(ind, data_res):
        if data[ind] & 1 == 0:
            data_res.append(ind)
        ind += 1
        if ind+1 > len(data):
            return
        recur(ind, data_res)
        return
    data_res = []
    recur(0, data_res)
    return data_res


if __name__ == "__main__":
    even_num_indexes([8, 3, 15, 6, 4, 2])


# python -m memory_profiler .\lesson_6_task_1-3.py
# Filename: .\lesson_6_task_1-3.py

# Line #    Mem usage    Increment   Line Contents
# ================================================
#     10   42.484 MiB   42.484 MiB   @profile
#     11                             def even_num_indexes(data: list) -> list:
#     12   42.484 MiB    0.000 MiB       def recur(ind, data_res):
#     13   42.484 MiB    0.000 MiB           if data[ind] & 1 == 0:
#     14   42.484 MiB    0.000 MiB               data_res.append(ind)
#     15   42.484 MiB    0.000 MiB           ind += 1
#     16   42.484 MiB    0.000 MiB           if ind+1 > len(data):
#     17   42.484 MiB    0.000 MiB               return
#     18   42.484 MiB    0.000 MiB           recur(ind, data_res)
#     19   42.484 MiB    0.000 MiB           return
#     20   42.484 MiB    0.000 MiB       data_res = []
#     21   42.484 MiB    0.000 MiB       recur(0, data_res)
#     22   42.484 MiB    0.000 MiB       return data_res
