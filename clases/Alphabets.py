from Operations import Operations    
import random

class Alphabets(Operations):
    def __init__(self, lista):
        super().__init__(lista)    
    
    def Cerradura(self, conjunto,numPalabras):
        lenguaje = list()
        while len(set(lenguaje)) != numPalabras:
            potencia = random.randint(1, 5)  # numero de caracteres en la palabra
            palabra = ''
            for i in range(potencia):  # creacion de la cadena
                letra = random.choice(list(conjunto))
                palabra = letra + palabra
            lenguaje.append(palabra)
        return lenguaje