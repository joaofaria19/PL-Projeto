import ply.lex as lex

tokens = ('COMMENT', 'COMMA', 'DOT', 'VAR',
          'LEFTBRACKET', 'RIGHTBRACKET', 'LEFTSQUAREBRACKET', 'RIGHTSQUAREBRACKET',
          'EQUAL', 'DATE', 'INT', 'FLOAT', 'INF', 'NAN', 'STRING', 'MSTRING', 'BOOLEAN',
          'TIME', 'DATETIME', 'OFFSET', 'OFFSETDATETIME', 'HEXADECIMAL', 'BINARY', 'OCTAL',
          'NEWLINE')


t_COMMA = r'\,'
t_DOT = r'\.'
t_LEFTSQUAREBRACKET = r'\['
t_RIGHTSQUAREBRACKET = r'\]'
t_LEFTBRACKET = r'\{'
t_RIGHTBRACKET = r'\}'
t_EQUAL = r'\='
t_BOOLEAN = r'(false|true)'
t_STRING = r'(\"[^"]+\")'
t_MSTRING = r'\"\"\"[^\"]*\"\"\"'
t_INT = r'[\+\-]?(0|[1-9](\_?[0-9])*)'
t_FLOAT = r'[\+\-]?(0|[1-9](\_?[0-9])*)(\.[0-9](\_?[0-9])*([eE][\+\-]?[0-9](\_?[0-9])*)?|[eE][\+\-]?[0-9](\_?[0-9])*)'
t_INF = r'[\+\-]?inf'
t_NAN = r'[\+\-]?nan'
t_HEXADECIMAL = r'0x[0-9A-Fa-f]([0-9A-Fa-f]|_[0-9A-Fa-f])*'
t_BINARY = r'0b[01]([01]|_[01])*'
t_OCTAL = '0o[0-7]([0-7]|_[0-9])*'
t_VAR = r'(\w+|\-)+'

t_COMMENT = r'\#\s*.*'
t_ignore = ' \t'


#Definições em funções para respeitar prioridades
def t_TIME(t):
    r'\d{2}:\d{2}:\d{2}(\.\d{6})?'
    return t

def t_OFFSETDATETIME  (t):
    r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{6})? [+-]\d{2}:\d{2}'
    return t

def t_DATETIME (t):
    r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d{6})?'
    return t

def t_OFFSET (t):
    r'[+-]\d{2}:\d{2}'
    return t

def t_DATE(t):
    r'\d{4}-\d{2}-\d{2}'
    return t

def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += 1
    return t

def t_error(t):
    print(f"Illegal character {t.value[0]} on line {t.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()

