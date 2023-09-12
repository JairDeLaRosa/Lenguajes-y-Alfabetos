import random  # languaje
import itertools  # language


class SetOperations:
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
            
            
            
              
            
            


class Alphabets(SetOperations):
   def star_lock(self, index, cant_word):
      list_result = []
      Alphabet = self.list[index]
      Alphabet_list = list(Alphabet)  # Convertir el conjunto en una lista
      i = 0
      while i < cant_word:
          word = ""
          for j in range(random.randint(2, 5)):
              word += str(random.choice(Alphabet_list))  # Usar la lista en lugar del conjunto
          if word not in list_result:
              list_result.append(word)
              i += 1
   
      return list_result


class Language(SetOperations):
    def create_language(alphabet, number):
        symbols1 = alphabet[0]
        symbols2 = alphabet[1]
        language = []

        for _ in range(number):
            symbol1 = random.choice(symbols1)
            symbol2 = random.choice(symbols2)
            word = f"{symbol1}{symbol2}"
            language.append(word)

        return language

    def cardinality_language(language):
        cont = len(language)
        return cont

    def concatenate_languages(language1, language2):
        concatenate_languages = language1
        # extend Used to concatenate iterables
        concatenate_languages = concatenate_languages.extend(language2)

        return concatenate_languages

    def inverse_language(languange):
        inverse_laguage = list(reversed(languange))

        return inverse_laguage

    def power_language(langauge, exponent):
        if exponent < 0:
            return None

        # itertools.product to generate all possible combinations of language strings to the specified power.
        combinations = itertools.product(langauge, exponent)

        for combination in combinations:
            result = "".join(combination)

        return result
