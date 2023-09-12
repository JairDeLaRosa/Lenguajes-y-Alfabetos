class Operations:
    def __init__(self):
        self.list = []

    def add_element(self, elemnt):
        self.list.append(elemnt)

    def get_element(self, element):
        return self.list[element]

    def set_list(self, lista):
        self.list = lista

    def get_list(self):
        return self.list

    def union(self, index1, index2):
        list_result = set(self.list[index1]) | set(self.list[index2])
        return list(list_result)

    def difference(self, index1, index2):
        list_result = []
        for index in self.list[index1]:
            if index not in self.list[index2]:
                list_result.append(index)
        return list_result

    def interception(self, index1, index2):
        list_result = []
        for index in self.list[index1]:
            if index in self.list[index2]:
                list_result.append(index)
        return list_result
    def mostrar(self):
        i = 0
        while i < len(self.list):  # Cambiar la condición a i < len(self.list)
            print(f"{i}: {self.list[i]}")
            i += 1
            
    

lista=[]
a1=[1, 2, 3, 4]
a2=[3, 4, 5]    
a3=[3,4, 6, 7]
lista.append(a1)
lista.append(a2)
lista.append(a3)
print(lista)
conjunto=Operations(lista)
print(conjunto.interceccion())