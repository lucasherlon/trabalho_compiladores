import re
import sys


TOKEN_TYPES = {
    'PROGRAM':r'\b(Program)\b',
    'TYPE':r'\b(int|float|str|bool)\b',
    'CONDITION': r'\b(if|else|while)\b',
    'INPUT': r'\b(input)\b',
    'OUTPUT': r'\b(print)\b',
    'CONST': r'\b(const)\b',
    'BREAK': r'\b(break)\b',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z_0-9]*',
    'NUMBER': r'\b\d+(\.\d+)?\b',
    'STRING': r'".*?"',
    'OP_SOMA': r'[+]=?|!',
    'OP_SUBT': r'[\-]=?|!',
    'OP_MULT': r'[*]=?|!',
    'OP_EQUAL': r'[==]=?',
    'OP_DIFF': r'[!]=?',
    'OP_BIGGER': r'[>]=?',
    'OP_MINOR': r'[<]=?',
    'OP_BIGGER_EQUAL': r'[>=]=?',
    'OP_MINOR_EQUAL': r'[<=]=?',
    'DELIMITER': r'[;,{()}]',
    'WHITESPACE': r'[ \t]+',
    'NEWLINE': r'\n',
    'COMMENT': r'//.*'
}

non_operador = ('DELIMITER','NEWLINE','STRING')

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
        if token[1] not in non_operador:
            print(f"<{token[0]}, {token[1]}>")
        else:
            print(f"<{token[0]}>")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <filename>")
    else:
        main(sys.argv[1])