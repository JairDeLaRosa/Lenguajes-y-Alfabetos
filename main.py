from clases.Alphabets import Alphabets
from clases.Languages import Language
import os, time

def process_alphabets(alphabet):
    alphabet=alphabet[1:len(alphabet)-1]
    alphabet=f"{alphabet} "
    add_element=""
    process_alphabet=[]
    for index in range(len(alphabet)):
        if alphabet[index] != " ":
            add_element=f"{add_element}{alphabet[index]}"
        else:
            process_alphabet.append(add_element)
            add_element=""
            
    return process_alphabet

def enterAlphabets(n):
    i=0
    listaAlphabets=[]
    for i in range(i,n):
        alphabet=input(f"Enter the alphabet {i+1} between braces and separated by spaces: ")
        process_alphabet=process_alphabets(alphabet)
        listaAlphabets.append(process_alphabet)
    
    return listaAlphabets

alphabets = Alphabets()
leng = Language()

def main():    
    while True:
        os.system("cls")
        print("""
          1 - Enter alphabets
          2 - Create languages
          3 - Alphabet options
          4 - Language options
          0 - Exit
    """)
        option=int(input("Enter option: "))
        match option:
            case 1:
                cant_alphabets=int(input("Enter the number of alphabets to enter: "))
                Listalphabets=enterAlphabets(cant_alphabets)
                for i in Listalphabets: 
                    alphabets.add_element(i) 
            case 2:
                
                number = int(input('How many words will each lenfuahe have?: '))
                lenguage1=alphabets.star_lock(0,number)
                leng.add_element(lenguage1)
                lenguage2=alphabets.star_lock(0,number)
                leng.add_element(lenguage2)
                print('Languages created')
                input('press a key to continue...')
            case 3:    
                while True:
                    os.system("cls")
                    print("""
                        1 - Show alphabet by index
                        2 - Join alphabets by index
                        3 - Alphabet difference by index
                        4 - Alphabet interception by index
                        5 - Alphabet star lock
                        0 - Back
                    """)
                    opcion = int(input("Enter option: "))
                    match opcion:
                        case 1:#mostrar alfabeto
                            alphabets.show()
                            input('press a key to continue...')
                        case 2:#unir
                            index1=int(input('Enter the first index: '))
                            index2=int(input('Enter the second index: '))
                            union=alphabets.union(index1, index2)
                            print(f"The union of {alphabets.get_element(index1)} and of {alphabets.get_element(index2)} is: \n")  
                            print(union)
                            input('press a key to continue...')
                        case 3:#difference
                            index1=int(input('Enter the first index: '))
                            index2=int(input('Enter the second index: '))
                            diferencia=alphabets.difference(index1,index2)
                            print(f"The difference of {alphabets.get_element(index1)} and of {alphabets.get_element(index2)} is: \n")  
                            print(diferencia)
                            input('press a key to continue...')
                        case 4:#interception
                            index1=int(input('Enter the first index: '))
                            index2=int(input('Enter the second index: '))
                            intercepcion=alphabets.interception(index1,index2)
                            print(f"The interception of {alphabets.get_element(index1)} and of {alphabets.get_element(index2)} is: \n")  
                            print(intercepcion)
                            input('press a key to continue...')
                        case 5:#star lock
                            index=int(input('Enter the alphabet index: '))
                            longitud=int(input('Enter the number of words you want to generate:'))
                            cadena=alphabets.star_lock(index,longitud)
                            print(f"the alphabet star lock is: \n {cadena}")  
                            input('press a key to continue...')
                        case 0:
                            break
                        case _:
                            print("Invalid option! ")
                            input("press a key to continue...")
            
            case 4:
                while True:
                    os.system("cls")
                    print("""
                        1 - Show languages by indexes
                        2 - Join languages
                        3 - Difference of languages
                        4 - Language interception
                        5 - Language concatenation
                        6 - Find the power of a language
                        7 - Find the inverse of a language
                        8 - Find the cardinality of a language
                        0 - Back
                    """)
                    opcion = int(input("Enter option: "))
                    match opcion:
                        case 1:#Mostrar
                            leng.show()
                            input('press a key to continue...')
                            
                        case 2:#unir
                            languaje_union=leng.union(0,1)
                            print(f"The union of {leng.get_element(0)} and of {leng.get_element(1)} is: \n")  
                            print(languaje_union)
                            input('press a key to continue...')
                            
                        case 3:#diferencia
                            languaje_difference=leng.difference(0,1)
                            print(f"The difference of {leng.get_element(0)} and of {leng.get_element(1)} is: \n")  
                            print(languaje_difference)
                            input('press a key to continue...')    
                            
                        case 4:#intercepción
                            languaje_interception=leng.interception(0,1)
                            print(f"The interception of {leng.get_element(0)} and of {leng.get_element(1)} is: \n")  
                            print(languaje_interception)
                            input('press a key to continue...')    
                            
                        case 5: #concatenacion
                            languaje_concatenation1=leng.get_element(0)
                            languaje_concatenation2=leng.get_element(1)
                            languaje_concatenation=leng.concatenate_languages(languaje_concatenation1,languaje_concatenation2)    
                            print(f"The concatenation of {leng.get_element(0)} and of  {leng.get_element(1)} is: \n")  
                            print(languaje_concatenation)
                            input('press a key to continue...')
                            
                        case 6: #potencia de lenguaje
                            i=int(input('Insert language index to extract the power: '))
                            n=int(input('Enter power "n": '))
                            languaje_pow=leng.get_element(i)
                            languaje_power=leng.pow(languaje_pow,n)
                            print(f"The power of languaje {leng.get_element(i)} is: \n")  
                            print(languaje_power)
                            input('press a key to continue...')    
                            
                        case 7: #Inversa de lenguaje
                            i=int(input('Insert language index to get the inverse: '))
                            languaje_torevert=leng.get_element(i)
                            languaje_reverse=leng.inverse_language(languaje_torevert)    
                            print(f"The reverse of languaje {leng.get_element(i)} is: \n")  
                            print(languaje_reverse)
                            input('press a key to continue...')   
                            
                        case 8: #Cardinalidad
                            i=int(input('Insert language index to get cardinality: '))
                            languaje_tocardinality=leng.get_element(i)
                            languaje_carninality=leng.cardinality_language(languaje_tocardinality)    
                            print(f"The cardinality of languaje {leng.get_element(i)} is: \n")  
                            print(languaje_carninality)
                            input('press a key to continue...')   
                                
                                
                        case 0:
                            break
                            
                        case _:
                            print("Invalid Option! ")
                            input("press a key to continue...")
                            
            case 0:
                break    
                
if __name__ == "__main__":
    main()