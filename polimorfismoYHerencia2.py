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
        print(f"El paciente: {names} fue agrrgado correctamente a la lista de pacientes del doctor: {self.name}")

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
        print(f"Solo los doctores pueden agendar o agregar pacientes a la lista de espera.")
    

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

"""
Crea un sistema de personajes en un juego.

Clase base: Personaje
nombre, nivel
Subclases:
Guerrero → fuerza
Mago → mana
Arquero → precisión

🔧 Requisitos:

Método atacar() distinto para cada clase.
Método subir_nivel() que funcione diferente según el personaje.
Crear una lista de personajes y ejecutar ataques (polimorfismo).
"""

class Personaje:
    def __init__(self,name,nivel,vida):
        self.name=name
        self.nivel=nivel
        self.vida=vida

    def atacar(self):
        pass

    def subir_nivel(self):
        pass

    def recibir_daño(self, daño):
        self.vida-=daño
        
        if self.vida<0:
            self.vida=0
    
    def subir_nivel(self):
        self.nivel+=1

    
class Guerrero(Personaje):

    def __init__(self, name, nivel, vida,fuerza):
        super().__init__(name, nivel, vida)
        self.fuerza=fuerza

   

    def atacar(self):
        daño=self.fuerza
        return daño
    
    def subir_nivel(self):
        self.fuerza+=10
        super().subir_nivel()
    
    
        

class Mago(Personaje):
    def __init__(self, name, nivel, vida,magia):
        super().__init__(name, nivel, vida)
        self.magia=magia

   

    def atacar(self):
        daño=self.magia
        return daño
    
    def subir_nivel(self):
        self.magia+=12
        super().subir_nivel()
    

class Arquero(Personaje):
    def __init__(self, name, nivel, vida,presicion):
        super().__init__(name, nivel, vida)
        self.presicion=presicion

   

    def atacar(self):
        daño=self.presicion
        return daño
    
    def subir_nivel(self):
        self.presicion+=13
        super().subir_nivel()
    

#Problema dos tienda virtual

class Producto:

    def __init__(self,nombre,precio,stock):
        self.nombre=nombre
        self.precio=precio
        self.stock=stock

    def precio_final(self):
        pass


class Electrodomestico(Producto):
    
    def precio_final(self):
        #Agregaremos una garantia por el 10% del valor del producto
        garantia=self.precio/10
        new_precio=self.precio+garantia
        print(f"El nuevo precio incluyendo la garantia es {new_precio}")


class Ropa(Producto):

    def precio_final(self):
        #Haremos un descuento del 15%
        descuento= self.precio/100 *15
        new_precio=self.precio - descuento
        print(f"El nuevo precio con el descuento de ropa es de {new_precio}")

class Alimento(Producto):

    def precio_final(self):
        #Agregaremos el valor del impuesto que en mi pais es del 18%
        impuesto=self.precio/100 *18
        new_precio=self.precio + impuesto
        print(f"El precio con los impuestos agregados es de {new_precio}")
        
    
# Problema 8 con sistema escolar
"""
class Persona:
    
    def __init__(self, nombre,id):
        self.nombre=nombre
        self.id=id

    def identificarse(self):
        print(f"Nombre: {self.nombre}\nId: {self.id}")



class Profesor(Persona):
    def __init__(self, nombre, id,curso):
        super().__init__(nombre, id)
        self.curso=curso

    def identificarse(self):
        super().identificarse()
        print(f"Curso: {self.curso}")

    def agregar_nota(self,alumno_name,nota):
        alumno_name.lista_nota.append(nota)
        print(f"La nota {nota} se guardo correctamente")


class Alumno(Persona):
    
    def __init__(self, nombre, id,curso,):
        super().__init__(nombre, id)
        self.curso=curso
        self.lista_nota=[]

    def identificarse(self):
        super().identificarse()
        print(f"Curso: {self.curso}")

    def ver_notas(self):
        if len(self.lista_nota)==0:
            print("El profesor aun no ingresa ninguna nota.")
        else:
            index=1
            for i in self.lista_nota:
                print(f"{index}. {i}")
                index+=1

    def promedio(self):
        
        cantidad=len(self.lista_nota)
        
        total=sum(self.lista_nota)
        
        print(f"El promedio de las notas es: {total/cantidad}")

    
        

    

class Alumno(Persona):
    def agregar_nota(self):
        print(f"Solo los profesores pueden agregar notas")


"""
# Problema 8 con sistema escolar

class Persona:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def identificarse(self):
        print(f"Nombre: {self.name}\nID: {self.id}")
    
    def accion(self):
        pass
    

class Maestro(Persona):
    def __init__(self, name, id,materia):
        super().__init__(name, id)
        self.materia=materia
    
    def identificarse(self):
        super().identificarse()
        print(f"Curso: {self.materia}")

    def accion(self):
        while True:
            clases=input("Ingresa si el profesor esta en clase(Si o NO)")
            if clases.lower() =="si":
                print(f"El profesor actualmente esta dando clases.")
                break
            elif clases.lower()=="no":
                print(f"El profesor actualemte esta descansano en el area de descanso")
                break
            else: 
                print(f"La variable {clases}, no es valida, por favor ingrese la variable si o no")
    
    def registrar_nota(self,nombre_alumno,nota=int):
        nombre_alumno.lista_nota.append(nota)
        print(f"La nota {nota} se subio a sistema correctamente.")
    
    def evaluar_alumno(self,nombre_alumno):
        total=sum(nombre_alumno.lista_nota)
        cantidad=len(nombre_alumno.lista_nota)

        promedio=total/cantidad
        if promedio >=18:
            print(f"Tu promedio es: {promedio:.2f} tu estado es: EXCELENTE.")
        elif promedio>=15:
            print(f"Tu promedio es: {promedio:.2f} tu estado es: BUEN DESEMPEÑO.")
        else:
            print(f"Tu promedio es: {promedio:.2f} tu estado es: NECESITAS MEJORAR.")
            

    

class Alumno(Persona):
        
    def __init__(self, name, id,curso):
        super().__init__(name, id)
        self.curso=curso
        self.lista_nota=[]

    def identificarse(self):
        super().identificarse()
        print(f"Curso: {self.curso}")

    def accion(self):
        print(f"El alumno {self.name} esta actualmente en clases.")
    
    def ver_notas(self):
        print(f"Las notas del alumno {self.name}  en el curso {self.curso} son : {self.lista_nota}")
    
    def calcular_promedio(self):
        total=0
        for nota in self.lista_nota:
            total+=nota
        promedio=total/len(self.lista_nota)
        print(f"El promedio dell alumno {self.name} es: {promedio:.2f}:")

print("Problema de alumno y profesor")
maestro1=Maestro("Jean",2222,"Matematicas")
miguel=Alumno("Miguel lopez",1111,"Matematicas")

maestro1.identificarse()
maestro1.accion()
maestro1.registrar_nota(miguel,12)
maestro1.registrar_nota(miguel,11)
maestro1.registrar_nota(miguel,11)
maestro1.evaluar_alumno(miguel)

miguel.accion()
miguel.identificarse()
miguel.ver_notas()
miguel.calcular_promedio()






        


        





        
    


        



        

                
        

    

    