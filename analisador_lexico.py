import ply.lex as lex

tokens = ('COMMENT','COMMA','DOT','VAR',
          'LEFTBRACKET','RIGHTBRACKET','LEFTSQUAREBRACKET','RIGHTSQUAREBRACKET',
          'EQUAL','NUMBER','STRING','MSTRING', 'BOOLEAN',
          'DATE','TIME','DATETIME')

t_COMMENT = r'\#.*'
t_COMMA = r'\,'
t_DOT = r'\.' 
t_LEFTSQUAREBRACKET = r'\['
t_RIGHTSQUAREBRACKET = r'\]'
t_LEFTBRACKET = r'\{'
t_RIGHTBRACKET = r'\}'
t_EQUAL = r'\='
t_VAR = r'(\w+|\-)+'
t_BOOLEAN = r'(false|true)'
t_STRING = r'(\"[^"]+\")'
t_MSTRING = r'\"\"\"(.*|\n)+\"\"\"' 
t_DATE = r'(\d{4}\-\d{2}\-\d{2})'
t_TIME = r'(\d{2}:\d{2}:\d{2}(\.\d{6})?)'
t_DATETIME = r'(\d{4}\-\d{2}\-\d{2}T\d{2}\:\d{2}\:\d{2}(\.\d{6})?)'
t_NUMBER = r'(\+|\-)?(\d+(\.\d+)*((e|E)+(\+|\-)?\d+)*|inf|nan)+' # necessário corrigir o number para floats e expoentes


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

f = open('toml3.toml','r')
lines = f.readlines()

for line in lines:    
    lexer.input(line)
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)