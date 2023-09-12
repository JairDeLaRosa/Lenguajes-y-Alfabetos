from alfabetos.SetOperations import SetOperations,Language,Alphabets
import os, time

def enterAlphabets(N):
    i=0
    listAlphabets=[]
    for i in range(i,N):
        alphabet=set(input(f"ingrese el alfabeto {i + 1} separado por espacios: ").split(" "))
        listAlphabets.append(alphabet)
    return listAlphabets

alphabets = Alphabets()

while True:
    os.system("cls")
    print("""
        1-ingresa alfabeto
        2-mostrar alfabeto por indice
        3-unir alfabetos por indice
        4-diferencia alfabeto por indice
        5-intercepcion de alfabeto por indice
        6-cerradura de estrella de alfabeto
        0-salir
    """)
    opcion = int(input("Ingrese la opcion: "))
    match opcion:
        case 1:#ingresar alfabeto
            cant_alfabetos = int(input("Ingrese la cantidad de alfabetos a ingresar: "))
            Listalphabets = enterAlphabets(cant_alfabetos)
            for i in Listalphabets: 
                alphabets.add_element(i) 
        case 2:#mostrar alfabeto
            alphabets.mostrar()
            input('presiona una tecla para continuar...')
        case 3:#unir
            index1=int(input('ingresa el primer indice: '))
            index2=int(input('ingresa el segundo indice: '))
            union=alphabets.union(index1, index2)
            #alphabets.add_element(union)
            print(f"la union de {alphabets.get_element(index1)} y de {alphabets.get_element(index2)} es:")  
            print(union)
            input('presiona una tecla para continuar...')
        case 4:
            index1=int(input('ingresa el primer indice: '))
            index2=int(input('ingresa el segundo indice: '))
            diferencia=alphabets.difference(index1,index2)
            #alphabets.add_element(diferencia)
            print(f"la union de {alphabets.get_element(index1)} y de {alphabets.get_element(index2)} es:")  
            print(diferencia)
            input('presiona una tecla para continuar...')
        case 5:
            index1=int(input('ingresa el primer indice: '))
            index2=int(input('ingresa el segundo indice: '))
            intercepcion=alphabets.interception(index1,index2)
            #alphabets.add_element(intercepcion)
            print(f"la union de {alphabets.get_element(index1)} y de {alphabets.get_element(index2)} es:")  
            print(intercepcion)
            input('presiona una tecla para continuar...')
        case 6:
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
        case _:
            print("opcion invalida!")
            input("presione para continuar")