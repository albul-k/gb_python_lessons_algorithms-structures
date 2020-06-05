'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
'''

from collections import deque

HEX_TO_DEC = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
              8: 8, 9: 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
DEC_TO_HEX = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7,
              8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def hex_sum(a: str, b: str) -> str:
    res = []
    hex_1, hex_2 = deque(a), deque(b)
    # if len(hex_1) > len(hex_2):
    #     while len(hex_1):
    #         _sum = hex_1[-1] + hex_2[-1]
    #         if _sum > 9
    #     for itm in hex_1[::-1]:

    # else:
    #     pass

    return ('').join(res)


def hex_mul(a: str, b: str) -> str:
    pass


inp_1 = input('Введите первое шестнадцатеричное число: ')
inp_2 = input('Введите второе шестнадцатеричное число: ')

print(hex_sum(inp_1, inp_2))

# print(hex(int(inp_1, 16) + int(inp_2, 16)))

# if __name__ == "__main__":
#     assert(hex_sum('A2', 'C4F')) ==  ['C', 'F', '1']
