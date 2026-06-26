"""
* EJERCICIO:
 * Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
 * en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
 * - Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición,
 *   recorrido, conversión a mayúsculas y minúsculas, reemplazo, división, unión,
 *   interpolación, verificación...
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que analice dos palabras diferentes y realice comprobaciones
 * para descubrir si son:
 * - Palíndromos
 * - Anagramas
 * - Isogramas
 """
def palindromos(palabra1,palabra2):
    if palabra1 == palabra1[::-1]:
        print(f"La palabra {palabra1} es: palindroma ")
    else:
         print(f"La palabra {palabra1} no es: palindroma ")
    
    if palabra2 == palabra2[::-1]:
        print (f"La palabra {palabra2} es: palindroma ")
    else:
        print(f"La palabra {palabra2} no es: palindroma ")
    
    
def anagrama(palabra1,palabra2):
    return f"La palabra: {palabra1} es anagrama de {palabra2}: {sorted(palabra1)==sorted(palabra2)}"  

def isograma(palabra):
    lista_de_palabra=set(palabra)
    if len(palabra)==len(lista_de_palabra):
        return (f"La palabra {palabra} es isograma")
   
    return (f"La palabra {palabra} no es isograma")

def problema(world1,world2):
    palindromos(world1,world2)

    print(anagrama(world1,world2))

    print(isograma(world1))
    print(isograma(world2))


problema("amor","persona")