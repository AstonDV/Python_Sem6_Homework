# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат 
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Диапазон от 6 до 12
# Вывод: [1, 9, 13, 14, 19]

import os
clear = lambda: os.system('cls')

def usr_inpt(text) -> int:
    n = int(input(f'{text}: '))
    return n

def arr_build( quantity) -> list:
    result = list()
    for i in range(quantity):
        result.append(int(input(f'Введите {i+1} значение: ')))
    return result

def search_index(arr, min, max):
    for i in range(len(arr)):
        if min <= arr[i] <= max: print(i, end=' ')

def main():
    clear()
    # array = arr_build(usr_inpt('Введите количество элементов массива'))
    # min = usr_inpt('Введите нижнюю границу диапозона поиска')
    # max = usr_inpt('Введите верхнюю границу диапозона поиска')
    search_index(arr_build(usr_inpt('Введите количество элементов')), usr_inpt('Введите низ диапозона'), usr_inpt('Введите верх диапозона'))

main()
