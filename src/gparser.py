import sys
import toml as toml
from analisador_sintatico import parser

parser.toml = toml.TOML()
parser.table_token = False
parser.stack = []
parser.final = []
parser.size = 1

lines=[]
for line in sys.stdin:
    lines.append(line)

result=""
for line in lines:
    result+=line

parser.parse(result)

print(parser.toml.toJSON())

with open('../out/result.json','w') as file:
    file.write(parser.toml.toJSON())