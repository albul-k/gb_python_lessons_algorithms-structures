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
    file_data = 'data.txt'
    try:
        with open(file_data, 'r', encoding='UTF-8') as f_in:
            data = list(map(lambda itm: int(itm), f_in.readline().split()))
    except IOError:
        print("Произошла ошибка ввода/вывода файла")

    even_num_indexes(data)

# проанализировать при тех же условиях не удалось из-за RecursionError
