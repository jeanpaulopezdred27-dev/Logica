#Problemas de excepciones con logica demouredev
"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
"""

#Es con try exception el try es el codigo que pueda petar y el exception se va a ejecutar si figura un error en el try

try:
    print(10/0)
except:
    print("eres un pendejo")

class MiExcepcion(Exception):
    pass


def prueba_excepciones(parametro:list):

    if len(parametro) <3:
        raise IndexError()
    
    elif parametro[1]==0:
        raise ZeroDivisionError()
    elif type(parametro[2])==str:
        raise MiExcepcion()
    
    print(parametro[2])
    print(parametro[0]/parametro[1])
    print(parametro[2])

lista_prueba=[1,1,2,2]
try:
    prueba_excepciones(lista_prueba)
except IndexError:
    print("Metele mas elementos pes causa")
except ZeroDivisionError:
    print("No puedes dividir entre cero, cambia el segundo elemento de tu lista")
except MiExcepcion :
    print("Esta viene de mi clase")
    
except Exception as e:
    print(f"Se a producido un error inesperado: {e}")

else:
    print("No se ejecuto ningun error")

finally:
    print("El problema se ejecuta siun problemas")




