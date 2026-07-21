"""
* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 */
 """

#Recordar que hay un comando para permitirte escribir y luego tienes que poner el comando para poder leerlo
import os
#Para escribir
file_name="jeanPaul.txt"
with open(file_name,"w") as file:
    file.write("hola\n")
    file.write("jean paul\n")
    file.write("como estas")

with open(file_name,"r")  as file:
    print(file.read())

#os.remove(file_name) #Esto es para eliminar el fichero

#problema de control de gestion de inventario
import os

problema="gestion_de_inventario.txt"
while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar pedido")
    print("4. borrar  producto")
    print("5. mostrar productos")
    print("6. Calcular venta por producto")
    print("7. Calcular venta totales")
    print("8. Salir")

    try:
        que_hacer=int(input("Ingresa una de las variables:  "))
    except:
        print("Por favor ingresa una variable valida.")
        continue

    if que_hacer==1:
        name=input("Producto:  ")
        cantidad=input("Stock:  ")
        precio=input("Precio:   ")
        with open(problema,"a") as paper:
            paper.write(f"{name}, {cantidad}, {precio}\n")
    
    elif que_hacer==2:
        name=input("Producto:  ")
        encontrado=False
        with open(problema,"r") as paper:
            for producto in paper.readlines():
                if name == producto.split(", ")[0]:
                    print(producto)
                    encontrado=True
                    break
            if not encontrado:
              print("Producto no encontrado.\n ingrese la varable 1 para poder añadir el producto...(1)")
    
    elif que_hacer==3:
        name=input("Producto:  ")
        cantidad=input("Stock:  ")
        precio=input("Precio:   ")
        with open(problema,"r") as paper:
            hacer_3=paper.readlines()

        with open(problema,"w") as paper:
            for i in hacer_3:
                if i.split(", ")[0]==name:
                    paper.write(f"{name}, {cantidad}, {precio}\n")
                else:
                    paper.write(i)

    elif que_hacer==4:  #borrar producto
        name=input("Producto:  ")
        with open(problema,"r") as paper:
            hacer_4=paper.readlines()
        with open(problema,"w") as paper:
            for producto in hacer_4:
                if producto.split(", ")[0]!=name:
                    paper.write(producto) 
            

    elif que_hacer==5: #mostrar producto
        with open(problema,"r") as paper:
            hacer_5=paper.readlines()
            for i in hacer_5:
                print(i)

    elif que_hacer==6:
        total=0
        name=input("Producto:  ")
        with open(problema,"r") as paper:
            hacer_6=paper.readlines()
        for producto in hacer_6:
            condicion=producto.split(", ")
            if condicion[0]==name:
                cantidad_producto=int(condicion[1])
                precio_producto=float(condicion[2])
                total= cantidad_producto*precio_producto
                break
        print(f"El total de ventas de {name}  es: {total}")

    elif que_hacer==7:
        total=0
        with open(problema,"r") as paper:
            hacer_6=paper.readlines()
        for i in hacer_6:
            condicion=i.split(", ")
            cantidad_producto=int(condicion[1])
            precio_producto=float(condicion[2])
            total+= cantidad_producto*precio_producto
        print(f"El total de ventas es: {total}")


    elif que_hacer==8:
        os.remove(problema)
        break



        
        


    
