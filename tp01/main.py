import math
import random
import string


def reverse():
    a = 1
    b = 2
    c = 3
    d = 4

    a_old = a
    a = d
    b_old = b
    b = c
    c = b_old
    d = a_old

    print(a, b, c, d)


def volume_sphere(air):
    print(4 / 3 * math.pi * air ** 2)


def book_price(amount):
    shipping_price = 0
    price = 24.95 * 1.40
    if amount == 1:
        shipping_price = 3
    if amount >= 1:
        shipping_price = 3 + (amount - 1) * 0.75

    print("prix: " + price + "\nshipping_prince: " + shipping_price)


def km_to_miles(km, seconds):
    miles = km / 1.61
    time_in_hours = seconds / 3600

    print(miles / time_in_hours)


def walking():
    start_time_walk_minutes = 6 * 60 + 52

    normal_walk_seconds = 8 * 60 + 15
    speeder_walk_seconds = 7 * 60 + 12

    walk_total_seconds = 2 * normal_walk_seconds + 3 * speeder_walk_seconds

    walk_total_minutes = walk_total_seconds / 60

    end_time_walk = start_time_walk_minutes + walk_total_minutes

    print(str(int(end_time_walk // 60)) + ":" + str(int(end_time_walk % 60)))


def typeO():
    a = 14 - 14
    b = 1 + 6.9
    c = 1.0 + 2.0
    d = 18 / 7 + 1
    e = ((3 + 2) * 2.5) / 4 * 2
    f = 3 ** (-1 / 2)
    g = 0 * 0.0

    print("Il y a " + 31 + "jours en janvier")


def randomA():
    while True:
        listRandom = []
        for i in range(random.randint(10, 24)):
            listRandom.append(random.randint(0, 9))
            listRandom.append(random.choice(string.ascii_letters))
        print(listRandom)


randomA()
