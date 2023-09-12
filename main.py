import os, time
from clases.Alphabets import Alphabets


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

def main():
    lenguage=[]
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
                break
            
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
                            print(f"la union de {alphabets.get_element(index1)} y de {alphabets.get_element(index2)} es:")  
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
                            longitud=int(input('ingresa la longitud de la cadena que desea generar:'))
                            cadena=alphabets.star_lock(index,longitud)
                            #alphabets.add_element(intercepcion)
                            print(f"la cerrradura de estrella del alfabeto es:{cadena}")  
                            input('presiona una tecla para continuar...')
                        case 7:        
                            pass
                        case 8:   
                            pass     
                        case 9: 
                            pass       
                        case 10:
                            pass        
                        case 11:
                            pass
                        case 0:
                            break
                        case _:
                            print("opcion invalida!")
                            input("presione para continuar")
            case 0:
                break    
                
if __name__ == "__main__":
    main()