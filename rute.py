from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/cofactor')
def cofactor():
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
