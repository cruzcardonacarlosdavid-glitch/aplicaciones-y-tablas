from sqlite3 import *

base_de_datos = connect("tabla.db")
cr = base_de_datos.cursor()

def crearTabla():
    cr.execute('''
        CREATE TABLE IF NOT EXISTS estudiantes(
        ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Nombre TEXT NOT NULL,
        Edad TEXT NOT NULL,
        Stock TEXT NOT NULL);
        ''')
    base_de_datos.commit()
    print("Creado")

