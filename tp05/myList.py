import itertools


def map(fun, array: map):
    new_array = []
    for i in range(len(array)):
        new_array.append(fun(array[i]))
    return new_array


def _filter(fun, array: map):
    new_array = []
    for i in array:
        if fun(i):
            new_array.append(i)
    return new_array


def reduce(fun, array: map):
    if len(array) == 0:
        return None

    var = array[0]
    for i in range(len(array)):
        if i != len(array) - 1:
            var = fun(var, array[i + 1])

    return var


def is_prime(number):
    dividers = []
    for i in range(number + 1):
        if i != 0:
            if str((number / i))[-1] == "0":
                dividers.append(i)

    return len(dividers) == 2


def _range(number: int):
    new_array = []
    for i in range(number):
        new_array.append(i)
    return new_array


def prime_numbers(n):
    prime_numbers_list = []
    i = 0
    while len(prime_numbers_list) != n:
        if is_prime(i):
            prime_numbers_list.append(i)
        i += 1

    return prime_numbers_list


def insert(seq: list, n):
    seq.append(n)
    seq.sort()
    print(seq)


def produit_matriciel(premiere_matrice, deuxieme_matrice):
    to_addition = []

    columns_premier_matrice = len(premiere_matrice[0])
    lines_deuxieme_matrice = len(deuxieme_matrice)

    matrice_size = len(premiere_matrice) * len(deuxieme_matrice[0])

    lines_matrice_len = len(premiere_matrice)

    if columns_premier_matrice != lines_deuxieme_matrice:
        return None

    for k in range(lines_matrice_len):  # 2
        for number1 in range(len(premiere_matrice)):  # 3
            for number2 in range(len(deuxieme_matrice)):  # 2
                i = premiere_matrice[k][number2]
                j = deuxieme_matrice[number2][number1]
                to_addition.append(i * j)

    split_in_list_to_addition = [len(to_addition) // matrice_size] * matrice_size
    iter_list = iter(to_addition)
    matrice_before_addition = [list(itertools.islice(iter_list, elem))
                               for elem in split_in_list_to_addition]

    matrice_after_addition = []
    for i in matrice_before_addition:
        addition = 0
        for k in i:
            addition += k
        matrice_after_addition.append(addition)

    split_in_matrice = [len(matrice_after_addition) // lines_matrice_len] * lines_matrice_len
    iter_list = iter(matrice_after_addition)
    final_matrice = [list(itertools.islice(iter_list, elem))
                     for elem in split_in_matrice]

    return final_matrice
