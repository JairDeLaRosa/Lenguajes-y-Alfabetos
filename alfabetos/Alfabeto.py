class Alfabeto:
    def __init__(self, a1,a2):
        self.a1=a1
        self.a2=a2
        
    def getA1(self):
        return self.a1
    
    def getA2(self):
        return self.a2
    
    def union(self):
        return self.a1 | self.a2
    
    def resta(self):
        return self.a1 - self.a2
    
    def interceccion(self):
        return self.a1 & self.a2    
    
