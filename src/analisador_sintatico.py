import ply.yacc as yacc
import analisador_lexico as lexer
from toml import Assignment
from toml import Table

tokens = lexer.tokens

start = 'program'

def p_program(p):
    """
    program : statements
    """
    for assg in p.parser.stack:
        p.parser.final.insert(0,assg)
    for obj in p.parser.final:
        p.parser.toml.add_element(obj)
    
    p[0] = p[1]

def p_statements(p):
    """
        statements : statement
                | statement statements
    """
    
    if isinstance(p[1],Assignment): 
        p.parser.stack.append(p[1].content)
        p.parser.table_token = False
    elif isinstance(p[1],Table):
        if p[1].type == 'table_dict':
            name = p[1].name
            if p.parser.table_token:
                obj = p.parser.toml.new_assignment(name,{})
                p.parser.final.insert(0,obj)
            else:
                for assg in reversed(p.parser.stack):
                    p.parser.toml.add_element_table(p[1].data,assg)
                data = p[1].data
                obj = p.parser.toml.new_assignment(name,data)
                p.parser.final.insert(0,obj)
        elif p[1].type == 'table_list':
            name = p[1].name
            if p.parser.table_token:
                obj = p.parser.toml.new_assignment(name,[])
                p.parser.final.insert(0,obj)
            else:
                for assg in reversed(p.parser.stack):
                    obj = p.parser.toml.new_assignment(name,[assg])
                    p.parser.final.insert(0,obj)
        p.parser.stack = []
        p.parser.table_token = True
    else:
        pass        
    p[0] = parser.toml.data


def p_statement(p):
    """
        statement : table
                | assignment
                | comment
                | newline
    """
    p.parser.size +=1
    p[0] = p[1]
    
def p_newline(p):
    """
        newline : NEWLINE
    """
    p[0] = {'type': 'newline', 'value':p[1]}

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
        header1 : LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET 
            | LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET NEWLINE
            | LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET COMMENT
    """
    if len(p) == 4:
        if p.lexer.lineno == p.parser.size:
            p[0] = Table(p[2],'table_dict')
        else:
            raise Exception(f'Unexpected character, table expected only newlines or comments till end of line at row {p.lexer.lineno}')
    
    else:
        p[0] = Table(p[2],'table_dict')
    
def p_header2(p):
    """
        header2 : LEFTSQUAREBRACKET LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET RIGHTSQUAREBRACKET 
            | LEFTSQUAREBRACKET LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET RIGHTSQUAREBRACKET NEWLINE
            | LEFTSQUAREBRACKET LEFTSQUAREBRACKET name RIGHTSQUAREBRACKET RIGHTSQUAREBRACKET COMMENT
    
    """
    if len(p) == 6:
        if p.lexer.lineno == p.parser.size:
            p[0] = Table(p[3],'table_list')
        else:
            raise Exception(f'Unexpected character, table expected only newlines or comments till end of line at row {p.lexer.lineno}')
    
    else:
        p[0] = Table(p[3],'table_list')

def p_assignment(p):
    """
        assignment : name EQUAL elemento 
                | name EQUAL elemento NEWLINE
    """
    if len(p) == 4:
        if p.parser.size == p.lexer.lineno:
            content = p.parser.toml.new_assignment(p[1], p[3])
            p[0] = Assignment(content)
        else:
            raise Exception(f'Unexpected character, assignment expected only newlines or comments till end of line')
    else:
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
            | LEFTSQUAREBRACKET conteudo_lista RIGHTSQUAREBRACKET
            | LEFTSQUAREBRACKET conteudo_lista COMMA RIGHTSQUAREBRACKET     
    """
    if len(p) == 2:
        p[0] = []
    else:  
        p[0] = p[2]

def p_conteudo_lista(p):
    """
        conteudo_lista : elemento
                | elemento COMMA conteudo_lista
    """
    if len(p) == 2:
        p[0] = [p[1]] 
    else: 
        p[0] = [p[1]] + p[3]

def p_object(p):
    """
        object : LEFTBRACKET RIGHTBRACKET
                | LEFTBRACKET conteudo_object RIGHTBRACKET
    """
    if len(p) == 2:
        p[0] = {}
    else:  
        p[0] = p[2]

def p_conteudo_object(p):
    """
        conteudo_object : assignment_object
                | assignment_object COMMA conteudo_object
    """
    if len(p) == 2:
        p[0] = p[1]
    else: 
        p[0] = p.parser.toml.add_element_aux(p[1],p[3])

def p_elemento(p):
    """
        elemento : int
             | float
             | inf
             | nan
             | hexadecimal
             | binary
             | octal
             | string
             | mstring
             | lstring
             | mlstring
             | boolean
             | date
             | time
             | datetime
             | offset_datetime
             | lista
             | object
    """
    p[0] = p[1]

def p_mstring(p):
    """
        mstring : MSTRING
    """
    p[0] =  p[1][3:-3]

def p_mlstring(p):
    """
        mlstring : MLSTRING
    """
    p[0] =  p[1][3:-3]

def p_string(p):
    """
        string : STRING
    """
    p[0] =  p[1][1:-1]

def p_lstring(p):
    """
        lstring : LITERALSTRING
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


