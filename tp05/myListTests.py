from myList import *
import math

from myList import _range, _filter

# print(map(math.sqrt, []) == [])
# print(map(math.sqrt, [2.0, 4.0, 6.0, 100.0]) == [1.4142135623730951, 2.0, 2.449489742783178, 10.0])
# print(map(str.upper, list("hello")) == ["H", "E", "L", "L", "O"])

# print(_filter(is_prime, range(20)))  # == [2, 3, 5, 7, 11, 13, 17, 19]
# print(_filter(str.isalpha, list("r2d2")))  # == ["r", "d"])

# print(reduce(math.pow, [2, 2]))  # 4.0
# print(reduce(math.pow, [2, 3, 4]))  # 4096.0
# print(reduce(math.pow, [2, 3, 4, 2]))  # 16777216.0

# print(prime_numbers(1))  # [2]
# print(prime_numbers(12))  # [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

# print(is_prime(1))  # False
# print(is_prime(2))  # True
# print(is_prime(3))  # True
# print(is_prime(33))  # False

# insert([], 1)  # [1]
# insert(list(range(6)), -1)  # [-1, 0, 1, 2, 3, 4, 5]
# insert(list(range(6)), 3)  # [0, 1, 2, 3, 3, 4, 5]
# insert(list(range(6)), 10)  # [0, 1, 2, 3, 4, 5, 10]

# print(produit_matriciel([[2, 0, 1], [3, 6, 2]], [[1, 5], [2, 6], [3, 7]]))  # [[5, 17], [21, 65]]
# print(produit_matriciel([[1, 5], [2, 6], [3, 7]], [[2, 0, 1], [3, 6, 2]]))  # [[17, 30, 11], [22, 36, 14], [27, 42, 17]]
# print(produit_matriciel([[1.0, 2.5]], [[3.0], [4.5]]))  # 14.25
# print(produit_matriciel([[1.0, 2.5]], [[3.0, 4.5]]))  # None
# print(produit_matriciel([[1, 5], [2, 6], [3, 7]], [[1, 5], [2, 6], [3, 7]]))  # None
