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
            # Capturar los valores de la matriz desde el formulario
            a = [
                [int(request.form['a00']), int(request.form['a01']), int(request.form['a02'])],
                [int(request.form['a10']), int(request.form['a11']), int(request.form['a12'])],
                [int(request.form['a20']), int(request.form['a21']), int(request.form['a22'])]
            ]

            # Calcula el determinante y la inversa
            invM, det = calcular_determinante_y_inversa(a)

            print(f"Determinante: {det}")

            # Si el determinante es 0, mostrar mensaje de error
            if det == 0:
                error = "La matriz no tiene inversa porque el determinante es 0."
                return render_template('cofactor.html', error=error)

            # Si hay una inversa, mostrar los resultados
            if invM:
                return render_template('cofactor.html', invM=invM, det=det)
            else:
                error = "Error en el cálculo de la matriz inversa."
                return render_template('cofactor.html', error=error)
        except Exception as e:
            # Maneja cualquier error en el cálculo o formato
            error = f"Hubo un error procesando la matriz: {e}"
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
