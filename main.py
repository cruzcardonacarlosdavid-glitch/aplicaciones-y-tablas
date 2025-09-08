from sqlite3 import *
from tkinter import *
from tkinter import ttk

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

cr.execute('''SELECT * FROM estudiantes;''')
datos =cr.fetchall()

def rellenar_tabla(tabla):
    for dato in datos:
        tabla.insert("", "end", values=dato)

#Iniciamos la aplicacion
app = Tk()
app.title("Aplicacion y tablas")

#Creamos el widget Treeview
tabla = ttk.Treeview(app, columns=("ID", "Nombre", "Edad","Stock"), show="headings")

#Colocamos sus encabezados
tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.heading("Stock", text ="Stock")

#Ajustar el ancho de las columnas
for col in tabla["columns"]:
    tabla.column(col, anchor="center", width=100)



#Empaquetar el widget Treeview
tabla.pack()




#Se invocan los métodos para ejemplificar
rellenar_tabla(tabla)




#Se inicia el bucle principal
app.mainloop()