#las pruebas unitarias sirven para probra una parte de nuestro codigo en especifico 

# La mejor libreria para haacer puebas  en python es unittest
import unittest
from datetime import datetime,date
def sum(a,b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        raise ValueError("Los argumentos tienen que ser enteros o decimales")


    return a+b

#Para python es necesario que el test este dentro de una clase y siepre tiene que comenzar con la palabra test para que la 
#libreria pueda detectarlo como un test

class TestSum(unittest.TestCase):
    def test_sum(self): #Estos son los test que va a correr para verificvar si esta bien nuestra funcion sum()
        self.assertEqual(sum(5,7),12)
        self.assertEqual(sum(1,2),3)

    def test_sum_type(self):
        with self.assertRaises(ValueError):
            sum("5",7)
        with self.assertRaises(ValueError):
            sum(5,"7")
        with self.assertRaises(ValueError):
            sum("5","7")
        with self.assertRaises(ValueError):
            sum(5,"a")
        with self.assertRaises(ValueError):
            sum(None,7)
        

diccionario={"name":"Jean Paul","edad":24,"birthdate":"27/10/2001","lenguajes":["python","java"]}

class TestDiccionario(unittest.TestCase):

    def setUp(self):
        self.diccionario={"name":"Jean Paul","edad":24,"birthdate":datetime.strptime("27-10-2001","%d-%m-%Y").date(),"lenguajes":["python","java"]}


    
    def test_diccionario_keys(self):
        self.assertIn("name",self.diccionario)
        self.assertIn("edad",self.diccionario)
        self.assertIn("birthdate",self.diccionario)
        self.assertIn("lenguajes",self.diccionario)

    def test_diccionario_value(self):
        self.assertEqual(self.diccionario["name"],"Jean Paul") #Esto esta bien pero solo en el caso de que sepamos la respuesta, ya que si es un app para que pueda subir datos, 
        #nosotros no sabemos cuales son los datops de los clientes, lo mejor es verificar el tipo de dato que ingresa el usuario
        self.assertIsInstance(self.diccionario["name"],str)
        self.assertIsInstance(self.diccionario["edad"],int)
        self.assertIsInstance(self.diccionario["birthdate"],date)
        self.assertIsInstance(self.diccionario["lenguajes"],list)


    



unittest.main()
