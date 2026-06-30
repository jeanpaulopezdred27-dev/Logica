
"""
/*
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.

 */
 """

class Programer():
    surname=None

    def __init__(self,name,age,lenguage):
        self.name=name
        self.age=age
        self.lenguage=lenguage

    def impresion(self):
        print(f"Nombre: {self.name}\nEdad: {self.age}\nLenguaje: {self.lenguage}\nApellido: {self.surname}")

"""
programador=Programer("Jean",24,"Java y Python")
programador.impresion()
programador.surname="Lopez"
programador.impresion()
"""

#Dificultad extra

#Implementa dos clases que representen las estructuras de Pila y Cola
#inicializarse y disponer de operaciones para añadir, eliminar,
#retornar el número de elementos e imprimir todo su contenido.

class Cola():
    def __init__(self):
        self.lista=[]

    def añadir(self,elemento):
        self.lista.append(elemento)

    def eliminar(self):
        if len(self.lista)==0:
            print("No hay elementos")
        else:
            salida=self.lista[0]
            self.lista.pop(0)
            return salida
    
    def retornar(self):
        return f"Tienes {len(self.lista)} elementos en tu lista "
    
    def imprimir(self):
        if len(self.lista)==0:
            print("No tienes nada en tu lista de pendientes.")
        else:
            print(f"Los elementos de la lista son :{self.lista}")
    

pila=Cola()

pila.añadir("Elemento 1")
pila.añadir("Elemento 2")
pila.añadir("Elemento 3")
pila.añadir("Elemento 4")
pila.imprimir()

pila.eliminar()
pila.retornar()
pila.imprimir()


class Pilas():
    
    def __init__(self):
        self.lista=[]

    def añadir(self,elemento):
        self.lista.append(elemento)

    def eliminar(self):
        if len(self.lista)==0:
            print("No hay elementos")
        else:
            salida=self.lista[len(self.lista)-1]
            self.lista.pop()
            return salida
    
    def retornar(self):
        return len(self.lista)
    
    def imprimir(self):
        if len(self.lista)==0:
            print("No tienes nada en tu lista de pendientes.")
        else:
            print(f"Los elementos de la lista son :{self.lista}")