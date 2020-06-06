'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого — цифры числа.
'''

from collections import deque

HEX_TO_DEC = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
DEC_TO_HEX = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def hex_to_dec(num: str) -> int:
    num_dec = 0
    for ind, value in enumerate(num[::-1]):
        if value.isdigit():
            num = int(value)
        else:
            num = HEX_TO_DEC[value.capitalize()]
        num_dec += num * (16 ** ind)
    return num_dec


def dec_to_hex(num: str) -> list:
    res = deque()
    while num > 0:
        _t = num % 16
        if _t >= 10:
            _t = DEC_TO_HEX[_t]
        res.appendleft(str(_t))
        num = num // 16
    return list(res)


def hex_sum(a: str, b: str) -> str:
    return dec_to_hex(hex_to_dec(a) + hex_to_dec(b))


def hex_mul(a: str, b: str) -> str:
    return dec_to_hex(hex_to_dec(a) * hex_to_dec(b))


inp_1 = input('Введите первое шестнадцатеричное число: ')
inp_2 = input('Введите второе шестнадцатеричное число: ')

print(f'Результат сложения: {hex_sum(inp_1, inp_2)}')
print(f'Проверка: {hex(int(inp_1, 16) + int(inp_2, 16))}')

print(f'\nРезультат умножения: {hex_mul(inp_1, inp_2)}')
print(f'Проверка: {hex(int(inp_1, 16) * int(inp_2, 16))}')

if __name__ == "__main__":
    assert(hex_sum('A2', 'C4F')) == ['C', 'F', '1']
    assert(hex_mul('A2', 'C4F')) == ['7', 'C', '9', 'F', 'E']
