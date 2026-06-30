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