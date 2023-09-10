<<<<<<< HEAD
from alfabetos.clases import SetOperations
=======
from alfabetos.SetOperations import SetOperations, Language
>>>>>>> 55479fce439e3b18d3fda63196ec41d9639beba9
import os, time

def enterAlphabets(N):
    i=0
    listAlphabets=[]
    for i in range(i,N):
        alphabet=set(input(f"ingrese el alfabeto separado {i + 1} por espacios: ").split(" "))
        listAlphabets.append(alphabet)

    return listAlphabets

alphabets=[]

<<<<<<< HEAD
lista = SetOperations






# while True:
#     os.system("cls")
#     print("""
#         1-ingresa alfabeto
#         2-mostrar
#         0-salir
#     """)
#     opcion = int(input("Ingrese la opcion: "))
#     match opcion:
#         case 1:
#             cant_alfabetos = int(input("Ingrese la cantidad de alfabetos a ingresar: "))
#             alphabets = enterAlphabets(cant_alfabetos)

#         case 2:
#             print("alfabetos...", alphabets)
#             time.sleep(2)

#         case 0:
#             break
#         case _:
#             print("opcion invalida!")
#             input("presione para continuar")
=======

while True:
    os.system("cls")
    print("""
        1-ingresa alfabeto
        2-mostrar
        3-crear lenguaje
        4-union de alfabetos 
        5-intercepcion
        6-cardinal del lenguaje
        7-concatenar lenguaje
        8-inversa
        9-potencia  
        0-salir
    """)
    opcion = int(input("Ingrese la opcion: "))
    match opcion:
        case 1:
            cant_alfabetos = int(input("Ingrese la cantidad de alfabetos a ingresar: "))
            alphabets = enterAlphabets(cant_alfabetos)
   
        case 2:
            os.system("cls")
            print("alfabetos...", alphabets)
            time.sleep(4)
        case 3:
            #Importan !! alphabet is a set of sets and to use this function it must be a list of lists.
            alphabets = [list(subset) for subset in alphabets]
            number = int(input("Enter how many words you want the language to have: "))
            language = Language.create_language(alphabets, number)
            print("labguage...", language)
            time.sleep(4)

        case 4:
            break
        case 5:
            break
        case 6:
            break
        case 7:
            break
        case 8:
            break
        case 0:
            break
        case _:
            print("opcion invalida!")
            input("presione para continuar")
>>>>>>> 55479fce439e3b18d3fda63196ec41d9639beba9




