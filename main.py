from sqlite3 import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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

def limpiar_tabla(tabla):
    for item in tabla.get_children():
            tabla.delete(item)

app = Tk()
app.title("Aplicacion y tablas")


tabla = ttk.Treeview(app, columns=("ID", "Nombre", "Edad","Stock"), show="headings")


tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.heading("Stock", text ="Stock")


for col in tabla["columns"]:
    tabla.column(col, anchor="center", width=100)

tabla.pack()


rellenar_tabla(tabla)
tabla.after(2000, lambda: limpiar_tabla(tabla))


app.mainloop()