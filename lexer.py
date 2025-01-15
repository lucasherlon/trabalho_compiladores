import ply.lex as lex
import sys

# Regras para palavras reservadas
reserved = {
    'Program': 'PROGRAM',
    'const': 'CONST',
    'int': 'INT',
    'float': 'FLOAT',
    'str': 'STR',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT',
    'input': 'INPUT',
    'true': 'TRUE',
    'false': 'FALSE'
}

# Lista de tokens
tokens = [
    'IDENTIFIER', 'INTEGER_LITERAL', 'FLOAT_LITERAL', 'STRING_LITERAL',
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EQUAL', 'NOTEQUAL',
    'GREATER_EQUAL', 'LESS_EQUAL', 'GREATER', 'LESS', 'NOT',
    'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'SEMICOLON', 'COMMA', 'ASSIGN'
] + list(reserved.values())


# Regras de expressões regulares para tokens simples
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_COMMA = r','
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_EQUAL = r'=='
t_NOTEQUAL = r'!='
t_GREATER_EQUAL = r'>='
t_LESS_EQUAL = r'<='
t_GREATER = r'>'
t_LESS = r'<'
t_NOT = r'!'

# Regras para tokens mais complexos
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Verifica se é uma palavra reservada
    return t

def t_INTEGER_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT_LITERAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING_LITERAL(t):
    r'"([^\\"]|\\.)*"'
    t.value = t.value[1:-1]  # Remove aspas
    return t

# Ignorar espaços e tabulações
t_ignore = ' \t'

# Contador de linhas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

# Construção do lexer
lexer = lex.lex()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python lexer.py <filename>")
    else:
        with open(sys.argv[1], 'r') as file:
            code = file.read()
        lexer.input(code)
        for tok in lexer:
            print(tok)