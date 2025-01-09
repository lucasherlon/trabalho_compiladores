import re
import sys


TOKEN_TYPES = {
    'PROGRAM':r'\b(Program)\b',
    'TYPE':r'\b(int|float|str|bool)\b',
    'CONDICAO': r'\b(if|else|while)\b',
    'INPUT': r'\b(input)\b',
    'OUTPUT': r'\b(print)\b',
    'KEYWORD': r'\b(const|break)\b',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z_0-9]*',
    'NUMBER': r'\b\d+(\.\d+)?\b',
    'STRING': r'".*?"',
    'OP_SOMA': r'[+]=?|!',
    'OP_SUBT': r'[\-]=?|!',
    'OP_MULT': r'[*]=?|!',
    'OP_IGUAL': r'[==]=?',
    'OP_DIFERENTE': r'[!]=?',
    'OP_MAIOR': r'[>]=?',
    'OP_MENOR': r'[<]=?',
    'OP_MAIOR_IGUAL': r'[>=]=?',
    'OP_MENOR_IGUAL': r'[<=]=?',
    'DELIMITER': r'[;,{()}]',
    'WHITESPACE': r'[ \t]+',
    'NEWLINE': r'\n',
    'COMMENT': r'//.*'
}

operador = ('INPUT','OUTPUT','CONDICAO','IDENTIFIER','OP_SOMA', 'OP_SUBT', 'OP_MULT', 'OP_DIV', 'OP_IGUAL', 'OP_DIFERENTE', 'OP_MAIOR', 'OP_MENOR', 'OP_MAIOR_IGUAL', 'OP_MENOR_IGUAL','PROGRAM')


class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def token(self):
        return ( repr(self.value),self.type)


class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.line = 1
        self.column = 1

    def tokenize(self):
        tokens = []
        while self.position < len(self.code):
            token = self._next_token()
            if token:
                tokens.append(token)
        return tokens

    def _next_token(self):
        if self.position >= len(self.code):
            return None

        for type, pattern in TOKEN_TYPES.items():
            regex = re.compile(pattern)
            match = regex.match(self.code, self.position)
            if match:
                value = match.group(0)
                token = Token(type, value, self.line, self.column)
                self._update_position(value)
                if type == 'WHITESPACE' or type == 'COMMENT':
                    return self._next_token()
                return token.token()

        raise SyntaxError(f'Unexpected token at line {self.line}, column {self.column}')

    def _update_position(self, value):
        self.position += len(value)
        if '\n' in value:
            self.line += value.count('\n')
            self.column = 1
        else:
            self.column += len(value)

def main(filename):
    with open(filename, 'r') as file:
        code = file.read()
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    for token in tokens:
        if token[1] in operador:
            print(f"<{token[0]}, {token[1]}>")
        else:
            print(f"<{token[0]}>")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <filename>")
    else:
        main(sys.argv[1])