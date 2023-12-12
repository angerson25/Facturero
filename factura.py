##Crear un archivo con el formato de una factura de venta, la cual debe tener un encabezado de los datos básicos de la empresa y posterior los datos de la fecha, nombre de cliente, adicional los datos de un grupo indeterminado de registros de ventas de productos (código, nombre, cantidad, precio unitario y precio total). cuyos datos del cliente, preciosy nombres son obtenidos a partir de diccionarios, al final de los ítems tiene que agregarse el total de la venta, Todos los diccionarios son obtenidos de archivos .txt. Cada producto debe tener identificado su pocentaje de IVA. Al finalizar la factra se dbee totalizar este mismo.

import os
import random

# Actualizar el diccionario
Productos = {}

# Importar el archivo de texto que contiene los datos
with open("Productos.txt", "r") as f:
    x = f.readlines()
    for i in x:
        lista1 = i.split(":")
        lista1[1] = lista1[1].replace("\n", "")
        lista2 = lista1[1].split(",")
        Productos.setdefault(lista1[0], lista2)
        
##Añadir clientes
Clientes = {}

# Importar el archivo de texto que contiene los datos
with open("Clientes.txt", "r") as f:
    x = f.readlines()
    for i in x:
        lista1 = i.split(":")
        lista1[1] = lista1[1].replace("\n", "")
        lista2 = lista1[1].split(",")
        Clientes.setdefault(lista1[0], lista2)
        
##Venta
ventaunitaria = {}
print("Bienvenido a la tienda de la esquina\n")

##productos disponibles
print("{:<5} {:<15} {:<10}".format("Código", "Producto", "Precio"))
print("-" * 30)

for codigo, (producto, precio) in Productos.items():
    print("{:<5} {:<15} ${:<10}".format(codigo, producto, precio))
    
##realizar la compra   
print("\n¿Desea realizar una compra? (1: Si, 0: No)")
opcion = input("Ingrese la opcion: ")

clienteacomprar = ""

while opcion == "1":
    if clienteacomprar == "":
        clienteacomprar = input("Ingrese el codigo del cliente: ")
        if clienteacomprar not in Clientes.keys():
            print("\nEl cliente no está registrado")
            print("¿Desea registrarlo? (1: Si, 0: No)")
            opcionagre = input("Ingrese la opcion: ")
            if opcionagre == "1":
                nombre = input("Ingrese el nombre del cliente: ")
                codigo = input("Ingrese el codigo del cliente: ")
                Clientes[codigo] = [nombre]
            else:
                break
        else:
            print("\nEl cliente está registrado")

    codigoacomprar = input("\nDigite el codigo del producto a comprar: ")
    for key in Productos:
        if codigoacomprar == key:
            cantidad = int(input("Digite la cantidad del producto a comprar: "))
            print("El precio de ", Productos[key][0], "es: ", Productos[key][1])
            ventaunitaria[Productos[key][0]] = (Productos[key][1], cantidad)

    print(ventaunitaria)

    opcion = input("\n¿Desea realizar otra compra? (1: Si, 0: No): ")
    

if len(ventaunitaria) == 0:
    print("No realizó ninguna compra")
else:
    ##Datos de la factura
    numero_factura = random.randint(1000000, 9999999)
    total=0
    compras=""
    compras += "{:<15} {:<10} {:<15} {:<10}\n".format("Producto", "Cantidad", "Precio Unit.", "Subtotal")
    compras += "-" * 50 + "\n"

    for producto, (precio_unitario, cantidad) in ventaunitaria.items():
        precio_unitario = int(precio_unitario)
        subtotal = precio_unitario * cantidad
        total += subtotal

        compras += "{:<15} {:<10} {:<15} {:<10}\n".format(producto, cantidad, f"${precio_unitario}", f"${subtotal}")

    compras += "-" * 50 + "\n"
    compras += "{:<40} {:<10}".format("Subtotal:", f"${total}")
    
    compras += "\n{:<40} {:<10}".format("Total con IVA:", f"${total*1.19}")
    


    ##Escribir la factura
    with open("ticket.txt", "w") as f:
        f.write("\nGracias por su compra")
        f.write("\nNombre cliente: "+str(Clientes[clienteacomprar]))
        f.write("\nCodigo cliente: "+clienteacomprar)
        f.write("\nNumero de factura: "+str(numero_factura))
        f.write("\n\nCompra: \n")
        f.write(compras)

    
##Actualizar el archivo con la informacion del cliente
with open("Clientes.txt", "w") as f:
    for i in Clientes:
        f.write(f"{i}:{','.join(Clientes[i])}\n")
