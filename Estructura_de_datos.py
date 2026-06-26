"""

 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto
 *   en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 */
 """
#Hay muchos tipo de estructuras de datos
"""
my_lista=["Jean","paul","Junior"]

my_lista.append("Miguel") #Operacion para agregar
print(my_lista)
#Operaciones para eliminar los elementos de la lista 
my_lista.pop(2) #Eliminar segun su orden
print(my_lista)
my_lista.remove("Miguel") #Eliminacion segun la cadena ingresada 
print(my_lista)
my_lista.append("Lopez")
my_lista.append("Davila")
my_lista.append("Alexa")
my_lista.append("Katherine")

print(my_lista[1])
my_lista[1]="Ang" #Con esto intercambiamos el valor en un lugar en especifico
print(my_lista[1])
print(my_lista)
my_lista.sort()
print(my_lista)

# Las tuplas son listas inmutables

my_tuplas=("Jean","Lopez","Jeanpaulopezdred.27@gmail.com")
 
#Ahora este es una lista inmutable
#Si quisieramos cambiarlo debemos usar el sorted, a parte de convertir en lista la ordena 
print(type(my_tuplas)) #<class 'tuple'>

my_tuplas=sorted(my_tuplas)

print(type(my_tuplas)) #<class 'list'>
print(my_tuplas)
"""
"""
 DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no numéricos y con más
 *   de 9 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
 """
#Primero generamos una diccionario con los nombres de usuario y su numero de contacto 
#Vamos a crear funciones en este mismo file pero podria ser en otro e importarlo par que
contactos_diccionario={"Jean":"931250171","Miguel":"987654321","Jesus":"927441797"}

def buscar_contacto(key):
    if key in contactos_diccionario:
        return f"El numero de contacto es: {contactos_diccionario[key]}"
    return f"El contacto {key} no se encontro en tus contactos."

def verificacion_numero(numero):
    if not numero.isdigit():
        print("Por favor ingresa solo numeros")
        return False
        
    if len(numero)!=9:
        print(f"Por favor ingresa un numero valido de 9 digitos, el numero {numero} no es valido ya que tiene {len(numero)}")
        return False
    return True
        
   

while True:
    try:
        que_hacer=int(input("Buscar contacto   (1)\nInsertar contacto   (2)\nActualizar concto   (3)\nEliminar contato   (4)\nSalir del app   (5)\n"))
    except ValueError:
        print(f"Tienes un error, por favor ingrsa una de las variables que te mencionamos antes: 1,2,3,4,5")
        continue

    if que_hacer==1:
        nombre=input("Que contacto desea buscar? ----:")
        print(buscar_contacto(nombre))


    elif que_hacer==2:
        nombre=input("Que contacto desea agregar? ----:")
        numero=input(f"Cual es el numero de contacto de {nombre}----:")
        if verificacion_numero(numero):
            contactos_diccionario[nombre]=numero
            print(f"Perfecto, su contaco: {nombre} con numero {numero} fue guardado exitosamente.")
            

    elif que_hacer==3:
        nombre=input("Que contacto desea modificar? ----:")
        numero=input(f"Cual es el numero de contacto a modificar ----:")
            
        if nombre in contactos_diccionario:
            if verificacion_numero(numero):
                contactos_diccionario[nombre]=numero
                print(f"El nombre se actualizo correctamente, ahora el contaco {nombre} tiene el numero: {numero}")
        else:
            if verificacion_numero(numero):
                print(f"El contacto: {nombre} no se encuentra en tus contactos\nSe va a agregar a tu contacto como nuevo.")
                contactos_diccionario[nombre]=numero
    elif que_hacer==4:
        nombre=input("Que contacto desea eliminar? ----:")
        if not nombre in contactos_diccionario:
            print(f"El contacot {nombre} no se encontro en tu lista de contactos.")
        else:
            contactos_diccionario.pop(nombre)
            print(f"Contacto {nombre} elimnado. ")
    
    elif que_hacer==5:
        print(f"Gracias por usar el aplicativo...\nHazta luego.")
        break
    
    else:
        print(f"El valor {que_hacer} no es valido, por favor ingresa uno de los valores:\n 1,2,3,4,5" )





        

print(contactos_diccionario)