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
index=0
for i in productos:
    print(f" La cantidad  de {i["name"]}: {i["precio"] * i["stock"]}")        
