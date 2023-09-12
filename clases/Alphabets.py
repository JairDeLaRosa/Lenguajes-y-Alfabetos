import random
from .Operations import Operations
    
class Alphabets(Operations):
    def star_lock(self, index, cant_word):
      list_result = []
      Alphabet = self.list[index]
      Alphabet_list = list(Alphabet)  # Convertir el conjunto en una lista
      i = 0
      while i < cant_word:
          word = ""
          for j in range(random.randint(1, 5)):
              word += str(random.choice(Alphabet_list))  # Usar la lista en lugar del conjunto
          if word not in list_result:
              list_result.append(word)
              i += 1
   
      return list_result