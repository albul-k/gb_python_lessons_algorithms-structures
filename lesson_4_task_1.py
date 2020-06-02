'''
1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать,
b. написать 3 варианта кода (один у вас уже есть),
c. проанализировать 3 варианта и выбрать оптимальный,
d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
e. написать общий вывод: какой из трёх вариантов лучше и почему.
'''

import cProfile


# 1st vers (origin)
def even_num_indexes(data: list) -> list:
    return [ind for ind, value in enumerate(data) if value & 1 == 0]
# # python -m timeit -n 1000000 -s "import lesson_4_task_1" "lesson_4_task_1.even_num_indexes([8, 3, 15, 6, 4, 2])"
# # 1000000 loops, best of 5: 975 nsec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:11(even_num_indexes)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:12(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# # 2nd vers
# def isEven(itm):
#     if itm & 1 == 0:
#         return True
#     else:
#         return False
# def even_num_indexes(data: list) -> list:
#     return [ind for ind, value in enumerate(data) if isEven(value) == True]
#
# # python -m timeit -n 1000000 -s "import lesson_4_task_1" "lesson_4_task_1.even_num_indexes([8, 3, 15, 6, 4, 2])"
# # 1000000 loops, best of 5: 1.45 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         6    0.000    0.000    0.000    0.000 lesson_4_task_1.py:17(isEven)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:24(even_num_indexes)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:25(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# # 3rd vers
# def even_num_indexes(data: list) -> list:
#     def recur(ind, data_res):
#         if data[ind] & 1 == 0:
#             data_res.append(ind)
#         ind += 1
#         if ind+1 > len(data):
#             return
#         recur(ind, data_res)
#         return
#     data_res = []
#     recur(0, data_res)
#     return data_res
#
# # python -m timeit -n 1000000 -s "import lesson_4_task_1" "lesson_4_task_1.even_num_indexes([8, 3, 15, 6, 4, 2])"
# # 1000000 loops, best of 5: 2.15 usec per loop
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:29(even_num_indexes)
#       6/1    0.000    0.000    0.000    0.000 lesson_4_task_1.py:31(recur)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         6    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('even_num_indexes([8, 3, 15, 6, 4, 2])')

# if __name__ == "__main__":
#     print(even_num_indexes([8, 3, 15, 6, 4, 2]))
#     assert(even_num_indexes([8, 3, 15, 6, 4, 2])) == [0, 3, 4, 5]
#     assert(even_num_indexes([7, 3, 15, 5, 7, 1])) == []
#     assert(even_num_indexes([7, 8, 15, 6, 4, 2])) == [1, 3, 4, 5]


'''
Вывод: наиболее быстрый и оптимальный 1-ый вариант, тк по сравнению с другими вариантами нет вызовов функций и рекурсии
'''
