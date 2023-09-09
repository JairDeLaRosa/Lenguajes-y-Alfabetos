from alfabetos.SetOperations import SetOperations
import os, time

def enterAlphabets(N):
    i=0
    listAlphabets=[]
    for i in range(i,N):
        alphabet=set(input(f"ingrese el alfabeto separado {i + 1} por espacios: ").split(" "))
        listAlphabets.append(alphabet)
 
    return listAlphabets

alphabets=[]


while True:
    os.system("cls")
    print("""
        1-ingresa alfabeto
        2-mostrar
        0-salir
    """)
    opcion = int(input("Ingrese la opcion: "))
    match opcion:
        case 1:
            cant_alfabetos = int(input("Ingrese la cantidad de alfabetos a ingresar: "))
            alphabets = enterAlphabets(cant_alfabetos)
   
        case 2:
            print("alfabetos...", alphabets)
            time.sleep(4)
      
        case 0:
            break
        case _:
            print("opcion invalida!")
            input("presione para continuar")




