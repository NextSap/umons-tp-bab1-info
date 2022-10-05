def droite(p1, p2):
    # ax + bx - c = 0
    # ax - y + c = 0
    vect_x = p2[0] - p1[0]
    vect_y = p2[1] - p1[1]

    # calcul de a
    if (p2[0] - p1[0]) == 0:
        return None
    a = (p2[1] - p1[1])/(p2[0] - p1[0])
    b = -1
    # injection d'un point pour avoir c
    c = -(a*p1[0] - p1[1])

    #b = -vect_x
    #a = vect_y

   # c = -(a * p2[0] + b * p2[1])

    return a, b, c


def appartient(d, p):
    a = d[0]
    b = d[1]
    c = d[2]

    x = p[0]
    y = p[1]
    return a * x + b * y - c == 0


def paralleles(d1, d2):
    return d1[0] * d1[1] - d2[1] * d2[0] == 0


def intersection(d1, d2):
    m1 = -d1[0]
    c1 = d1[2]
    m2 = -d2[0]
    c2 = d2[2]

    xi = (c1 - c2) / (m2 - m1)

    yi = m1 * xi + c1

    print((xi, yi))


def droite_normale(d, p):
    a = -1 / d[0]
    b = -p[1]

    c = -(a * p[0] + b * p[1])

    return a, b, c