"""
EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 """
 #Es una funcion que se llama a si misma

 
def cuenta_regresiva(numero):
    if numero>=0:
        print(numero)
        cuenta_regresiva(numero-1)

cuenta_regresiva(10)

#Esta es la version correcta de hacerlo, la recursividad no se usa para este tipos de caso, pero esta bien para el ejemplo
print("con for")
for i in range(10,0,-1):
    print(i)
print("Factorial")

def factorial(numero):
    if numero==0:
        return 1
    elif numero==1:
        return 1
    elif numero<0:
        return "Los numeros negativos no sacan factorial"
    else:
        return numero * factorial(numero-1)
 

print(factorial(5))

def fibonacci(numero):
    if numero<=0:
        print("El valor no puede ser 0 o menor")
        return 0
    elif numero==1:
        return 0
    elif numero==2:
        return 1
    else:
        return fibonacci(numero-1) +fibonacci(numero-2)

print(fibonacci(5))
    
#Parece que para esto de la recursividad primero tenemor que encontrar los excedentes.


