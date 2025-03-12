#SQL ----> Query
#El traductor de python a SQL es SQLAlchemy
from extensions import db_s

#Importar modulo para hashear contraseñas
from werkzeug.security import generate_password_hash, check_password_hash
#generete_password_hash('contraseña') ----> Hashea la contraseña
#check_password_hash('contraseña_hasheada', 'contraseña') ----> Verifica si la contraseña es correcta

#Vamos a crear un modelo 
# Un modelo es un plano de como se ve la tabla en la base de datos
class Usuario(db_s.Model):
    #Nombre de la tabla
    __tablename__ = 'usuarios'
    #Columnas de la tabla
    id = db_s.Column(db_s.Integer, primary_key=True)
    name = db_s.Column(db_s.String(100), nullable=True)  # 👈 Esto indica que no puede ser NULL
    email = db_s.Column(db_s.String(100), unique=True, nullable=False)
    password = db_s.Column(db_s.String(100), nullable=False)

    #Metodos
    #Metodo para cifrar constraseña
    def hashear_password(self, password_original): 
        self.password = generate_password_hash(password_original)

    def verificar_password(self, password_plano):
        return check_password_hash(self.password, password_plano)

    def save(self):
        #Creamos una conexion a la base de datos para añadir un nuevo usuario
        db_s.session.add(self)

        #Guardamos los cambios
        db_s.session.commit()
        
    def delete(self):
        #Creamos una conexion a la base de datos
        db_s.session.delete(self)

        #Guardamos los cambios
        db_s.session.commit()