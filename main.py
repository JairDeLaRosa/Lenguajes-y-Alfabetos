from alfabetos.clases import SetOperations,Language,Alphabets
import os, time

def enterAlphabets(N):
    i=0
    listAlphabets=[]
    for i in range(i,N):
        alphabet=set(input(f"ingrese el alfabeto {i + 1} separado por espacios: ").split(" "))
        listAlphabets.append(alphabet)

    return listAlphabets

        # 1-ingresa alfabeto
        # 2-mostrar

        # 3-crear lenguaje
        # 4-union de alfabetos 
        # 5-intercepcion
        # 6-cardinal del lenguaje
        # 7-concatenar lenguaje
        # 8-inversa
        # 9-potencia  
        # 0-salir
while True:
    os.system("cls")
    print("""
          1-Ingresar alfabetos
          2-Crear lenguajes
          3-Opciones de alfabetos
          4-Opciones de lenguajes
    """)
    opcion = int(input("Ingrese la opcion: "))
    match opcion:
        case 1:
            cant_alfabetos = int(input("Ingrese la cantidad de alfabetos a ingresar: "))
            alphabets = enterAlphabets(cant_alfabetos)
   
        case 2:
            #Importan !! alphabet is a set of sets and to use this function it must be a list of lists.
            languages=[]
            alphabets = [list(subset) for subset in alphabets]
            number = int(input("Enter how many words you want the language to have: "))
            language = Language.create_language(alphabets, number)   
            languages.append(language) 
            language = Language.create_language(alphabets, number)   
            languages.append(language)           
        case 3:
            while True:
                os.system("cls")
                print("""
                      1-Mostrar Alfabetos
                      2-Calcular unión
                      3-Calcular diferencia
                      4-Calcular intersección
                      5-Cerradura de estrella
                      0-Regresar
                """)
                opcion = int(input("Ingrese la opcion: "))
                match opcion:
                    case 1:
                        os.system("cls")
                        print("alfabetos...", alphabets)
                        time.sleep(15)
                    case 2:
                        union_alphabets=Alphabets.union(alphabets[0],alphabets[1])
                        print(f"La unión de los alfabetos es: {union_alphabets}")
                        time.sleep(15)
                    case 3:
                        difference_alphabets=Alphabets.difference(alphabets[0],alphabets[1])
                        print(f"La diferenfia de los alfabetos es: {difference_alphabets}")
                        time.sleep(15)
                    case 4:
                        interception_alphabets=Alphabets.interception(alphabets[0],alphabets[1])
                        print(f"La intersección de los alfabetos es: {interception_alphabets}")
                        time.sleep(15) 
                    case 5:
                        for i in alphabets:
                            number_of_words=int(input('Digite la cantidad de palabras que desea tener la cerradura: '))
                            star_lock= Alphabets.star_lock(i,number_of_words)
                            print(star_lock)      
                    case 0:
                        break                   
        case 4:
            while True:
                os.system("cls")
                print("""
                      1-Mostrar lenguajes
                      0-Regresar
                """)
                opcion = int(input("Ingrese la opcion: "))
                match opcion:
                    case 1:
                        os.system("cls")
                        print("language...", languages)
                        time.sleep(15)
                    case 0:
                        break      
        case 0:
            break
        case _:
            print("opcion invalida!")
            input("presione para continuar")




