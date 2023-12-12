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
print("Bienvenido a la tienda de la esquina")
