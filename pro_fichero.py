import os
problema="gestion_de_inventario.txt"
while True:
    print("1. Añadir producto")
    print("2. Consultar producto")
    print("3. Actualizar pedido")
    print("4. borrar  producto")
    print("5. mostrar productos")
    print("6. Calcular venta totales")
    print("7. Calcular venta por producto")
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
            paper.write(f"{name}, {stock}, {precio}\n")
            print(f"El producto:  {name} fue ingresado correctamente")
    
    elif que_hacer==2: #Consultar producto
        name=input("Nombre:  ")
        encontrado=False
        with open(problema,"r") as paper:
            hacer_2=paper.readlines()

        for i in hacer_2:
            if i.split(", ")[0]==name:
                print(i)
                encontrado=True
        if not encontrado:
            print(f"El producto {name} no fue encontrado, por favor añadalo con la opcion (1)")
    
    elif que_hacer==3: #Actualizar producto
        name=input("Nombre:  ")
        stock=int(input("Stock:  "))
        precio=float(input("Precio:  "))
        with open(problema,"r") as paper:
            hacer_3= paper.readlines()
        
        with open(problema,"w") as paper:
            for i in hacer_3:
                if i.split(", ")[0]==name:
                    paper.write(f"{name}, {stock}, {precio}\n")
                else:
                    paper.write(i)
    
    elif que_hacer==4: #borrar producto
        name=input("Nombre:  ")
        with open(problema,"r") as paper:
            hacer_4= paper.readlines()
        
        with open(problema,"w") as paper:
            for i in hacer_4:
                if i.split(", ")[0] !=name:
                    paper.write(i)
    
    elif que_hacer==5: #mostrar productos
        
        with open(problema,"r") as paper:
            hacer_5= paper.readlines()
        
        for i in hacer_5:
            print(i)
    
    elif que_hacer==6: #Calcular venta total
        with open(problema,"r") as paper:
            hacer_6=paper.readlines()
        
        total=0

        for i in hacer_6:
            cantidad= int(i.split(", ")[1])
            costo= float(i.split(", ")[2])
            total+=cantidad*costo
        
        print(f"El total de ventas totales es: {total}")
    
    elif que_hacer==7: #Calcular venta por producto
        name=input("Nombre:  ")

        with open(problema,"r") as paper:
            hacer_7=paper.readlines()
        
        encontrado=False

        for i in hacer_7:
            if i.split(", ")[0]==name:
                cantidad= int(i.split(", ")[1])
                costo=float(i.split(", ")[2])
                total=cantidad*costo
                encontrado=True
                print (f"El producto {name} tiene una gancia de: {total}")

        if not encontrado:
            print(f"Producto no encontrado")
            
    elif que_hacer==8:
        os.remove(problema)
        break

    else:
        print("Por favor ingresa una variable valida del(1-8)")




        



        





        