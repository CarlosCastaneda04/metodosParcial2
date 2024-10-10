from flask import Flask, render_template, request, jsonify
from cofactor import calcular_determinante_y_inversa  # Importa la función desde cofactor.py
from multiplicacion import multiplicar_matrices  # Importa la función desde multiplicacion.py
from reduccion import reducir_matrices  # Importa la función desde reduccion.py
from regresion import calcular_regresion, graficar_regresion  # Asegúrate de que estas funciones existan en regresion.py
from resta import restar_matrices  # Importa la función de resta de matrices
import os  # Importa la biblioteca os para manejar rutas de archivos

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

# Ruta para el cálculo del determinante e inversa
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

# Ruta para la multiplicación de matrices
@app.route('/multiplicacion')
def multiplicacion():
    return render_template('multiplicacion.html')

# Ruta para procesar la multiplicación de matrices
@app.route('/multiplicar', methods=['POST'])
def multiplicar():
    try:
        # Obtener matrices desde el request
        datos = request.get_json()
        mat1 = datos['mat1']
        mat2 = datos['mat2']

        # Verificar que ambas matrices sean de 3x3 y no haya valores vacíos o no numéricos
        for fila in mat1 + mat2:
            if len(fila) != 3 or not all(isinstance(valor, int) for valor in fila):
                return jsonify({'error': 'Todos los campos de las matrices deben estar completos y ser números enteros.'}), 400

        # Multiplicar matrices
        resultado = multiplicar_matrices(mat1, mat2)

        # Enviar el resultado como JSON
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/reduccion')
def reduccion():
    return render_template('reduccion.html')

@app.route('/reduccion', methods=['GET', 'POST'])
def reduccion_view():
    if request.method == 'POST':
        try:
            # Obtener los datos enviados en formato JSON
            datos = request.get_json()
            print(f"Datos recibidos: {datos}")  # Esto imprimirá los datos en la terminal
            
            matrizA = datos['matrizA']
            vectorC = datos['vectorC']

            # Realizar la operación de reducción de matrices
            x, Y, Z, determinante = reducir_matrices(matrizA, [fila[0] for fila in vectorC])

            # Retornar los resultados en formato JSON
            return jsonify({'x': x, 'Y': Y, 'Z': Z, 'determinante': determinante})

        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template('reduccion.html')

@app.route('/regresion')
def regresion():
    return render_template('regresion.html')

# Ruta para la regresión lineal
@app.route('/calcular_regresion', methods=['POST'])
def calcular_regresion_view():
    try:
        datos = request.get_json()
        xValores = datos['xValores']
        yValores = datos['yValores']
        
        # Realizar el cálculo de la regresión
        m, b, r = calcular_regresion(xValores, yValores)
        
        # Graficar la regresión y guardar la imagen
        output_path = os.path.join('static', 'grafica.png')
        graficar_regresion(xValores, yValores, m, b, r, output_path)
        
        # Retornar los resultados en formato JSON
        return jsonify({'m': m, 'b': b, 'r': r})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/resta')
def resta():
    return render_template('resta.html')

# Ruta para procesar la resta de matrices
@app.route('/restar_matrices', methods=['POST'])
def restar_matrices_view():
    try:
        # Obtener matrices desde el request
        datos = request.get_json()
        mat1 = datos['mat1']
        mat2 = datos['mat2']

        # Verificar que ambas matrices sean de 3x3 y no haya valores vacíos o no numéricos
        for fila in mat1 + mat2:
            if len(fila) != 3 or not all(isinstance(valor, (int, float)) for valor in fila):
                return jsonify({'error': 'Todos los campos de las matrices deben estar completos y ser números válidos.'}), 400

        # Restar matrices
        resultado = restar_matrices(mat1, mat2)

        # Enviar el resultado como JSON
        return jsonify(resultado)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/suma')
def suma():
    return render_template('suma.html')

@app.route('/rute')
def rute():
    return render_template('rute.html')

if __name__ == '__main__':
    app.run(debug=True)
