def multiplicar_matrices(mat1, mat2):
    resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            resultado[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(3))
    return resultado
