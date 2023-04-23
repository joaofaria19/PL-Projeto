
import ply.yacc as yacc
import analisador_lexico as lexer

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
        table : LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET
            | LEFTSQUAREBRACKET LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET RIGHTSQUAREBRACKET
    """
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = [p[3]]

def p_name(p):
    """
        name : elementoVar
            | elementoVar name2
    """
    if len(p) == 2:
        p[0] = {'type': 'table', 'name': p[1]}
    else:
        p[0] = {'type': 'table', 'name': p[1], 'value': p[2]}

def p_assignment(p):
    """
        assignment : VAR EQUAL elemento
    """
    p[0] = {'type': 'assignment', 'name': p[1], 'value': p[3]}

def p_name2(p):
    """
        name2 : DOT elementoVar
            | DOT elementoVar name2
    """
    if len(p)==3:
        p[0] = {'type': 'table', 'name': p[2]}
    else:
        p[0] = {'type': 'table', 'name': p[2], 'value': p[3]}

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
        p[0] = {'type': 'list', 'value': []}
    else:  
        p[0] = {'type': 'list', 'value': p[2]} 

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
    p[0] = {'type': 'string', 'value': p[1][1:-1]}

def p_number(p):
    """
        number : NUMBER
    """
    p[0] = {'type': 'number', 'value': int(p[1])}

def p_boolean(p):
    """
        boolean : BOOLEAN
    """
    p[0] = {'type': 'boolean', 'value': bool(p[1])}

def p_date(p):
    """
        date : DATE
    """
    p[0] = {'type': 'date', 'value': p[1][1:-1]}

def p_time(p):
    """
        time : TIME
    """
    p[0] = {'type': 'time', 'value': p[1][1:-1]}

def p_datetime(p):
    """
        datetime : DATETIME
    """
    p[0] = {'type': 'datetime', 'value': p[1][1:-1]}



# Inicialização do parser
parser = yacc.yacc()

f = open('./TOML/toml4.toml','r')
lines = f.readlines()

result = ""
for line in lines:  
    result += str(parser.parse(line))

print(result)
