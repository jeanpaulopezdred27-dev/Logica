#Problema 1

lista_prueba=[1,3,5,6]

def obtener_pares(lista):
    pares=[]
    for i in lista:
        if  i%2==0:
            pares.append(i)
        
    return pares



print(obtener_pares(lista_prueba))

#problemas 2
productos = [
    {"name": "Mouse", "precio": 50, "stock": 10},
    {"name": "Teclado", "precio": 120, "stock": 5},
    {"name": "Monitor", "precio": 900, "stock": 2},
]
total=0
for i in productos:
    total_producto=i["precio"] * i["stock"]
    print(f" La cantidad  de {i["name"]}: {total_producto}")
    total+=total_producto

print(total)

nuevo_orden= sorted(productos,key=lambda x:x["precio"])

print(f"El producto más caro es: {nuevo_orden[len(nuevo_orden)-1]["name"]}")

#tambien puede ser:
mayor_precio=max(productos,key=lambda x:x["precio"]) #mayor precio seria todo el diccionario del producto más caro

print(f"El producto con mayor precio es: {mayor_precio["name"]}")

print(mayor_precio)
print(nuevo_orden)