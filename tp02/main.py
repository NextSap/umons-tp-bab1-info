prixTest = 34
tupleTest = [3, 0, 0, 0, 0]


# Donné : 60
# A rendre : 26
# 1x 20
# 1x 5
# 1x 1


def rendreMonnaie(prix, billets_tuple: tuple):
    nombre_20, nombre_10, nombre_5, nombre_2, nombre_1 = billets_tuple

    a_rendre_20, a_rendre_10, a_rendre_5, a_rendre_2, a_rendre_1 = 0, 0, 0, 0, 0

    monnaie_total = nombre_20 * 20 + nombre_10 * 10 + nombre_5 * 5 + nombre_2 * 2 + nombre_1 * 1

    if prix > monnaie_total:
        print("Il n'y a pas assez d'argent pour acheter cet article")
        return

    a_rendre = monnaie_total - prix

    reste = a_rendre

    if reste >= 20:
        a_rendre_20 = reste // 20
        reste = reste - ((reste // 20) * 20)

    if reste >= 10:
        a_rendre_10 = reste // 10
        reste = reste - ((reste // 10) * 10)

    if reste >= 5:
        a_rendre_5 = reste // 5
        reste = reste - ((reste // 5) * 5)

    if reste >= 2:
        a_rendre_2 = reste // 2
        reste = reste - ((reste // 2) * 2)

    if reste >= 1:
        a_rendre_1 = reste // 1
        reste = reste - ((reste // 1) * 1)

    print("20: " + str(a_rendre_20))
    print("10: " + str(a_rendre_10))
    print("5: " + str(a_rendre_5))
    print("2: " + str(a_rendre_2))
    print("1: " + str(a_rendre_1))