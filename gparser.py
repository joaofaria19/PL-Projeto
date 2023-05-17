import toml as toml
from analisador_sintatico import parser

parser.toml = toml.TOML()
parser.table_token = False
parser.table = None
parser.stack = []
parser.final = []

f = open('./TOML/toml2.toml','r')
lines = f.readlines()

parser.length = len(lines)
result = ""
for line in lines:  
    result += line

parser.parse(result)

print(parser.toml.toJSON())
