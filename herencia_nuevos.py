#Problema de Sistema de Biblioteca

class Persona:
    
    def __init__(self,name,id):
        self.name=name
        self.id=id
    
    def identificarse(self):
        print(f"Nombre: {self.name}\nID: {self.id}")

    def accion(self):
        pass


class bibliotecario(Persona):
    def __init__(self, name, id,area_de_trabajo):
        super().__init__(name, id)
        self.area_de_trabajo=area_de_trabajo

    def identificarse(self):
        super().identificarse()
        print(f"Area de trabajo: {self.area_de_trabajo}")

    def accion(self):
        while True:
            accion=input("Que esta haciendo el bibliotecario: Organizando libros(o) o atendiendo lectores(a)")

            if accion=="o":
                print(f"El bibliotecario {self.name} esta organizzando libros.")
                break
            elif accion=="a":
                print(f"El bibliotecario {self.name} esta atendiendo a los lectores.")
                break
            else:
                print(f"La variable {accion} no es valida, por favor ingresa una variable valida.")
    
    def prestar_libro(self,lector,libro):
        lector.lista_libros.append(libro)
        print(f"El libro {libro.titulo} se presto.")

    def devolver_libro(self,lector,libro):
         lector.lista_libros.remove(libro)
         print(f"Se devolvio corrrctamente el libro: {libro}")
         try:
             lector.lista_librs.remove(libro)
         except Exception as error:
             print(f"El error es: {error}")
             print(f"El libro {libro} no pertenece a la biblioteca.")

class Lector(Persona):

    def __init__(self, name, id,carrera):
        super().__init__(name, id)
        self.carrera=carrera
        self.lista_libros=[]
    
    def identificarse(self):
        super().identificarse()
        print(f"Profesion: {self.carrera}")

    def accion(self):

        while True:
            accion=input("Que esta haciendo el lector: leyendo(l) o buscando libro(b)")

            if accion=="l":
                print(f"El lector {self.name} esta leyendo libros.")
                break
            elif accion=="b":
                print(f"El lector {self.name} esta buscando un libro.")
                break
            else:
                print(f"La variable {accion} no es valida, por favor ingresa una variable valida.")
    
    def ver_libro_prestados(self):
        
        if len(self.lista_libros)==0:
            print("No tienes ningun libro prestado")
        else:
            conteo=1
            for libro in self.lista_libros:
                print(f"{conteo}. {libro.titulo}")
                conteo+=1
        

        
class Libro:

    def __init__(self,titulo,autor,disponibe=bool):
        self.titulo=titulo
        self.autor=autor
        self.disponible=disponibe

    def mostrar_informacion(self):
        print(f"Nombre: {self.titulo}\nAutor: {self.autor}\n Disponible: {self.disponible}")



jean=bibliotecario("Jean Paul Lopez Davila",23456,"infantil")
miguel=Lector("Miguel Lopez",21234,"Ing. Industrial")
libro1=Libro("la divina comedia","Dante",True)
libro2=Libro("Don Quijote","Paul",True)
libro3=Libro("Hola que tal","Lopez",True)


jean.identificarse()
jean.accion()
jean.prestar_libro(miguel,libro1)
jean.prestar_libro(miguel,libro2)
jean.prestar_libro(miguel,libro3)

miguel.identificarse()
miguel.accion()
miguel.ver_libro_prestados()



            

             
         
            
             




