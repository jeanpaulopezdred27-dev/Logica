print("Problema 1")

#verificacion si es par

import unittest


def par(a):
    if a%2==0:
        return True
    else:
        return False


class Test_par(unittest.TestCase):

    def test_validacion(self):
        self.assertEqual(par(2), True)
        self.assertEqual(par(3), False)
        self.assertTrue(par(4)) #Mejor manerr de resolver
        self.assertFalse(par(5))



print("Problema 2 mayoria de edad")

def mayor_edad(number):
    if number <1:
        raise ValueError ("no puedes tener 0 años o menos")
    elif number<18:
        return False
    else:
        return True

class Test_mayor_edad(unittest.TestCase):

    def test_edades(self):
        self.assertTrue(mayor_edad(18))
        self.assertTrue(mayor_edad(20))
        self.assertFalse(mayor_edad(17))

    def test_edades_irregulares(self):
        with self.assertRaises(ValueError):
            mayor_edad(0)
        with self.assertRaises(ValueError):
            mayor_edad(-1)

print("Problema 3 invertir texto")

def invertir(texto=str):
    return(texto[::-1])
    
        
class Test_invertir(unittest.TestCase):

    def test_words(self):
        self.assertEqual(invertir("hola"),"hola"[::-1])
        self.assertEqual(invertir("python"),"nohtyp")
        self.assertEqual(invertir(""),"")
        self.assertEqual(invertir("a"),"a")


print("Problema 4 sumar lista")

def sum_lista(lista):
    return sum(lista)


class Test_sum_lista(unittest.TestCase):
    def test_totales(self):
        self.assertEqual(sum_lista([1,2,3,4,5]),15)
        self.assertEqual(sum_lista([]),0)
        self.assertEqual(sum_lista([-1,5]),4)
        self.assertEqual(sum_lista([100]),100)

    def test_type(self):
        with self.assertRaises(TypeError):
            sum_lista(100)

print("Problema 5: Número mayor")

def numero_mayor(lista):
    return max(lista)

class Test_numero_mayor(unittest.TestCase):

    def test_verificacion(self):
        self.assertEqual(numero_mayor([5,8,2]),8)
        self.assertEqual(numero_mayor([-5,-1,-9]),-1)
        self.assertEqual(numero_mayor([100]),100)

    def test_raises(self):
        with self.assertRaises(ValueError):
            numero_mayor([])
        








unittest.main()
