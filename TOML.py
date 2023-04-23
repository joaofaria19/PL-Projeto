import json

class TOMLtable:
    # Função de inicialização do nosso dicionario 
    def __init__ (self):
        self.data = {}

    def criar_tabela(self,names,value):
        obj = {}
        print(names)
        for nome in reversed(names):
            if obj: 
                obj = {nome: obj} 
            else: 
                obj = {nome: value}
        return obj




# Função de testes
def run():
    toml = TOMLtable()
    info = TOMLtable()
    info.add("street", "123 Main Street")
    info.add("city", "Anytown")
    info.add("state", 3)
    toml.add("adress",info)

    print(toml.toJSON())
#run()