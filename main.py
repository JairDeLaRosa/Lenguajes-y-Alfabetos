from clases.Alphabets import Alphabets
from clases.Languages import Language
import os, time

def procesar_alfabeto(alfabeto):
    alfabeto=alfabeto[1:len(alfabeto)-1]
    alfabeto=f"{alfabeto} "
    elemento_agregar=""
    alfabeto_procesado=[]
    for indice in range(len(alfabeto)):
        if alfabeto[indice] != " ":
            elemento_agregar=f"{elemento_agregar}{alfabeto[indice]}"
        else:
            alfabeto_procesado.append(elemento_agregar)
            elemento_agregar=""
            
    return alfabeto_procesado

def enterAlphabets(n):
    i=0
    listaAlphabets=[]
    for i in range(i,n):
        alphabet=input(f"Ingrese el alfabeto {i+1} entre llaves y separado por espacios: ")
        alphabet_process=procesar_alfabeto(alphabet)
        listaAlphabets.append(alphabet_process)
    
    return listaAlphabets

alphabets = Alphabets()
leng=Language()

def main():
    lenguages=[]
    while True:
        os.system("cls")
        print("""
          1-Ingresar alfabetos
          2-Crear lenguajes
          3-Opciones de alfabetos
          4-Opciones de lenguajes
    """)
        option=int(input("Ingrese la opción: "))
        match option:
            case 1:
                cant_alphabets=int(input("Ingrese la cantidad de alfabetos a ingresar: "))
                Listalphabets=enterAlphabets(cant_alphabets)
                for i in Listalphabets: 
                    alphabets.add_element(i) 
            case 2:
                
                number = input('How many words will each lenfuahe have?: ') 
                lenguage1=alphabets.star_lock(0,40)
                leng.add_element(lenguage1)
                lenguage2=alphabets.star_lock(0,40)
                leng.add_element(lenguage2)
                print('Languages created')
                input('presiona una tecla para continuar...')
            case 3:    
                while True:
                    os.system("cls")
                    print("""
                        1-mostrar alfabeto por indice
                        2-unir alfabetos por indice
                        3-diferencia alfabeto por indice
                        4-intercepcion de alfabeto por indice
                        5-cerradura de estrella de alfabeto
                        0-salir
                    """)
                    opcion = int(input("Ingrese la opcion: "))
                    match opcion:
                        case 1:#mostrar alfabeto
                            alphabets.mostrar()
                            input('presiona una tecla para continuar...')
                        case 2:#unir
                            index1=int(input('ingresa el primer indice: '))
                            index2=int(input('ingresa el segundo indice: '))
                            union=alphabets.union(index1, index2)
                            #alphabets.add_element(union)
                            print(f"la union de {alphabets.get_element(index1)} y de {alphabets.get_element(index2)} es:")  
                            print(union)
                            input('presiona una tecla para continuar...')
                        case 3:
                            index1=int(input('ingresa el primer indice: '))
                            index2=int(input('ingresa el segundo indice: '))
                            diferencia=alphabets.difference(index1,index2)
                            #alphabets.add_element(diferencia)
                            print(f"la diferencia de {alphabets.get_element(index1)} y de {alphabets.get_element(index2)} es:")  
                            print(diferencia)
                            input('presiona una tecla para continuar...')
                        case 4:
                            index1=int(input('ingresa el primer indice: '))
                            index2=int(input('ingresa el segundo indice: '))
                            intercepcion=alphabets.interception(index1,index2)
                            #alphabets.add_element(intercepcion)
                            print(f"la union de {alphabets.get_element(index1)} y de {alphabets.get_element(index2)} es:")  
                            print(intercepcion)
                            input('presiona una tecla para continuar...')
                        case 5:
                            index=int(input('ingresa el indice del alfabeto: '))
                            longitud=int(input('ingresa la cantidad de palabras que desea generar:'))
                            cadena=alphabets.star_lock(index,longitud)
                            #alphabets.add_element(intercepcion)
                            print(f"la cerrradura de estrella del alfabeto es:{cadena}")  
                            input('presiona una tecla para continuar...')
                        case 0:
                            break
                        case _:
                            print("opcion invalida!")
                            input("presione para continuar")
            
            case 4:
                while True:
                    os.system("cls")
                    print("""
                        1-mostrar lenguajes por indices
                        2-unir lenguajes
                        3-diferencia de lenguajes
                        4-intercepcion de lenguajes
                        5-Concatenación de lenguajes
                        6-Hallar la potencia de un lenguaje
                        7-Hallar inversa de un lenguaje
                        8-Hallar la cardinalidad de un lenguaje
                        0-Regresar
                    """)
                    opcion = int(input("Ingrese la opcion: "))
                    match opcion:
                        case 1:#mostrar
                            leng.mostrar()
                            input('presiona una tecla para continuar...')
                            
                        case 2:#unir
                            union_lenguage=leng.union(0,1)
                            print(f"la union de {leng.get_element(0)} y de {leng.get_element(1)} es:")  
                            print(union_lenguage)
                            input('presiona una tecla para continuar...')
                            
                        case 3:#diferencia
                            diferencia_lenguajes=leng.difference(0,1)
                            print(f"la diferencia de {leng.get_element(0)} y de {leng.get_element(1)} es:")  
                            print(diferencia_lenguajes)
                            input('presiona una tecla para continuar...')    
                            
                        case 4:#intercepción
                            intercepcion_lenguajes=leng.interception(0,1)
                            print(f"la intercepción de {leng.get_element(0)} y de {leng.get_element(1)} es:")  
                            print(intercepcion_lenguajes)
                            input('presiona una tecla para continuar...')    
                            
                        case 5: #concatenacion
                            concatenacion_lenguaje1=leng.get_element(0)
                            concatenacion_lenguaje2=leng.get_element(1)
                            concatenacion_lenguajes=leng.concatenate_languages(concatenacion_lenguaje1,concatenacion_lenguaje2)    
                            print(f"la concatenación de {leng.get_element(0)} y de {leng.get_element(1)} es:")  
                            print(concatenacion_lenguajes)
                            input('presiona una tecla para continuar...')
                            
                        case 6: #potencia de lenguaje
                            i=int(input('Insertar indice del lenguaje a sacar la potencia: '))
                            n=int(input('ingresar potencia "n": '))
                            lenguage_potencia=leng.get_element(i)
                            potencia_lenguaje=leng.pow(lenguage_potencia,n)
                            print(f"la potencia del lenguaje {leng.get_element(i)} es:")  
                            print(potencia_lenguaje)
                            input('presiona una tecla para continuar...')    
                            
                        case 7: #Inversa de lenguaje
                            i=int(input('Insertar indice del lenguaje a sacar la potencia: '))
                            lenguaje_inverso=leng.get_element(i)
                            inversa_lenguaje=leng.inverse_language(lenguaje_inverso)    
                            print(f"la inversa del lenguaje {leng.get_element(i)} es:")  
                            print(inversa_lenguaje)
                            input('presiona una tecla para continuar...')   
                            
                        case 8: #Cardinalidad
                            i=int(input('Insertar indice del lenguaje a sacar la cardinalidad: '))
                            lenguaje_cardinalidad=leng.get_element(i)
                            cardinalidad_lenguaje=leng.cardinality_language(lenguaje_cardinalidad)    
                            print(f"la inversa del lenguaje {leng.get_element(i)} es:")  
                            print(cardinalidad_lenguaje)
                            input('presiona una tecla para continuar...')   
                                
                                
                        case 0:
                            break
                            
                        case _:
                            print("opcion invalida!")
                            input("presione para continuar")
                            
            case 0:
                break    
                
if __name__ == "__main__":
    main()