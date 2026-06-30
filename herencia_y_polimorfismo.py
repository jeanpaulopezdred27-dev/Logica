"""
/*
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 """
class Animal:

    def __init__(self,name):
        self.name=name

    def sound(self):
        pass

class Perro(Animal):
    def sound(self):
        print(f"El perro hace woof")


class Gato(Animal):
    def sound(self):
        print("El gato hace miau")


animal=Animal("Animal")
animal.sound()
perro=Perro("Perro")
perro.sound()
gato=Gato("Gato")
gato.sound()

#Esto en sintesis es herencia 

#Ester es un ehemplo de polimorfismo
print("Polimorfismo")
def print_sound(animal:Animal):
    animal.sound()

perro=Perro("Perro")
print_sound(perro)

print_sound(gato)


"""
DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.

"""

print("Ejercicio pesado")
class Empleado:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.lista=[]
      

    def identificar(self):
        return f"El Empleado se llama {self.name} y su id es: {self.id}"
    
    def funciones(self):
        pass

    def agregar(self,name):
        self.lista.append(name)

    def a_cargo(self):
        pass
    

class Programador(Empleado):
    
    def funciones(self):
        print(f"El empleado {self.name} es un programador backend")

    def a_cargo(self):
        print(f"El empleado {self.name} no tiene a nadie a su cargo, ya que es un programador.")
    
class Gerente_de_proyecto(Empleado):

    def funciones(self):
        print(f"El empleado {self.name} es un gerente de proyecto")

    def a_cargo(self):
        
        print(f"El Gerente de proyecto {self.name} esta a cargo de : ")
        for i in self.lista:
            print(f"--{i.name}")

class Gerente_general(Empleado):
    def funciones(self):
        print(f"El empleado {self.name} es un gerente General")

    def a_cargo(self):
        
        print(f"El Gerente General {self.name} esta a cargo de : ")
        for i in self.lista:
            print(f"--{i.name}")

     
        

programador=Programador("Miguel",1234)
gerente_proyecto=Gerente_de_proyecto("AlexaGP",987)
gerente_general=Gerente_general("Jean",8778)
programador2=Programador("Carlota",1234)
gerente_proyecto.agregar(programador)
gerente_proyecto.agregar(programador2)
gerente_general.agregar(gerente_proyecto)

programador.a_cargo()
gerente_general.a_cargo()
gerente_proyecto.a_cargo()





