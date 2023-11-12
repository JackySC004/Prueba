''' from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/ruta1', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        correo= request.form['correo']
        print (correo)

    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True) '''

from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/ruta2', methods=['GET', 'POST'])
def index():
    variable_servidor="Buenas tetas digo tardes"
    mensaje=None

    if request.method == 'POST':
        contraseña = request.form['contraseña']
        mensaje = request.form['contraseña']

    return render_template('index.html', variable_servidor=variable_servidor, mensaje=mensaje)


if __name__=='__main__':
    app.run(debug=True)