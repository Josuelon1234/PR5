from tkinter import *

# Crear la ventana
ventana = Tk()
ventana.title("Registro de productos")

# Crear los campos de entrada
producto_label = Label(ventana, text="Producto:")
producto_label.grid(row=0, column=0, padx=5, pady=5)
producto_entry = Entry(ventana)
producto_entry.grid(row=0, column=1, padx=5, pady=5)

sku_label = Label(ventana, text="SKU:")
sku_label.grid(row=1, column=0, padx=5, pady=5)
sku_entry = Entry(ventana)
sku_entry.grid(row=1, column=1, padx=5, pady=5)

depto_label = Label(ventana, text="Depto:")
depto_label.grid(row=2, column=0, padx=5, pady=5)
depto_entry = Entry(ventana)
depto_entry.grid(row=2, column=1, padx=5, pady=5)

opcion_label = Label(ventana, text="Opción:")
opcion_label.grid(row=3, column=0, padx=5, pady=5)
opcion_entry = Entry(ventana)
opcion_entry.grid(row=3, column=1, padx=5, pady=5)

provedor_label = Label(ventana, text="Proveedor:")
provedor_label.grid(row=4, column=0, padx=5, pady=5)
provedor_entry = Entry(ventana)
provedor_entry.grid(row=4, column=1, padx=5, pady=5)

idioma_label = Label(ventana, text="Idioma:")
idioma_label.grid(row=5, column=0, padx=5, pady=5)
idioma_entry = Entry(ventana)
idioma_entry.grid(row=5, column=1, padx=5, pady=5)

opcion_boton = Radiobutton(ventana, text="Opción A", value="A")
opcion_boton.grid(row=6, column=1, padx=5, pady=5)
opcion_boton = Radiobutton(ventana, text="Opción B", value="B")
opcion_boton.grid(row=7, column=1, padx=5, pady=5)
opcion_boton = Radiobutton(ventana, text="Opción C", value="C")
opcion_boton.grid(row=8, column=1, padx=5, pady=5)

idioma_boton = Radiobutton(ventana, text="BN", value="BN")
idioma_boton.grid(row=9, column=0, padx=5, pady=5)
idioma_boton = Radiobutton(ventana, text="SP", value="SP")
idioma_boton.grid(row=9, column=1, padx=5, pady=5)

# Crear botón de registro
def registrar():
    producto = producto_entry.get()
    sku = sku_entry.get()
    depto = depto_entry.get()
    opcion = opcion_entry.get()
    provedor = provedor_entry.get()
    idioma = idioma_entry.get()
    print(f"Producto: {producto}\nSKU: {sku}\nDepto: {depto}\nOpción: {opcion}\nProveedor: {provedor}\nIdioma: {idioma}")

registrar_boton = Button(ventana, text="Registrar", command=registrar)
registrar_boton.grid(row=10, column=1,
