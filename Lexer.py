import ply.lex as lex

tokens = (
    'PROGRAM', 'TYPE', 'CONDITIONAL', 'LOOP', 'INPUT', 'OUTPUT', 'KEYWORD',
    'IDENTIFIER', 'NUMBER_INT', 'NUMBER_FLOAT', 'STRING',
    'OP_SOMA', 'OP_SUBT', 'OP_MULT', 'OP_DIV', 'OP_IGUAL', 'OP_ATRIB',
    'OP_DIFERENTE', 'OP_MAIOR', 'OP_MENOR', 'OP_MAIOR_IGUAL', 'OP_MENOR_IGUAL',
    'PAREN_ESQ', 'PAREN_DIR', 'CHAVE_ESQ', 'CHAVE_DIR',
    'COLCH_ESQ', 'COLCH_DIR', 'PONTO_VIRGULA', 'VIRGULA', 'PONTO'
)

# Regras simples baseadas em expressões regulares
t_PROGRAM = r'\bProgram\b'
t_TYPE = r'\b(int|float|str|bool)\b'
t_CONDITIONAL = r'\b(if|else)\b'
t_LOOP = r'\b(while)\b'
t_INPUT = r'\b(input)\b'
t_OUTPUT = r'\b(print)\b'
t_KEYWORD = r'\b(const|break)\b'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z_0-9]*'
t_NUMBER_INT = r'\b\d+\b'
t_NUMBER_FLOAT = r'\b\d+\.\d+\b'
t_STRING = r'"[^"]*"'
t_OP_SOMA = r'\+'
t_OP_SUBT = r'-'
t_OP_MULT = r'\*'
t_OP_DIV = r'/'
t_OP_IGUAL = r'=='
t_OP_ATRIB = r'='
t_OP_DIFERENTE = r'!='
t_OP_MAIOR = r'>'
t_OP_MENOR = r'<'
t_OP_MAIOR_IGUAL = r'>='
t_OP_MENOR_IGUAL = r'<='
t_PAREN_ESQ = r'\('
t_PAREN_DIR = r'\)'
t_CHAVE_ESQ = r'\{'
t_CHAVE_DIR = r'\}'
t_COLCH_ESQ = r'\['
t_COLCH_DIR = r'\]'
t_PONTO_VIRGULA = r';'
t_VIRGULA = r','
t_PONTO = r'\.'

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'


def t_COMMENT(t):
    r'//.*'
    pass


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f"Caractere inválido '{t.value[0]}' na linha {t.lineno}")
    t.lexer.skip(1)

lexer = lex.lex()

def main(filename):
    with open(filename, 'r') as file:
        code = file.read()

    lexer.input(code)
    for token in lexer:
        print(f"<{token.type}, {token.value}>")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: python lexer.py <filename>")
    else:
        main(sys.argv[1])
