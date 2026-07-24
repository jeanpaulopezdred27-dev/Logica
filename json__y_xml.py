"""
* IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 *
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
 """
 
import xml.etree.ElementTree as xml
import os
import json


data={"name":"Jean Paul Lopez Davila","age":24,"birthday":"27/10/2001","lenguajes":["Python","Java","Rubi"]}

def save_xml():
    root=xml.Element("data") #El element es par indicar la clase padre o el nudo padre

    for key,value in data.items(): #El .items() es usado para diccionarios para unir la llave con el valor
        child=xml.SubElement(root,key)
        if isinstance(value,list): #el isinstance es para compravar si una variable es de un tipo de dato en especifico.
            for i in value:
                xml.SubElement(child,"item").text=i
        else:
            child.text=str(value)
    #Ahora que tenemos todo creado tenemos que crear un arbol de gerarquia

    tree=xml.ElementTree(root)
    xml.indent(tree, space="    ", level=0)
    tree.write("jean.xml")



save_xml()

with open("jean.xml","r") as paper:
    print(paper.readlines())

####################### json


json_file="jeanpaul.json"

with open(json_file,"w") as datajson:
    json.dump(data,datajson)

with open(json_file,"r") as datajson:
    print(datajson.read())

