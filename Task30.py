# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

import os
clear = lambda: os.system('cls')


def user_input(text) -> int:
    n = int(input(f'{text}: '))
    return n

def array_builder(start, step, quantity) -> list:
    result = [start]
    for i in range(quantity - 1):
        result.append(result[i] + step)
    print(result)

def main():
    clear()
    start = user_input('Введите стартовое значение')
    step = user_input('Введите шаг прогрессии')
    quantity = user_input('Введите количество элементов прогрессии')
    array_builder(start, step, quantity)

main()