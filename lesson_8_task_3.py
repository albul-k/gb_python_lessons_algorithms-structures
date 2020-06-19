'''
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
'''

from collections import defaultdict


def dfs(graph: dict, start: int, visited: list):

    # пометим текущую вершину посещенной и выведем ее
    visited[start] = True
    print(start, end=' ')

    # рекурсивно обходим вершины
    for i in graph[start]:
        if visited[i] == False:
            dfs(graph, i, visited)


# функция генерации графа
def get_graph(num: int) -> dict:
    graph = defaultdict(list)
    for i in range(num):
        for k in range(num):
            # добавление ребра в массив
            # поскольку в задаче нет никаких упоминаний о связях вершин, то связываем все вершины со всеми
            graph[i].append(k)
    return graph


if __name__ == "__main__":
    num = int(input(f'Введите количество точек: '))
    graph = get_graph(num)
    print(graph)

    start = int(input(f'Введите стартовую точку: '))
    visited = [False] * (max(graph)+1)
    dfs(graph, start, visited)
