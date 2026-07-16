print("Problema 1\nPilas de Libros")
    
def problema1():
    pila_de_libros=[]
    while True:
        
        try:
            print("Que deceas hacer,por favor ingresa un numero")
            que_hacer=int(input("1.Agregar libro\n2.Retirar último libro\n3.Ver pila\n4.Salir\n"))
        except:
            print(f"Ingresa una variable valida")
            continue
        
        if que_hacer==1:
            libro=input("Ingresa el titulo del libro que quieres agregar: ")
            pila_de_libros.append(libro)
            print(f"Ingresaste el libro {libro} correctamente")
        
        elif que_hacer==2:
            if len(pila_de_libros)>=1:
                ultimo_libro=pila_de_libros.pop()
                print(f"El libro que retiraste es {ultimo_libro}")
                print(pila_de_libros)
            else:
                print("No tienes nada en tu pila de libros,")
        
        elif que_hacer==3:
            if len(pila_de_libros)==0:
                print(f"No tienes nada en tu pila de libros")
            else:
                conteo=1
                for i in pila_de_libros:
                    print(f"{conteo}.  {i}")
                    conteo+=1
        
        elif que_hacer==4:
            print(f"Gracias por usar el sistema de fila de cola\nHasta luego...")
            break
        
       

problema1()

print("Problema 2\nHistorial de Navegacion")

def problema2():
    historial=[]
    while True:
        try:
            print("Que deceas hacer,por favor ingresa un numero")
            que_hacer=int(input("1. Visitar página\n2. Atrás\n3. Ver página actual\n4. Ver historial\n5. Salir\n"))
        except:
            print("Ingresa una variable valida por favor.")
            continue
        
        if que_hacer==1:
            pagina=input("Ingresa la pagina a la que quieres ingresar: ")
            historial.append(pagina)
            print(f"Estas en {historial[-1]}")

        elif que_hacer==2:
            if len(historial)>=1:
                historial.pop()
                if len(historial)>=1:
                    print(f"Estas en: {historial[-1]}")
                else:
                    print("Estas en la pagina de inicio")
            else:
                print("Estas en la pagina de inicio")
        
        elif que_hacer==3:
            if len(historial)>=1:
                print(f"Estas en: {historial[-1]}")
            else:
                print("Estas en la pagina de inicio")
                
        
        elif que_hacer==4:
            conteo=1
            if len(historial)>=1:
                print("Historia: ")
                for i in historial:
                    print(f"{conteo}.  {i}")
                    conteo+=1
            else:
                print("No haz visitado paginas aun")
        elif que_hacer==5:
            print("Gracias por usar nuestra web\nAdios ...")
            break
            
problema2()




