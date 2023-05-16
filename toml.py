import json


"""
    Classe Assignment para o tipo assignment detetado na gramática
"""
class Assignment:
    def __init__(self,content):
        self.content = content


"""
    Classe Table  para o tipo assignment detetado na gramática
""" 
class Table:
    def __init__(self,name,type):
        self.type = type
        self.name = name
        self.data = {}

"""
    Classe TOML como auxilio na gramática
"""
class TOML: 
    """
        Função de inicialização da classe, com a criação do dicionário global
    """
    def __init__(self):
        self.data = {}

    """
         Função responsável por adicionar um dicionário ao dicionário adicional
         A Função verifica se a key do novo dicionário é também ela um dicionário e 
        se a mesma key do dicionário global é também esta um dicionário.
         Caso sejam, é chamada a função add_element_aux, para recursivamente adicionar 
        os vários dicionários aninhados. Caso não sejam o elemnto no dicionário global
        é reescrito com o novo valor.
    """
    def add_element(self,new_dict):
        for key, value in new_dict.items():
            if key not in self.data:
                self.data[key] = value
            else:
                if isinstance(value, dict) and isinstance(self.data[key], dict):
                    self.data[key] = self.add_element_aux(self.data[key], value)
                elif isinstance(self.data[key], list) and isinstance(value,list):
                    self.data[key].append(value[0])
                elif isinstance(self.data[key], list):
                    self.add_element_aux(self.data[key][-1], value)
                else:
                    self.data[key] = value
        return self.data

    """
         Realiza a mesma estratégia que a função anterior, só que em vez de adicionar 
        ao dicionário global, a adição é feita ao dicionário passado como argumento(atual_dict).
         Desta forma podemos adicionar dicionários ao dicionário de uma tabela
    """
    def add_element_table(self, atual_dict,new_dict):
        for key, value in new_dict.items():
            if key not in atual_dict:
                atual_dict[key] = value
            else:
                if isinstance(value, dict) and isinstance(atual_dict[key], dict):
                    atual_dict[key] = self.add_element_aux(atual_dict[key], value)
                else:
                    atual_dict[key] = value
        return atual_dict

    """
        Função chamada recursivamente para realizar a devida adição entre dicionários aninhados.
    """
    def add_element_aux(self, dict1, dict2):
        for key, value in dict2.items():
            if key not in dict1:
                dict1[key] = value
            else:
                if isinstance(value, dict) and isinstance(dict1[key], dict):
                    dict1[key] = self.add_element_aux(dict1[key], value)
                elif isinstance(value, list):
                    if len(value) > 0:
                        dict1[key].append(value[0])
                    else:
                        dict1[key].append([])     
                else:
                    dict1[key] = value
        return dict1
    
    """
        Função que recebe como argumento uma lista de nomes e um valor a atribuir ao último nome da lista.
        Desta forma conseguimos objeter objetos aninhados.
        Retorna o objeto resultante
    """
    def new_assignment(self,names,value):
        obj = {}
        for nome in reversed(names):
            if obj:
                obj = {nome: obj} 
            else: 
                obj = {nome: value}
        return obj
    
    """
        Função para transformar o dicionário em python num objeto JSON
    """
    def toJSON(self):
        return json.dumps(self.data, indent=4, ensure_ascii=False)