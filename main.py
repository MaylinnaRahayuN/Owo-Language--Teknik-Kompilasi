import lexer_owo
import parser_owo
import interpreter_owo
from sys import *

#MASUKAN LANGSUNG DENGAN TERMINAL PADA PROGRAM
if __name__ == '__main__':
    lexer = lexer_owo.leksikal()
    parser = parser_owo.sintaksis()
    env = {}
    while True:
        try:
            text = input('owo > ')
        except EOFError:
            break
        if text:
            tree = parser.parse(lexer.tokenize(text))
            interpreter_owo.BasicExecute(tree, env)