import lexer_owo
import parser_owo
import interpreter_owo

from sys import *

# EXECUTE FROM FILE BAHASAKU.suns
lexer = lexer_owo.leksikal()
parser = parser_owo.sintaksis()
env = {}

file = open(argv[1])
text = file.readlines()
for line in text:
    tree = parser.parse(lexer.tokenize(line))
    interpreter_owo.BasicExecute(tree, env)