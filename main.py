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
    ventana.title("Agregar")
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
        if Nombre == "" or Precio == "" or Stock == "":
            messagebox.showwarning("ALERTA", "No hay nada escirto por favor ingresa de todos los datos")
        else:
            cr.execute('''
                INSERT INTO tabla(Nombre,Precio , Stock)
                VALUES(?,?,?)''',(Nombre, Precio, Stock))
            base_de_datos.commit()
            print("Datos ingresados existosamente")
            caja.delete(0,END)
            caja2.delete(0, END)
            caja3.delete(0, END)
            limpiar_tabla(tabla)
            rellenar_tabla(tabla)

    btn = Button(ventana, text = "guardar", command= guardar)
    btn.pack()

def modificar():
    ventana = Toplevel(marco2)
    ventana.title("Modificar")
    ventana.geometry()

    boton_cerrar = Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack()

    etiqueta1 = Label(ventana, text="Ingrese el ID de los datos que quiere modificar")
    etiqueta1.pack()
    caja1 = Entry(ventana)
    caja1.pack()

    etiqueta = Label(ventana, text="Ingrese el Nombre")
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

    def modificaru():
        ID = caja1.get()
        Nombre = caja.get()
        Precio = caja2.get()
        Stock = caja3.get()

        if ID == "" or Nombre == "" or Precio == "" or Stock == "":
            messagebox.showwarning("ALERTA", "No hay nada escirto por favor ingresa de todos los datos")
        else:
            cr.execute('''
               UPDATE tabla
               SET Nombre = ?, Precio = ?, Stock = ?
               WHERE ID = ? ''', (Nombre, Precio, Stock,ID))
            base_de_datos.commit()

            caja.delete(0, END)
            caja2.delete(0, END)
            caja3.delete(0, END)

            limpiar_tabla(tabla)
            rellenar_tabla(tabla)

    btn = Button(ventana, text="modificar", command=modificaru)
    btn.pack()

def eliminar():
    ventana = Toplevel(marco2)
    ventana.title("Modificar")
    ventana.geometry()

    boton_cerrar = Button(ventana, text="Cerrar", command=ventana.destroy)
    boton_cerrar.pack()

    etiqueta1 = Label(ventana, text="Ingrese el ID de los datos que quiere modificar")
    etiqueta1.pack()
    caja1 = Entry(ventana)
    caja1.pack()



    base_de_datos.commit()
    def eliminador():
        ID = caja1.get()
        if ID == "" :
            messagebox.showwarning("ALERTA", "No hay nada escirto por favor ingresa de todos los datos")
        else:
            cr.execute('''
                     DELETE tabla WHERE ID  = ?''', (id,))
            base_de_datos.commit()

            caja.delete(0, END)
            caja2.delete(0, END)
            caja3.delete(0, END)

            limpiar_tabla(tabla)
            rellenar_tabla(tabla)

    btn = Button(ventana, text="eliminar", command=eliminador)
    btn.pack()


app = Tk()
app.title("Aplicacion y tablas")

marco = Frame(app)
marco.grid(row=1,column=0)
tabla = ttk.Treeview(marco, columns=("ID", "Nombre", "Precio","Stock"), show="headings")
marco2 = Frame(app)
marco2.grid(row = 2, column = 0)


tabla.heading("ID", text="ID")
tabla.heading("Nombre", text="Nombre")
tabla.heading("Precio", text="Precio")
tabla.heading("Stock", text ="Stock")


for col in tabla["columns"]:
    tabla.column(col, anchor="center", width=100)

tabla.pack()

btn = Button(marco2, text = "Agregar", command = ingresarDatos,width=30)
btn.grid(row = 1 , column = 0)

btn = Button(marco2, text = "Modificar", command = modificar,width=30)
btn.grid(row = 1 , column = 1)

btn = Button(marco2, text = "eliminar", command = eliminar,width=30)
btn.grid(row = 2, column = 0)

btn = Button(marco2, text  = "cerrar", command = app.destroy,width=30)
btn.grid(row = 2, column = 1)
rellenar_tabla(tabla)

app.mainloop()
