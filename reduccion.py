def determinante(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1]) -
            a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0]) +
            a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))

def matriz_inversa(a):
    inversa = [[0, 0, 0] for _ in range(3)]

    inversa[0][0] = (a[1][1] * a[2][2] - a[1][2] * a[2][1])  
    inversa[0][1] = -(a[1][0] * a[2][2] - a[1][2] * a[2][0])  
    inversa[0][2] = (a[1][0] * a[2][1] - a[1][1] * a[2][0])  

    inversa[1][0] = -(a[0][1] * a[2][2] - a[0][2] * a[2][1])  
    inversa[1][1] = (a[0][0] * a[2][2] - a[0][2] * a[2][0])  
    inversa[1][2] = -(a[0][0] * a[2][1] - a[0][1] * a[2][0])  

    inversa[2][0] = (a[0][1] * a[1][2] - a[0][2] * a[1][1])  
    inversa[2][1] = -(a[0][0] * a[1][2] - a[0][2] * a[1][0])  
    inversa[2][2] = (a[0][0] * a[1][1] - a[0][1] * a[1][0]) 

    return inversa

def transponer_matriz(a):
    return [[a[j][i] for j in range(3)] for i in range(3)]

def inversa_por_cofactores(a):
    det = determinante(a)
    
    if det == 0:
        raise ValueError("La matriz no tiene inversa, su determinante es 0.")
    
    inversa = matriz_inversa(a)
    
    adjunta = transponer_matriz(inversa)
    
    inversa = [[round(adjunta[i][j] / det, 2) for j in range(3)] for i in range(3)]
    
    return inversa, round(det, 2)

def multiplicar_matriz_vector(a, c):
    resultado = [0, 0, 0]
    
    resultado[0] = round(a[0][0] * c[0] + a[0][1] * c[1] + a[0][2] * c[2], 2)
    resultado[1] = round(a[1][0] * c[0] + a[1][1] * c[1] + a[1][2] * c[2], 2)
    resultado[2] = round(a[2][0] * c[0] + a[2][1] * c[1] + a[2][2] * c[2], 2)

    return resultado


def reducir_matrices(A, C):
    A_inversa, determinante = inversa_por_cofactores(A)
    
    resultado = multiplicar_matriz_vector(A_inversa, C)
    
    x = resultado[0]
    Y = resultado[1]
    Z = resultado[2]
    
    return x, Y, Z, determinante

