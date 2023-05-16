from analisador_lexico import lexer

f = open('./TOML/toml.toml', 'r')
lines = f.readlines()

for line in lines:
    lexer.input(line)
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)
