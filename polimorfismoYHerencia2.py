"""
DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""
"""
🔹 Problema 1: Sistema de Hospital

Implementa la jerarquía de un hospital.

Clase base: Personal
nombre, id
Subclases:
Doctor → especialidad, lista de pacientes
Enfermero → turno (día/noche)
Administrador → área

🔧 Requisitos:

Cada clase debe tener un método trabajar() que se comporte diferente (polimorfismo).
Los doctores pueden agregar pacientes.
Todos pueden mostrar su información.
Implementa una función que recorra una lista de personal y ejecute trabajar().
"""

class Personal:
    def __init__(self,name, id):
        self.name=name
        self.id=id
        self.lista=[]

    def trabajar(self):
        pass

    def datos(self):
        print(f"Nombre: {self.name}\nID: {self.id}")

    def agregar(self):
        pass

class Doctor(Personal):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.especialidad_completado=False

    def especialidad(self,especialidad):
        self.name_especialidad=especialidad
        self.especialidad_completado=True
        return self.name_especialidad


    def trabajar(self):
        if not self.especialidad_completado :
            print(f"Por favor primero ingresar la especialidad del doctor: {self.name}")

        else:
            print(f"El Dr {self.name} trabaja en la especialidad de {self.name_especialidad}")

    def agregar(self,names):
        self.lista.append(names)
        print(f"El paciente: {names} fue agregado correctamente a la lista de pacientes del doctor: {self.name}")

    def lista_pendientes(self):
        index=1
        for i in self.lista:
            print (f"{index}. {i}")
            index+=1


class Enfermero(Personal):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.turno_completado=False

    def turno(self,dia_o_noche):
        self.mi_turno=dia_o_noche
        self.turno_completado=True

    def trabajar(self):
        if not self.turno_completado:
            print(f"Por favor ingresa primero tu turno con la funcion turno.")
        else:
            print(f"El enfermero {self.name} tiene turno de {self.mi_turno}")

    def agregar(self):
        print(f"Solo los doctores pueden ingresar nuevos pacientes a las listas.")

    
class Administrador(Personal):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.especialidad_completado=False

    def especialidad(self,especialidad):
        self.name_especialidad=especialidad
        self.especialidad_completado=True
        return self.name_especialidad
    
    def trabajar(self):
        if not self.especialidad_completado :
            print(f"Por favor primero ingresar la especialidad del administrador: {self.name}")

        else:
            print(f"El administrador {self.name} trabaja en la especialidad de {self.name_especialidad}")

    def agregar(self):
        print(f"Solo los doctores pueden ingresar nuevos pacientes a las listas.")
    

print("Enfermero")
enfermero1=Enfermero("Miguel",12345)
enfermero2=Enfermero("Alexa",23456)

enfermero1.datos()
enfermero1.agregar()
enfermero1.trabajar()
enfermero1.turno("dia")
enfermero1.trabajar()

print("DOCTOR")
doctor1=Doctor("Jean",99999)
doctor1.datos()
doctor1.agregar("paciente1")
doctor1.trabajar()
doctor1.agregar("paciente2")
doctor1.especialidad("Cardiologo")
doctor1.trabajar()
doctor1.lista_pendientes()

print("Administrador")
administrador1=Administrador("Administrador1",76590)
administrador1.datos()
administrador1.agregar()
administrador1.trabajar()
administrador1.especialidad("Cardiologia")
administrador1.trabajar()







        

                
        

    

    