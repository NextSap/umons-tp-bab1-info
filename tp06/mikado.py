'''
i : numéro de la baguette
bag : liste de baguettes restantes
jeu : liste d'enchevêtrement
'''

import random


def creerEnchevetrement(bag: list, i: int, max: int):
    listeEnchevetrement = []
    nombreEnchevetrement = random.randint(0, max - 1)

    for increment in range(nombreEnchevetrement):
        randomBag = bag[random.randint(0, len(bag) - 1)]
        if randomBag != i:
            enchevetrement = (randomBag, i)
            listeEnchevetrement.append(enchevetrement)

    return listeEnchevetrement


def creerMikado(bag: list):
    listeEnchevetrement = []

    for i in range(len(bag)):
        for k in creerEnchevetrement(bag, i, len(bag)):
            listeEnchevetrement.append(k)

    return listeEnchevetrement


def peutRetirer(i: int, bag: list, mikado: list):
    if i not in bag:
        return False

    for couple in mikado:
        if couple[0] == i:
            return False

    return True


def quelOrdre(bag: list, mikado: list):
    ordre = []
    list_couple = []
    len_bag_default = len(bag)

    m = mikado

    # while len(ordre) != len_bag_default:
    for i in range(1):
        for baguette in bag:
            print("Baguette:", baguette)
            # print("Baguette in ordre ?", baguette in ordre)
            if baguette not in ordre:
                #    print("Peut retirer baguette ?", peutRetirer(baguette, bag, m))
                if peutRetirer(baguette, bag, mikado):
                    #       print("Ajout de", baguette, "dans ordre")
                    ordre.append(baguette)
                    for couple in mikado:
                        print(len(mikado))
                        print(" *** Couple:", couple)
                        print("Couple in list_couple ?", couple in list_couple)

                        if couple in list_couple:
                            continue

                        print(couple[1], "=", baguette, "?", couple[1] == baguette)
                        if couple[1] == baguette:
                            print("Ajout de", couple, "dans list_couple")
                            list_couple.append(couple)
                            m.pop(mikado.index(couple))

        print("Ordre:", ordre)
        print("Mikado:", m)
        print("Couple:", list_couple)
        print()

    return ordre


def main():
    bag = [0, 1, 2, 3]
    mikado_ = [(0, 1), (0, 2), (1, 2)]
    mikado = creerMikado(bag)
    print(quelOrdre(bag, mikado_))


main()
