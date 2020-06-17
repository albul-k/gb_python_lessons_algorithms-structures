'''
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
'''


def count_handshakes(graph: list) -> int:
    count = 0
    for i in graph:
        for k in i:
            count += 1
    return count


if __name__ == "__main__":
    assert(count_handshakes([[1], [1]])) == 2, '2 друга'
    assert(count_handshakes([[1, 1], [1, 1], [1, 1]])) == 6, '3 друга'

    N = int(input('Введите количество друзей: '))
    graph = [[1 for i in range(N-1)] for k in range(N)]
    # print(*graph, sep='\n')

    print(f'Количество рукопожатий: {count_handshakes(graph)}')
