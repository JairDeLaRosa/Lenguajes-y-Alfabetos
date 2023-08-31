from alfabetos.Alfabeto import Alfabeto

alfabeto_1=str("""{dmd vs, 4q 52 6}""")
alfabeto_2=str("""{dmdvs, dsa * ? 6 5 30}""")

def procesar_alfabeto(alfabeto):
    alfabeto=alfabeto[1:len(alfabeto)-1]
    alfabeto=f"{alfabeto} "
    elemento_agregar=""
    alfabeto_procesado=set()
    for indice in range(len(alfabeto)):
        if alfabeto[indice] != " ":
            elemento_agregar=f"{elemento_agregar}{alfabeto[indice]}"
        else:
            alfabeto_procesado.add(elemento_agregar)
            elemento_agregar=""
            
    return alfabeto_procesado

print(procesar_alfabeto(alfabeto_1))  
print(procesar_alfabeto(alfabeto_2))       

a1=procesar_alfabeto(alfabeto_1)
a2=procesar_alfabeto(alfabeto_2)


alf=Alfabeto(a1,a2)
print(alf.resta())


