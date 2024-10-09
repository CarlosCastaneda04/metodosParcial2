def sumar_matrices(mat1, mat2):
    resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            resultado[i][j] = mat1[i][j] + mat2[i][j]
    return resultado