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
                Alphabets=enterAlphabets(cant_alphabets)
                
            case 2:
                break
            
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
                   
                   option=int(input("Ingrese la opción: "))
                   match option:
                        case 1:
                            os.system("cls")
                            print("Alfabetos... ", Alphabets)
                            time.sleep(20)
                        case 0:
                            break    
            case 0:
                break    
                
if __name__ == "__main__":
    main()