from .Operations import Operations
import random

class Language(Operations):  
        
    def cardinality_language(self,language):
        return len(language)   
        
    def concatenate_languages(self, language1, language2):
        concatenate_language=[]
        element=''
        for i in language1:
            for j in language2:
                element=f"{i}{j}"
                element=element.replace('#', '')
                if element != '':
                    concatenate_language.append(element)
        return concatenate_language    
    
    def inverse_language(self, language):
        reversed_lista = [cadena[::-1] for cadena in language]

        return reversed_lista
    
    
    def pow(self, language, potencia):
        listaPow=[]
        pow={}
        if potencia > 0:
            listaPow.extend(language)
            for num in range(potencia-1):
                listaPow.extend(self.concatenate_languages(listaPow,language))
                
        listaPow=set(listaPow)
        listaPow=listaPow | set(language)        
                
        return list[listaPow]        
    
#pruebas finales
# lista=[]
# a1=['ab','cd', 'dc'] 
# a2=[3, 4, 5]
# a3=[3,4, 6, 7]
# lista.append(a1)
# lista.append(a2)
# lista.append(a3)
# print(lista)
# conjunto=Language()
# print(conjunto.concatenate_languages(a1,a2))
