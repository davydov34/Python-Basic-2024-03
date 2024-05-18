"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*args):
    num_list = []
    for arg in args:
        num_list.append(arg * arg)
    return num_list

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number = 0):
    if number <= 1:
        print("Аргуемент не задан или меньше единицы!")
        return None
    not_is_prime = True
    for i in range(2, number // 2+1):
        if number % i == 0:
            not_is_prime = False
    return not_is_prime

def filter_numbers(num_list = [], key_word = ""):
    match key_word:
        case "odd":
             return list(filter(lambda x: (x % 2) == 1, num_list))
        case "even":
             return list(filter(lambda x: (x % 2) == 0, num_list))
        case "prime":
             return list(filter(is_prime, num_list))
        case _:
            print("Параметр операции задан неверно! ")

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """