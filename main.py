from sqlite3 import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Notebook

base_de_datos = connect("tabla.db")
cr = base_de_datos.cursor()

def crearTabla():
    cr.execute('''
        CREATE TABLE IF NOT EXISTS tabla(
        ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Nombre TEXT NOT NULL,
        Precio TEXT NOT NULL,
        Stock TEXT NOT NULL);
        ''')
    base_de_datos.commit()
    print("Creado")




def rellenar_tabla(tabla):
    cr.execute('''SELECT * FROM tabla;''')
    datos = cr.fetchall()
    for dato in datos:
        tabla.insert("", "end", values=dato)

def limpiar_tabla(tabla):
    for item in tabla.get_children():
            tabla.delete(item)

def ingresarDatos():
    ventana = Toplevel(marco2)
    ventana.title("Ventana Secundaria")
    ventana.geometry()

    boton_cerrar = Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack()

    etiqueta = Label(ventana, text = "Ingrese el Nombre")
    etiqueta.pack()
    caja = Entry(ventana)
    caja.pack()


    etiqueta2 = Label(ventana, text="Ingrese el precio")
    etiqueta2.pack()
    caja2 = Entry(ventana)
    caja2.pack()



    etiqueta3 = Label(ventana, text="Ingrese el Stock")
    etiqueta3.pack()
    caja3 = Entry(ventana)

    caja3.pack()


    def guardar():
        Nombre = caja.get()
        Precio = caja2.get()
        Stock = caja3.get()
        cr.execute('''
            INSERT INTO tabla(Nombre,Precio , Stock)
            VALUES(?,?,?)''',(Nombre, Precio, Stock))
        base_de_datos.commit()
        print("Datos ingresados existosamente")

        limpiar_tabla(tabla)
        rellenar_tabla(tabla)

    btn = Button(ventana, text = "guardar", command= guardar)
    btn.pack()

app = Tk()
app.title("Aplicacion y tablas")

marco = Frame(app)
marco.grid(row=1,column=0)
tabla = ttk.Treeview(marco, columns=("ID", "Nombre", "Edad","Stock"), show="headings")
marco2 = Frame(app)
marco2.grid(row = 2, column = 0)


tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Edad", text="Edad")
tabla.heading("Stock", text ="Stock")


for col in tabla["columns"]:
    tabla.column(col, anchor="center", width=100)

tabla.pack()

btn = Button(marco2, text = "Agregar", command = ingresarDatos)
btn.grid(row = 1 , column = 3)

rellenar_tabla(tabla)

app.mainloop()