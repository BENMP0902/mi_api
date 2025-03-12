
#rA2_93#7tK2Meaj
# Flask es la librería que nos ayudará a crear un servidor para nuestra API
from flask import Flask
# Importamos la función que se encarga de cargar las rutas
from routes import cargar_rutas

from extensions import db_s

# flask: Librería
# Flask: módulo (clase)

# Vamos a crear un objeto que contendrá los métodos necesarios para nuestro servidor
app = Flask(__name__)

#1. Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres.atgxanqwsnttopfxzlwm:rA2_93#7tK2Meaj@aws-0-us-west-1.pooler.supabase.com:6543/postgres'


#2. Desactivar el track modification
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_s.init_app(app)


#Cargamos las rutas desde el archivo routes.py
cargar_rutas(app)

app.run(port=8000, debug=True)
