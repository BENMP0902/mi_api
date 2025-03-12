#Este archivo va a almacenar unica y exclusivamente las rutas de nuestra aplicación
from flask import Flask, render_template, request, redirect, url_for 

from methods import crear_cuenta, iniciar_sesion

def cargar_rutas(app):
    # Esta es una ruta
    @app.route('/')
    def pagina():
        return render_template('index.html')

    # Esta es otra ruta
    @app.route('/login')
    def login():
        return render_template('login.html')

    # Esta es otra ruta
    @app.route('/signup')
    def signup():
        return render_template('signup.html')

    # Esta ruta va a manejar la información
    #Este metodo solo funciona para el inicio de sesion
    @app.route('/manipulacion', methods=['POST'])
    def manipular_datos():
        correo = request.form.get('email')
        password = request.form.get('password')

        print(f'''
            Correo: {correo}
            Contraseña: {password}
    ''')
        
        iniciar_sesion()

        return redirect(url_for("pagina"))


    # Interceptamos la informacion del signup
    @app.route('/datos_crear_cuenta', methods=['POST'])
    def datos_crear_cuenta():
        nombre = request.form.get('name')
        correo = request.form.get('email')
        password = request.form.get('password')

        print(f'''
            Nombre: {nombre}
            Correo: {correo}
            Contraseña: {password}
        ''')

        crear_cuenta(nombre, correo, password)

        return redirect(url_for("pagina"))