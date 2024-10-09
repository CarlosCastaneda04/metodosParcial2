import matplotlib.pyplot as plt

def calcular_regresion(x, y):
    if len(x) != len(y):
        raise ValueError("Las listas de X e Y deben tener la misma longitud")
    
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y2 = sum(yi ** 2 for yi in y)

    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x ** 2)
    x_media = sum_x / n
    y_media = sum_y / n

    b = y_media - m * x_media

    r_numerador = n * sum_xy - sum_x * sum_y
    r_denominador = ((n * sum_x2 - sum_x ** 2) * (n * sum_y2 - sum_y ** 2)) ** 0.5
    r = r_numerador / r_denominador if r_denominador != 0 else 0

    m = round(m, 2)
    b = round(b, 2)
    r = round(r, 4)

    return m, b, r

def graficar_regresion(x, y, m, b, r, output_path):
    plt.scatter(x, y, color='red', label='Datos')
    plt.plot(x, [b + m * xi for xi in x], label=f'y = {b} + {m}x', color='blue')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Regresión Lineal por Mínimos Cuadrados (r = {r})')
    plt.legend()
    plt.savefig(output_path)
    plt.close()

def main():
    x = [1, 2, 3, 4, 5]  
    y = [2, 4, 5, 4, 5]  
    
    m, b, r = calcular_regresion(x, y)
    
    print(f"La ecuación de la recta es: y = {b} + {m}x")
    print(f"Coeficiente de correlación (r): {r}")
    
    output_path = 'grafica.png'
    graficar_regresion(x, y, m, b, r, output_path)
    print(f"Gráfica guardada en: {output_path}")

if __name__ == "__main__":
    main()
