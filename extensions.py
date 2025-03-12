#Este archivo evitara las importaciones circulares

from flask_sqlalchemy import SQLAlchemy

 #Creamos un objeto de tipo SQLAlquemy que va a controlar toda la base de datos
db_s = SQLAlchemy()