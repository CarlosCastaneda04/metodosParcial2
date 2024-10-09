from flask import Flask, render_template, request
from cofactor import calcular_determinante_y_inversa  # Importa la función desde cofactor.py

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

# Asegúrate de que el endpoint y la función sean ambos 'cofactor'
@app.route('/cofactor', methods=['GET', 'POST'])
def cofactor():
    if request.method == 'POST':
        try:
            # Captura la matriz enviada por el formulario
            matriz = request.form['matriz']
            # Convierte la matriz de texto a una lista de listas de enteros
            filas = matriz.splitlines()
            a = [list(map(int, fila.split(','))) for fila in filas]

            # Calcula el determinante y la inversa
            invM, det = calcular_determinante_y_inversa(a)

            if invM:
                return render_template('cofactor.html', invM=invM, det=det)
            else:
                error = det  # Este es el mensaje de error si el determinante es 0
                return render_template('cofactor.html', error=error)
        except Exception as e:
            # Maneja cualquier error en el cálculo o formato
            error = "Hubo un error procesando la matriz. Asegúrate de ingresar una matriz 3x3 correctamente."
            return render_template('cofactor.html', error=error)

    return render_template('cofactor.html')

@app.route('/multiplicacion')
def multiplicacion():
    return render_template('multiplicacion.html')

@app.route('/reduccion')
def reduccion():
    return render_template('reduccion.html')

@app.route('/regresion')
def regresion():
    return render_template('regresion.html')

@app.route('/resta')
def resta():
    return render_template('resta.html')

@app.route('/suma')
def suma():
    return render_template('suma.html')

@app.route('/rute')
def rute():
    return render_template('rute.html')

if __name__ == '__main__':
    app.run(debug=True)
