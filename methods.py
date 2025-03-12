# Un archivo que contiene todas las acciones que un usiario puede realizar
from models import Usuario

#Metodo para que el usuario pueda crear una cuenta
def crear_cuenta(nombre, correo, password):

    usuario_existente = Usuario.query.filter_by(email=correo).first()
    #Revisamos si la quey es diferente a None
    if usuario_existente is not None:
        print('El correo ya existe')
        return{'status': 'error', 'error': 'La cuenta ya esta registrada'}

    #Esto solo se ejecuta si el usuario no existe en la db
    print(f"Intentando crear cuenta con: {nombre}, {correo}, {password}")  # 👈 Agrega esto para depuración
    nuevo_usuario = Usuario(name = nombre, email = correo)

    nuevo_usuario.hashear_password(password_original=password)
 

    #Guardamos el nuevo usuario en la base de datos
    nuevo_usuario.save()

    return {'status': 'ok', 'email': correo}

def iniciar_sesion(correo, password):

    #VAriable que contenga usuarios filtrados por un parametro
    usuarios_existentes = Usuario.query.filter_by(email = correo).first()

    #1. Si el usuario existe puede iniciar sesion

    #2. Si el ussuario no existe no puede iniciar sesion

    #Si el ususario no existe
    if usuarios_existentes is None:
        print('La cuenta no existe')
        return{'status': 'error', 'error': 'La cuenta no existe'}

    #Si la contraseña del formulario esta en la db 
    
    if usuarios_existentes.verificar_password(password_plano = password):
        pass