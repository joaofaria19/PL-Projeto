
import ply.yacc as yacc
import analisador_lexico as lexer
import TOML as TOML

tokens = lexer.tokens

start = 'program'

def p_program(p):
    """
        program : table
                | assignment
    """
    p[0] = p[1]

def p_table(p):
    """
        table : LEFTSQUAREBRACKET LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET RIGHTSQUAREBRACKET conteudo
            | LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET conteudo
            | LEFTSQUAREBRACKET LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET RIGHTSQUAREBRACKET
            | LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET
    """
    if len(p) == 4:
        obj = p.parser.toml.criar_tabela(p[2],{})
        p[0] = obj
    elif len(p)==6:
        obj = p.parser.toml.criar_tabela(p[2],[])
        p[0] = obj
    elif len(p)==5:
        obj = p.parser.toml.criar_tabela(p[2],p[4])
        p[0] = obj
    else:
        obj = p.parser.toml.criar_tabela(p[2],[p[4]])
        p[0] = obj

def p_assignment(p):
    """
        assignment : name  EQUAL elemento
    """
    obj = {}
    obj= p.parser.toml.criar_tabela(p[1],p[3])
    p[0] = obj


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
        p[0] =  [p[2]]
    else:
        p[0] = [p[2]] + p[3]

def p_conteudo(p):
    """
        conteudo : assignment
                | assignment conteudo
    """
    obj = {}
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] 


def p_elemento_var(p):
    """
        elementoVar : VAR
                    | STRING
                    | NUMBER
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
        p[0] = {'type': 'object', 'value': {}}
    else:  
        p[0] = {'type': 'object', 'value': p[2]} 

def p_conteudo_object(p):
    """
        ContObject : assignment
                | assignment ContObject2
    """
    if len(p) == 2:
        p[0] = p[1]
    else: 
        p[0] = [p[1]] + [p[2]]

def p_conteudo_object2(p):
    """
    ContObject2 : COMMA 
            | COMMA ContObject
    """
    if len(p) == 2:
        p[0] = p[1]
    else: 
        p[0] = p[2]

def p_elemento(p):
    """
        elemento : 
             | number
             | string
             | boolean
             | date
             | time
             | datetime
             | lista
             | object
    """
    p[0] = p[1]

def p_string(p):
    """
        string : STRING
    """
    p[0] = p[1][1:-1]

def p_number(p):
    """
        number : NUMBER
    """
    p[0] = int(p[1])

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



# Inicialização do parser
parser = yacc.yacc()

parser.toml = TOML.TOMLtable()

f = open('./TOML/toml4.toml','r')
lines = f.readlines()

result = ""
for line in lines:  
    result += str(parser.parse(line))

print(result)
