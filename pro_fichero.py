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
        que_hacer=int(input("Ingresa una variable por favor: "))
    except:
        print("Por favor ingresa una variable valida...")
        continue

    if que_hacer==1: #Añadir producto
        print("Por favor ingrese el nombre, cantidad de stock y precio...")
        name=input("Nombre:  ")
        stock=int(input("Stock:  "))
        precio=float(input("Precio:  "))
        with open(problema,"a") as paper:
            paper.write(f"{name}, {precio}, {precio}")
            print(f"El producto:  {name} fue ingresado correctamente")
    
    elif que_hacer==2: #Consultar producto
        name=input("Nombre:  ")
        with open(problema,"r") as paper:
            hacer_2=paper.readlines()

        for i in hacer_2:
            if i.split(", ")[0]==name:
                print(i)



