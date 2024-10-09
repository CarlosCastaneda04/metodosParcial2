def calcular_determinante_y_inversa(a):
    dP = a[0][0]*a[1][1]*a[2][2] + a[1][0]*a[2][1]*a[0][2] + a[2][0]*a[0][1]*a[1][2]
    dS = a[0][2]*a[1][1]*a[2][0] + a[1][2]*a[2][1]*a[0][0] + a[2][2]*a[0][1]*a[1][0]
    det = dP - dS

    if det == 0:
        return None, "La matriz no tiene inversa (determinante = 0)"

    aCof = [[0]*3 for _ in range(3)]
    #primera fila
    aCof[0][0] = a[1][1]*a[2][2] - a[1][2]*a[2][1]
    aCof[0][1] = -(a[1][0]*a[2][2] - a[2][0]*a[1][2])
    aCof[0][2] = a[1][0]*a[2][1] - a[1][1]*a[2][0]
    #segunda fila
    aCof[1][0] = -(a[0][1]*a[2][2] - a[2][1]*a[0][2])
    aCof[1][1] = a[0][0]*a[2][2] - a[2][0]*a[0][2]
    aCof[1][2] = -(a[0][0]*a[2][1] - a[2][0]*a[0][1])
    #tercera fila
    aCof[2][0] = a[0][1]*a[1][2] - a[1][1]*a[0][2]
    aCof[2][1] = -(a[0][0]*a[1][2] - a[1][0]*a[0][2])
    aCof[2][2] = a[0][0]*a[1][1] - a[1][0]*a[0][1]

    aT = [[aCof[j][i] for j in range(3)] for i in range(3)]

    invM = [[round(aT[i][j] / det, 2) for j in range(3)] for i in range(3)]

    return invM, det
