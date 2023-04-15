import ply.yacc as yacc
import analisador_lexico as lexer

tokens = lexer.tokens

start = 'Lista'

def p_lista(p):
    """
    Lista : LEFTSQUAREBRACKET RIGHTSQUAREBRACKET
        | LEFTSQUAREBRACKET Conteudo RIGHTSQUAREBRACKET
        | LEFTSQUAREBRACKET ConteudoVar RIGHTSQUAREBRACKET
    """
    if len(p) == 2:
        p[0] = []
    else:  
        p[0] = [p[2]]

def p_conteudo(p):
    """
    Conteudo : Elemento
            | Elemento Conteudo2
    """
    if len(p) == 2:
        p[0] = p[1]
    else: 
        p[0] = p[1] + p[2]

def p_conteudo2(p):
    """
    Conteudo2 : COMMA 
            | COMMA Conteudo
    """
    if len(p) == 2:
        p[0] = p[1]
    else: 
        p[0] = p[1] + p[2]

def p_conteudo_var(p):
    """
    ConteudoVar : Elemento2
            | Elemento2 DOT ConteudoVar
    """
    if len(p) == 2:
        p[0] = p[1]
    else: 
        p[0] = p[1] + p[2] + p[3]

def p_elemento2(p):
    """
    Elemento2 : VAR 
            | STRING
            | NUMBER
    """
    p[0] = str(p[1])


def p_elemento(p):
    """
    Elemento : NUMBER
            | STRING
            | MSTRING
            | DATE 
            | TIME
            | DATETIME
            | BOOLEAN
            | Lista
    """
    p[0] = str(p[1])


parser = yacc.yacc(debug=True, write_tables=True)

f = open('toml3.toml','r')
lines = f.readlines()

for line in lines:
    result = parser.parse(line)
    print(result)