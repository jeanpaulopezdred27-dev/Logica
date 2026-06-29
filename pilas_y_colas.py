#Son estructuras basicas en todos los lenguajes de programacion
#La pila es el ultimo en entrar es el primero en salir 
#Las colas son las primeros en ingresar son los primeros en salir 


"""
* EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 """
#Aplicativo de retroseso, avance y redireccion y salir para break

def aplicativo():
    secuencia_app=[]
    while True:
        accion=input("Que vamos a hacer: retroceder(r), avanzar(a), redirigir(url), salir(s)")
        
        if accion=="s":
            print("Procedemos a salir del programa.")
            break
        
        elif accion=="url":
            url=input("Ingresa tu url: ")
            secuencia_app.append(url)
        
        elif accion=="r":
            if len(secuencia_app)>0:
                secuencia_app.pop()

        elif accion=="a":
            pass
        
        else:
            print("Por favor ingresa una  variable valida")

        if len(secuencia_app)>=1:
            print(secuencia_app[len(secuencia_app)-1])
            
        else:
            print("Estas en la pagina de inicio")
       

def impresora():
    cola_de_impresion=[]
    while True:
        ingreso=input("Ingresar la accion a realizar: enviar documento(e) o imprimir(i) o salir(s)")
        
        if ingreso=="e":
            agregar=input("Ingresa el nombre del documento que enviaras: ")
            cola_de_impresion.append(agregar)
            print(f"Se agrego {agregar} a la cola de impresion")
        
        elif ingreso=="i":
            if len(cola_de_impresion)>0:
                print(f"Se esta imprimiendo {cola_de_impresion[0]} ")
                cola_de_impresion.pop(0)
                if len(cola_de_impresion)>0:
                    print(f"La cola de impresion es: {cola_de_impresion}")
                
                else: 
                    print("La cola de impresion esta vacia.")
                

            else:
                print("Ya no queda nada por imprimir")
        
        elif ingreso=="s":
            print("Se procede a salir de la web de la impresora...")
            break
        else:
            print("Ingrsa un valor valido por favor.")



"""
 Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
 """


def impre():
    cola_impresion=[]
    while True:
        que_hacer=input("Que quieres hacer\nImprimir(i) o enviar archivo(e)")

        
        if que_hacer=="i":
            if len(cola_impresion)==0:
                print("nO hay nada pendiente a imprimir")
            else: 
                print(f"Se esta imprimiendo {cola_impresion[0]}")
                cola_impresion.pop(0)
                print(cola_impresion)

        elif que_hacer=="e":
            agregar=input("Ingresa el nombre del documento que esta enviando: ")
            print(f"El documento ({agregar} se agrego a la cola. )")
            cola_impresion.append(agregar)
            print(f"La cola actual de impresion es: {cola_impresion}")

        elif que_hacer=="s":
            print("Procedemos a salir del app de la impresora... ")
            break
        else:
            print(f"La variable {que_hacer} no es valida, por favor ingresa una valida.")




impre()




        
        


