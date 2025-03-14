#Este archivo va a almacenar unica y exclusivamente las rutas de nuestra aplicación
from flask import Flask, render_template, request, redirect, url_for, make_response

from methods import crear_cuenta, iniciar_sesion, encontrar_todos_los_usuarios

from flask_jwt_extended import decode_token, verify_jwt_in_request, get_jwt_identity

firma = 'cvVElgt1FXxAIgLKrm0y07oWcO1L76'
def cargar_rutas(app):
    # Esta es una ruta
    @app.route('/')
    def pagina():
        
        logged = False

        try:
            verify_jwt_in_request()  # Verifica que la cookie con el token sea válida
            logged = True 
            

        except Exception as e:
            logged = False
            print(e)

        return render_template('index.html', logged=logged)

    # Esta es otra ruta
    @app.route('/login')
    def login():

        resultado = request.args.get('status')
        return render_template('login.html', estado = resultado)

    # Esta es otra ruta
    @app.route('/signup')
    def signup():

        resultado = request.args.get('status')


        return render_template('signup.html', estado = resultado)

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
        
        respuesta_login = iniciar_sesion(correo, password)
        
        if respuesta_login['status'] == 'error':
            return redirect(url_for("login", status = respuesta_login['status']))
        
        #Si lo anterior no se ejecuta tenemos un token
        respuesta = make_response(redirect(url_for('pagina')))

        respuesta.set_cookie('access_token_cookie', respuesta_login['token'], secure=True, httponly=True, max_age=180)

        
        return respuesta


    # Interceptamos la informacion del signup
    @app.route('/datos_crear_cuenta', methods=['POST'])
    def obtener_datos_cuenta():
        nombre = request.form.get('name')
        correo = request.form.get('email')
        password = request.form.get('password')

        print(f'''
            Nombre: {nombre}
            Correo: {correo}
            Password: {password}
        ''')

        respuesta_signup = crear_cuenta(nombre, correo, password)

        print(respuesta_signup)

        if respuesta_signup['status'] == 'error':
            return redirect(url_for('signup', status=respuesta_signup['status']))

        return redirect(url_for('pagina', status=respuesta_signup['status']))
    


    @app.route('/error')
    def pantalla_error():
        return render_template('error.html')
    
    
    @app.route('/usuario')
    def pantalla_usuario():
        try:
            verify_jwt_in_request()  # Verifica que la cookie con el token sea válida
            usuario_actual = get_jwt_identity()  # Obtiene la identidad del usuario
            print(f"Usuario autenticado: {usuario_actual}")
            return render_template('user.html', nombre=usuario_actual)

        except Exception as e:
            print(f'Error al verificar JWT: {str(e)}')
            return redirect(url_for('login'))

    @app.route('/logout')
    def cerrar_sesion():
        respuesta = make_response(redirect(url_for('pagina')))
        respuesta.set_cookie('access_token_cookie', '')

        return respuesta