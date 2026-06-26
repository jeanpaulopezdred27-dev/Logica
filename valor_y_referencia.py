"""
* EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como
 * variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime
 *   el valor de las variables originales y las nuevas, comprobando que se ha invertido
 *   su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""

#Tipos de datos de valor 
valor_a=10
valor_b=30
valor_b=valor_a
valor_a=29
print(valor_a)
print(valor_b)

#Tipos de datos de referencial son: una lista1,
# print(lista2)
# 
#
# lista1,lista2=cambio_referenciales(lista1,lista2)
#  tupla un set un diccionario
lista_a=[1,2,3,4]
lista_b=[9,8,7,6]
lista_b=lista_a
lista_b.append(555)
print(lista_a)
print(lista_b)
#Cuando igualas los datos de referencia se modifican ambos sin importar nada


print("Problema adicional")
print("Funcion con dato valor")

my_int_a=10
my_int_b=20

def cambio(valor_a,valor_b):
    paso=valor_a
    valor_a=valor_b
    valor_b=paso
    return valor_a,valor_b

my_int_a,my_int_b=cambio(my_int_a,my_int_b)
print(my_int_a)
print(my_int_b)


def cambio_referenciales(valor_a,valor_b):
    #valor_a.append(33)
    paso=valor_a
    valor_a=valor_b
    valor_b=paso
    return valor_a,valor_b
    
lista1=[1,2,3,4]
lista2=[6,7,8,9]

print(lista1)
print(lista2)

lista1,lista2=cambio_referenciales(lista1,lista2)
print(lista1)
print(lista2)
