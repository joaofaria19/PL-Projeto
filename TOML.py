import json

class TOMLtable:
    # Função de inicialização do nosso dicionario 
    def __init__ (self):
        self.data = {}

    def add_element(self, object):
        obj = {}
        list = []
        open_table = False
        if object['type'] == 'table_object':

            open_table = True
        elif object['type'] == 'table_list':
            open_table = True
        elif object['type'] == 'assignment':
            self.data.update(object['value'])
        elif object['type'] == 'empty':
            open_table = False
        else:
            pass
        
    def print(self):
        print(self.data)

    def json(self):
        return json.dumps(self.data,indent=2)

    def join_dicts(self,dict1,dict2):
        for key,value in dict2.items():
            if key in dict1:
                dict1[key] += value
            else:
                dict1[key] = value
        return dict1

    def new_assignment(self,names,value):
        obj = {}
        for nome in reversed(names):
            if obj:
                obj = {nome: obj} 
            else: 
                obj = {nome: value}
        return obj
    
# Função de testes
def run():
    toml = TOMLtable()
    toml.add_element({'type': 'assignment','value': toml.new_assignment(['name','proprio'],'John Doe')})
    toml.add_element({'type': 'assignment','value': toml.new_assignment(['mylist'],[0,True,'falso'])})
    print(toml.json())

run()