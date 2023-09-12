class Operations:
    def __init__(self, lista):
        self.list=list(lista)
        
    def getList(self):
        return self.list
    
    def union(self):
        union=set()
        for e in self.list:
            e=set(e)
            union=union | e
        return list(union)
    
    def resta(self):
        resta=set()
        for e in self.list:
            resta=set(e)-resta
        return list(resta)
    
    def interceccion(self):
        interception=set(self.list[0])
        for e in self.list:
            interception=interception & set(e)
        
        return list(interception)    
    

# lista=[]
# a1=[1, 2, 3, 4]
# a2=[3, 4, 5]    
# a3=[3,4, 6, 7]
# lista.append(a1)
# lista.append(a2)
# lista.append(a3)
# print(lista)
# conjunto=Operations(lista)
# print(conjunto.interceccion())

