import re
import sys

# Token types
TOKEN_TYPES = {
    'TYPE':r'\b(int|float|str|bool)\b',
    'KEYWORD': r'\b(program|const|int|float|str|bool|print|input|if|else|while|break)\b',
    'IDENTIFIER': r'[a-zA-Z_][a-zA-Z_0-9]*',
    'NUMBER': r'\b\d+(\.\d+)?\b',
    'STRING': r'".*?"',
    'OPERATOR': r'[+\-*/=!><]=?|!',
    'DELIMITER': r'[;,{()}]',
    'WHITESPACE': r'[ \t]+',
    'NEWLINE': r'\n',
    'COMMENT': r'//.*'
}

# Token class
class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f'({self.type}, {repr(self.value)}, {self.line}, {self.column})'

# Lexer class
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
        # Check for end of code
        if self.position >= len(self.code):
            return None

        # Try to match each token type
        for type, pattern in TOKEN_TYPES.items():
            regex = re.compile(pattern)
            match = regex.match(self.code, self.position)
            if match:
                value = match.group(0)
                token = Token(type, value, self.line, self.column)
                self._update_position(value)
                if type == 'WHITESPACE' or type == 'COMMENT':
                    return self._next_token()  # Skip whitespace and comments
                return token

        # If no token is matched, raise an error
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
        print(token)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <filename>")
    else:
        main(sys.argv[1])