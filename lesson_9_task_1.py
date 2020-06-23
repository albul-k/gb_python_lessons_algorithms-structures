'''
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.
'''

import hashlib


def count_dif_substr(data: str) -> any:
    if len(data) == 0:
        return 0

    count, count_hash = {}, {}
    i = 1
    while i < len(data):
        for k in range(0, len(data)):
            substr = data[k:k+i]
            substr_hash = hashlib.sha1(substr.encode('utf-8')).hexdigest()
            if count_hash.get(substr_hash) is None:
                count_hash[substr_hash] = 1
            else:
                count_hash[substr_hash] += 1
            count[substr] = count_hash[substr_hash]

            if k + i >= len(data):
                break
        i += 1

    return count, len(count)


if __name__ == "__main__":
    result = count_dif_substr('aaabbb')
    print(f'Словарь подстрок:\n{result[0]}\n')
    print(f'Количество уникальных подстрок: {result[1]}')
