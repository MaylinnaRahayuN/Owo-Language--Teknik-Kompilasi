import sys
from sly import Lexer

class leksikal(Lexer):
    tokens = {PRINT, NUMBER, TO, ARROW, THEN, NAME, STRING, IF, ELSE, FOR, FUN, EQEQ, }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';', '^'}

    PRINT = r'dudohno'
    IF = r'yen'
    ELSE = r'liyane'
    FOR = r'kanggo'
    FUN = r'gunane'
    STRING = r'\".*?\"'
    THEN = r'dadine'
    EQEQ = r'=='
    ARROW = r'->'
    TO = r'marang'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    
    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self, t):
        self.lineno = t.value.count('\n')
    
    def error(self, t):
        print(f"hurufe ora cetho '{t.value[0]}'")
        sys.exit()

if __name__ == '__main__':
    lexer = leksikal()
    env = {}
    while True:
        try:
            text = input('owo > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
