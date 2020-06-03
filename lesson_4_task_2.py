'''
2. Написать два алгоритма нахождения i-го по счёту простого числа. 
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. 
Проанализировать скорость и сложность алгоритмов.
'''

import math
import cProfile


def sieve(number: int) -> list:
    primes = []
    for i in range(2, number + 1):
        primes.append(i)

    i = 2
    while(i <= int(math.sqrt(number))):
        if i in primes:
            for j in range(i * 2, number + 1, i):
                if j in primes:
                    primes.remove(j)
        i = i+1

    return primes
# python -m timeit -n 1000 -s "import lesson_4_task_2" "lesson_4_task_2.sieve(1000)"
# 1000 loops, best of 5: 6.62 msec per loop
#          187 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:11(sieve)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {built-in method math.sqrt}
#        99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        74    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}


def prime(number: int) -> list:
    sieve = [True] * number
    for i in range(3, int(number ** 0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*((number-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3, number, 2) if sieve[i]]
# python -m timeit -n 1000 -s "import lesson_4_task_2" "lesson_4_task_2.prime(1000)"
# 1000 loops, best of 5: 37.8 usec per loop
#          5 function calls in 0.000 seconds
#    Ordered by: standard name
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:37(prime)
#         1    0.000    0.000    0.000    0.000 lesson_4_task_2.py:42(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


cProfile.run('prime(100)')

# if __name__ == "__main__":
#     assert(sieve(100)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
#                            31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
#     assert(prime(100)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
#                            31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

'''
Вывод: наиболее быстрый и оптимальный 2-ой вариант
'''
