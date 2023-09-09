import random
class SetOperations:
    def __init__(self, alphabet1,alphabet2):
          def __init__(self):
            self.list = []

    def add_index(self, index):
        self.list.append(index)

    def get_index(self, index):
        return self.list[index]

    def set_list(self, list):
        self.list = list
    
    def get_list(self):
        return self.list
    
    def union(self, index1, index2):
        list_result = set(self.list[index1]) | set(self.list[index2])
        return list(list_result)
    
    def difference(self, index1, index2):
        list_result = []
        for index in self.list[index1]:
            if index not in self.list[index2]:
                list_result.append(index)
        return list_result
        
    def interception(self, index1, index2):
        list_result = []
        for index in self.list[index1]:
            if index in self.list[index2]:
                list_result.append(index)
        return list_result
    

class Alphabets(SetOperations):
    def star_lock(self, index, cant_word):
        list_result=[]
        Alphabet=self.list[index]
        i=0
        while i in cant_word:
            word=''
            for j in range(random.randint(2,5)):
                word += str(random.choice(Alphabet))
            if(word not in list_result):
                list_result.append(word)    
            else:
                i-=1    
            
            i+=1    
        
        
        # def cerradura_de_estrella(vector, cantidad):
        #     letras = vector[0]
        #     numeros = vector[1]
        #     cerradura = []

        #     for _ in range(cantidad):
        #         letra = random.choice(letras)
        #         numero = random.choice(numeros)
        #         elemento = f"{letra}{numero}"
        #         cerradura.append(elemento)

        #     return cerradura
        
    
    
class Language(SetOperations):

    def create(alphabet, number):
        symbol1 = alphabet[0]
        symbol2 = alphabet[1]
        language = []
        
        for _ in range(number):
            symbol1 = random.choice(symbol1)
            symbol2 = random.choice(symbol2)
            word = F"{symbol1}{symbol2}"
            language.append(word)
        
        return language