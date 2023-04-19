import json

class TOMLtable:
    # Função de inicialização do nosso dicionario 
    def __init__ (self):
        self.data = {}
    
    # Função responsável por adicionar um elemento ao dicionario
    def add(self, key, value):
        self.data[key] = value

    # Função responsável por obter um determinado dicionario
    def get(self, key):
        return self.data.get(key, None)

    # Função de conversão de um dicionario para json
    def toJSON(self):
        return json.dumps(self.data, default=self.serialize_TOMLtable)

    # Funçãio auxiliar para realizar a conversão para JSON
    def serialize_TOMLtable(self, obj):
        if isinstance(obj, TOMLtable):
            return obj.data
        else:
            raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

    # Ciclo que percorre o resultado do nosso analisador sintático e 
    # faz diversas operações sobre os elemento presentes no mesmo
    def convert(self,obj):
        return

    # Função que dependendo do tipo de um elemento faz o devido cast para 
    # o elemento em questão
    def typecast(self,value):
        return

# Função de testes
def run():
    toml = TOMLtable()
    info = TOMLtable()
    info.add("street", "123 Main Street")
    info.add("city", "Anytown")
    info.add("state", "CA")
    toml.add("adress",info)
    print(toml.toJSON())

run()
