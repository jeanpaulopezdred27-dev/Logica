""" 
* EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
"""
def saludo(*names):
    for name in names:
        print(f"Hola {name}")


saludo("Jean","Paul","Junior")

#Esto es raro, es la primera vez que veo en el argumento de la funcion ** es como pedir un diccionario

def datos(**name):
    for keys, i in name.items():
        print(f" {keys} es igual a: {i} ")

datos(nombre="jean",edad=24,apellido="Lopez")

#Funciones dentro de funciones

def agregado(palabra):
    def nombre(name):
        return f"hola {name} {palabra}"
    return nombre


print(agregado("puto")("jean"))

#Pon a prueba el concepto de variable LOCAL y GLOBAL.

#Una variable global tiene presencia en todo el programa, puede usarla incluso dentro de funciones

global_variable="Python"

def sal():
    print(f"Hola {global_variable}")

sal()

#Sin envargo las variables locales son variables que solo estan presentes en una parte del programa 

def prueba():
    local_variabler="Ppp"
    print(f"Hola {local_variabler}")

prueba()

# print(local_variable) jala a error porque solo esta presente en la funcion prueba

#Dificultad extra

def problem_extra(text1,textr2):
    contador=0
    for i in range(1,101):
        if i % 3==0 and i%5==0:
            print(f"el numero {i} es {text1} y {textr2}")
        elif i%3==0:
            print (f"El numero {i} es {text1}")
        elif i%5==0:
            print(f"El numero {i} es {textr2}")
        else: 
            print(i)
            contador +=1
    print(f"LA Cantidad de numeros que no son multiplos de 3 ni de 5 son: {contador}")
    
problem_extra("multiplo 3","multiplo 5")
