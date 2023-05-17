import sys
from analisador_lexico import lexer


lines=[]
for line in sys.stdin:
    lines.append(line)


#f = open('./TOML/toml2.toml', 'r')
#lines = f.readlines()

for line in lines:
    lexer.input(line)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
