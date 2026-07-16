#Problemas de lambda
#problema1
numeros = [15, 8, 42, 19, 3, 50]

mayor=max(numeros,key= lambda x:x)

print(mayor)


#problema2
palabras = ["Python", "Programación", "IA", "Computadora", "Código"]

palabra_larga= max(palabras,key=lambda x:len(x))
print(palabra_larga)

#problema3
palabra_corta=min(palabras,key=lambda x:len(x))
print(palabra_corta)

#problema4
productos = [
    {"nombre": "Laptop", "precio": 4200},
    {"nombre": "Mouse", "precio": 90},
    {"nombre": "Teclado", "precio": 180},
    {"nombre": "Monitor", "precio": 1200}
]

producto_mas_caro=max(productos, key= lambda x:x["precio"])

print(producto_mas_caro)

#problema5
producto_mas_barato= min(productos, key= lambda x:x["precio"])
print(producto_mas_barato)

#problema6
alumnos = [
    {"nombre": "Ana", "nota": 18},
    {"nombre": "Luis", "nota": 15},
    {"nombre": "Carlos", "nota": 20},
    {"nombre": "María", "nota": 17}
]
mayor_nota= max(alumnos,key= lambda x:x["nota"])
print(mayor_nota)

#problema7
alumnos = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 19},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "María", "edad": 22}
]

mas_joven= min(alumnos,key= lambda x:x["edad"])
print(mas_joven)
#problema8
productos = [
    {"nombre": "Laptop", "precio": 4200},
    {"nombre": "Mouse", "precio": 90},
    {"nombre": "Teclado", "precio": 180},
    {"nombre": "Monitor", "precio": 1200}
]
new_order= sorted( productos, key= lambda x:x["precio"])
print(new_order)
#problema9
por_nombre= sorted(productos, key= lambda x:x["nombre"])
print(por_nombre)

#problema10
alumnos = [
    {"nombre": "Ana", "nota": 18},
    {"nombre": "Luis", "nota": 15},
    {"nombre": "Carlos", "nota": 20},
    {"nombre": "María", "nota": 17}
]
de_mayor_a_menor= sorted(alumnos,reverse=True,key= lambda x:x["nota"])
print(de_mayor_a_menor)

#problema 11
productos = [
    {"nombre":"Laptop","precio":3500},
    {"nombre":"Mouse","precio":80},
    {"nombre":"Monitor","precio":1200},
    {"nombre":"USB","precio":40},
    {"nombre":"Teclado","precio":250}
]

productos_caros= list(filter(lambda x:x["precio"] >=500,productos ))
print(productos_caros)

#problema12
numeros = [1,2,3,4,5,6,7,8,9,10]
pares= list(filter(lambda x:not x%2,numeros))
print(pares)

#problema13

palabras = [
    "Python",
    "IA",
    "Computadora",
    "Sol",
    "Programación"
]

palaabras_largas= list(filter(lambda x:len(x)>6,palabras))
print(palaabras_largas)

#Problema 14
numeros = [2,4,6,8]

cuadrados= list(map(lambda x:x*x,numeros))
print(cuadrados)

#problema15
nombres = [
    "juan",
    "maria",
    "pedro",
    "lucia"]

nombres_mayuscula= list(map(lambda x:x.upper(),nombres))

print(nombres_mayuscula)

#problema16
productos = [
    {"nombre":"Mouse","precio":80},
    {"nombre":"Teclado","precio":200},
    {"nombre":"Monitor","precio":1200}
]

aumento_precio= list(map(lambda x: x["precio"] + x["precio"]*0.18,productos))
print(aumento_precio)

print("problea 17")
#problema 17
productos = [
    {"nombre":"Laptop","precio":3500,"stock":5},
    {"nombre":"Mouse","precio":90,"stock":20},
    {"nombre":"Monitor","precio":1500,"stock":3},
    {"nombre":"USB","precio":40,"stock":50},
    {"nombre":"Teclado","precio":180,"stock":10}
]

#parte 1
mas_caro= max(productos,key= lambda x:x["precio"])
print(mas_caro)

#parte 2
menos_stock= min(productos, key=lambda x:x["stock"])
print(menos_stock)

#parte 3
orden_nombre= sorted(productos,key= lambda x:x["nombre"])
print(orden_nombre)

#parte 4
poco_stock= list(filter(lambda x:x["stock"]<10,productos))
print(poco_stock)

#parte 5
nuevos_precios= list(map(lambda x:x["precio"]+x["precio"]*0.15,productos))
print(nuevos_precios)
