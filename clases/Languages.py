from Operations import Operations

class Language(Operations):
    def __init__(self, lista):
        super().__init__(lista)
        
    def cardinality_language(language):
        return len(language)   
        
    def concatenate_languages(self):
        concatenate_language=[]
        for i in self.list:
            concatenate_language.extend(i)
            
        return concatenate_language    
    
    def inverse_language(self,language):
        inverse_laguage = list(reversed(language))

        return inverse_laguage
    
    def pow(self,language, potencia):
        listaPow=[""]
        if potencia != 0:
            for i in range(potencia):
                for j in list(listaPow):
                    palabra1 = (j)
                    for k in list(language):
                        palabraConcat = palabra1 + (k)
                        listaPow.append(palabraConcat)
        listaPow[:0] = '⌀'
        listaPow = list(set(listaPow))
        listaPow.sort(key=len)
        del listaPow[0]
        return listaPow
    
    
    
# lista=[]
# a1=[1, 2, 3, 4]
# a2=[3, 4, 5]
# a3=[3,4, 6, 7]
# lista.append(a1)
# lista.append(a2)
# lista.append(a3)
# print(lista)
# conjunto=Language(lista)
# print(conjunto.concatenate_languages())