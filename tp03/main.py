import math

from uturtle import *

bob = umonsTurtle()

bob.speed(0)


def triangle(t, n, size):
    if n == 0:
        moveForward(t, size)
        turnLeft(t, 120)
        moveForward(t, size)
        turnLeft(t, 120)
        moveForward(t, size)
        turnLeft(t, 120)
    else:
        triangle(t, n - 1, size / 2)
        moveForward(t, size / 2)
        triangle(t, n - 1, size / 2)
        moveBackward(t, size / 2)
        turnLeft(t, 60)
        moveForward(t, size / 2)
        turnRight(t, 60)
        triangle(t, n - 1, size / 2)
        turnLeft(t, 60)
        moveBackward(t, size / 2)
        turnRight(t, 60)


def koch(t, x, seuil):
    if seuil == 0:
        moveForward(t, x)
    else:
        koch(t, x / 3, seuil - 1)
        turnLeft(t, 60)
        koch(t, x / 3, seuil - 1)
        turnRight(t, 120)
        koch(t, x / 3, seuil - 1)
        turnLeft(t, 60)
        koch(t, x / 3, seuil - 1)


def flocon(t, x, seuil):
    if seuil == 0:
        moveForward(t, x)
    else:
        for i in range(4):
            koch(t, x / 3, seuil - 1)
            turnRight(t, 90)


def carre(t, x, seuil):
    if x < seuil:
        moveForward(t, x)
    else:
        carre(t, x / 4, seuil)
        turnLeft(t)
        carre(t, x / 4, seuil)
        turnRight(t)
        carre(t, x / 4, seuil)
        turnRight(t)
        carre(t, x / 4, seuil)
        turnLeft(t)
        carre(t, x / 4, seuil)


turnLeft(bob)


def arbre(t, x, a, n):
    if n == 0:
        moveForward(t, x)
        moveBackward(t, x)
    else:
        moveForward(t, x)
        turnRight(t, a/2)
        arbre(t, x * math.sqrt(2) / 2, a, n - 1)
        turnLeft(t, a)
        arbre(t, x * math.sqrt(2) / 2, a, n - 1)
        turnRight(t, a/2)
        moveBackward(t, x)

    """
    t = tortue
    x = longueur du tronc
    a = angle
    n = profondeur (nombre de récursion)
    """


arbre(bob, 100, 60, 4)

wait()
