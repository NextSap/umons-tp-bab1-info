from mikado import *

# tests peutRetirer()

bag = [0, 1, 2, 3]
mikado = creerMikado(bag)

for i in bag:
    print(peutRetirer(i, bag, mikado), i)
