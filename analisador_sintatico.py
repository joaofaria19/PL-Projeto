import ply.yacc as yacc
import analisador_lexico as lexer
import toml as TOML

tokens = lexer.tokens

class Assignment:
    def __init__(self,content):
        self.content = content
    
class Table:
    def __init__(self,name,type):
        self.type = type
        self.name = name
        self.data = {}
        self.list = []


start = 'program'

def p_program(p):
    """
        program : statement
                | statement program
    """
    if isinstance(p[1],Assignment): 
        if p.parser.table_dict == False and  p.parser.table_list == False :
            p.parser.toml.add_element(p[1].content)
        
        elif p.parser.table_dict == True:
            p.parser.toml.add_element_table(p.parser.table.data,p[1].content)
            
            name = p.parser.table.name
            data = p.parser.table.data
            obj = p.parser.toml.new_assignment(name,data)
            p.parser.toml.add_element(obj)
        
        elif p.parser.table_list == True:
            p.parser.table.list.append(p[1].content)
            
            name = p.parser.table.name
            list = p.parser.table.list
            obj = p.parser.toml.new_assignment(name,list)
            p.parser.toml.add_element(obj)
        
    elif isinstance(p[1],Table):
        p.parser.table = p[1]
        
        if p[1].type == 'table_dict':
            p.parser.table_list = False
            p.parser.table_dict = True
        elif p[1].type == 'table_list':
            p.parser.table_dict = False
            p.parser.table_list = True
    else : 
        pass

    p[0] = parser.toml.data



def p_statement(p):
    """
        statement : table
                | assignment
                | comment
                | NEWLINE
    """
    p[0] = p[1]

def p_comment(p):
    """
        comment : COMMENT NEWLINE
    """
    p[0] = {'type': 'comment', 'value':p[1]}

def p_table(p):
    """
        table : header1
            | header2
    """
    p[0] = p[1]

def p_header1(p):
    """
        header1 : LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET NEWLINE
    """
    p[0] = Table(p[2],'table_dict')
    
def p_header2(p):
    """
        header2 : LEFTSQUAREBRACKET LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET RIGHTSQUAREBRACKET NEWLINE
    """
    p[0] = Table(p[3],'table_list')

def p_assignment(p):
    """
        assignment : name EQUAL elemento NEWLINE
    """
    content = p.parser.toml.new_assignment(p[1], p[3])
    p[0] = Assignment(content)

def p_assignment_object(p):
    """
        assignment_object : name EQUAL elemento
    """
    p[0] = p.parser.toml.new_assignment(p[1],p[3])

def p_name(p):
    """
        name : elementoVar
            | elementoVar name2
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]

def p_name2(p):
    """
        name2 : DOT elementoVar
            | DOT elementoVar name2
    """
    if len(p)==3:
        p[0] = [p[2]]
    else:
        p[0] = [p[2]] + p[3]

def p_elemento_var(p):
    """
        elementoVar : VAR
                    | string
                    | int
    """
    p[0] = p[1]

def p_lista(p):
    """
        lista : LEFTSQUAREBRACKET RIGHTSQUAREBRACKET
            | LEFTSQUAREBRACKET ContList RIGHTSQUAREBRACKET
    """
    if len(p) == 2:
        p[0] = []
    else:  
        p[0] = p[2]

def p_conteudo_lista(p):
    """
        ContList : elemento
                | elemento ContList2
    """
    if len(p) == 2:
        p[0] = [p[1]] 
    else: 
        p[0] = [p[1]] + p[2]

def p_conteudo_lista2(p):
    """
    ContList2 : COMMA 
            | COMMA ContList
    """
    if len(p) == 2:
        p[0] = p[1]
    else: 
        p[0] = p[2]

def p_object(p):
    """
        object : LEFTBRACKET RIGHTBRACKET
                | LEFTBRACKET ContObject RIGHTBRACKET
    """
    if len(p) == 2:
        p[0] = {}
    else:  
        p[0] = p[2] 

def p_conteudo_object(p):
    """
        ContObject : assignment_object
                | assignment_object COMMA ContObject
    """
    if len(p) == 2:
        p[0] = p[1]
    else: 
        p[0] = p.parser.toml.add_element_aux(p[1],p[3])

def p_elemento(p):
    """
        elemento : 
             | int
             | float
             | inf
             | nan
             | hexadecimal
             | binary
             | octal
             | string
             | boolean
             | date
             | time
             | datetime
             | offset_datetime
             | lista
             | object
    """
    p[0] = p[1]

def p_string(p):
    """
        string : STRING
    """
    p[0] =  p[1][1:-1]

def p_number(p):
    """
        int : INT
    """
    p[0] = int(p[1])

def p_float(p):
    """
        float : FLOAT
    """
    p[0] = float(p[1])

def p_inf(p):
    """
        inf : INF
    """
    p[0] = p[1][1:-1]

def p_nan(p):
    """
        nan : NAN
    """
    p[0] = p[1][1:-1]

def p_hexadecimal(p):
    """
        hexadecimal : HEXADECIMAL
    """
    p[0] = p[1][1:-1]

def p_binary(p):
    """
        binary : BINARY
    """
    p[0] = p[1][1:-1]

def p_octal(p):
    """
        octal : OCTAL
    """
    p[0] = p[1][1:-1]

def p_boolean(p):
    """
        boolean : BOOLEAN
    """
    p[0] = bool(p[1])

def p_date(p):
    """
        date : DATE
    """
    p[0] = p[1][1:-1]

def p_time(p):
    """
        time : TIME
    """
    p[0] = p[1][1:-1]

def p_datetime(p):
    """
        datetime : DATETIME
    """
    p[0] = p[1][1:-1]

def p_offset_datetime(p):
    """
        offset_datetime : OFFSETDATETIME
    """
    p[0] = p[1][1:-1]

def p_error(p):
    if p:
        print(f"Sintax error on line {p.lineno}, column {p.lexpos + 1}: "
              f"unexpected token '{p.value}'")
    else:
        print("Syntax error: unexpected end of file")

# Inicialização do parser
parser = yacc.yacc()

parser.toml = TOML.TOML()
parser.table = None
parser.table_dict = False
parser.table_list = False

"""
f = open('./TOML/toml5.toml','r')
lines = f.readlines()
result = ""
for line in lines:  
    result += str(parser.parse(line))

print(result)
#print(parser.toml.data)
print(parser.toml.toJSON())
"""
