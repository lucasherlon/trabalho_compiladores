import ply.yacc as yacc
from lexer import tokens, lexer, reserved
import sys

# Tabela de símbolos
symbol_table = {}

def add_symbol(identifier, var_type):
    if identifier in symbol_table:
        raise Exception(f"Erro: Variável '{identifier}' já declarada")
    symbol_table[identifier] = {"type": var_type}

def check_declaration(identifier):
    if identifier not in symbol_table and identifier not in reserved:
        raise Exception(f"Erro: Identificador '{identifier}' não declarado")

def get_type(identifier):
    if identifier in symbol_table:
        return symbol_table[identifier]["type"]
    raise Exception(f"Erro: Identificador '{identifier}' não declarado")

# Regras do analisador sintático
def p_program(p):
    "program : PROGRAM IDENTIFIER LBRACE declarations statements RBRACE"
    p[0] = ("program", p[2], p[4], p[5])

def p_declarations(p):
    """declarations : declarations declaration
                    | empty"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = []

def p_declaration(p):
    """declaration : type IDENTIFIER SEMICOLON
                   | type IDENTIFIER COMMA identifiers SEMICOLON
                   | CONST IDENTIFIER ASSIGN expression SEMICOLON"""
    if p[1] == 'const':
        add_symbol(p[2], 'const')
        p[0] = ("const_declaration", p[2], p[4])
    else:
        add_symbol(p[2], p[1])
        if len(p) > 4:  # Suporte a múltiplas variáveis
            for identifier in p[4]:
                add_symbol(identifier, p[1])
        p[0] = ("declaration", p[1], [p[2]] + (p[4] if len(p) > 4 else []))

def p_type(p):
    """type : INT
            | FLOAT
            | STR
            | BOOL"""
    p[0] = p[1]

def p_identifiers(p):
    """identifiers : IDENTIFIER
                   | IDENTIFIER COMMA identifiers"""
    p[0] = [p[1]] + (p[3] if len(p) > 2 else [])

def p_statements(p):
    """statements : statements statement
                   | statement"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    """statement : declaration
                 | assignment
                 | if_statement
                 | while_statement
                 | print_statement
                 | input_statement
                 | function_call"""
    p[0] = p[1]

def p_assignment(p):
    "assignment : IDENTIFIER ASSIGN expression SEMICOLON"
    check_declaration(p[1])
    var_type = get_type(p[1])
    expr_type = p[3][1]
    if var_type != expr_type:
        raise Exception(f"Erro de tipo: Não é possível atribuir {expr_type} a {var_type}")
    p[0] = ("assign", p[1], p[3])

def p_expression(p):
    """expression : INTEGER_LITERAL
                   | FLOAT_LITERAL
                   | STRING_LITERAL
                   | IDENTIFIER
                   | TRUE
                   | FALSE
                   | LPAREN expression RPAREN
                   | expression PLUS expression
                   | expression MINUS expression
                   | expression MULTIPLY expression
                   | expression DIVIDE expression
                   | expression EQUAL expression
                   | expression NOTEQUAL expression
                   | expression GREATER expression
                   | expression LESS expression
                   | expression GREATER_EQUAL expression
                   | expression LESS_EQUAL expression"""
    if len(p) == 2:
        if isinstance(p[1], str) and p[1] in symbol_table:
            check_declaration(p[1])
            p[0] = (p[1], get_type(p[1]))
        elif isinstance(p[1], int):
            p[0] = (p[1], 'int')
        elif isinstance(p[1], float):
            p[0] = (p[1], 'float')
        elif p[1] in ['true', 'false']:
            p[0] = (p[1], 'bool')
        else:
            p[0] = (p[1], 'str')
    elif len(p) == 3:
        p[0] = p[2]
    else:
        left_type = p[1][1]
        right_type = p[3][1]
        if left_type != right_type:
            raise Exception(f"Erro de tipo: Operação entre {left_type} e {right_type} não permitida")
        if p[2] in ['==', '!=', '>', '<', '>=', '<=']:
            p[0] = (p[2], 'bool')
        else:
            p[0] = (p[2], left_type)

def p_if_statement(p):
    "if_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE else_statement"
    if p[3][1] != 'bool':
        raise Exception("Erro de tipo: A expressão da condição do if deve ser do tipo bool")
    p[0] = ("if", p[3], p[6], p[8])

def p_else_statement(p):
    """else_statement : ELSE LBRACE statements RBRACE
                      | empty"""
    if len(p) == 5:
        p[0] = ('else', p[3])
    else:
        p[0] = None

def p_while_statement(p):
    "while_statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACE"
    if p[3][1] != 'bool':
        raise Exception("Erro de tipo: A expressão da condição do while deve ser do tipo bool")
    p[0] = ("while", p[3], p[6])

def p_print_statement(p):
    """print_statement : PRINT LPAREN expression RPAREN SEMICOLON
                       | PRINT LPAREN expression COMMA expression RPAREN SEMICOLON"""
    if len(p) == 6:
        p[0] = ("print", p[3])
    else:
        p[0] = ("print", p[3], p[5])

def p_input_statement(p):
    """input_statement : INPUT LPAREN IDENTIFIER RPAREN SEMICOLON
                       | INPUT LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN SEMICOLON"""
    check_declaration(p[3])
    if len(p) == 8:
        check_declaration(p[5])
        p[0] = ("input", p[3], p[5])
    else:
        p[0] = ("input", p[3])

def p_function_call(p):
    """function_call : IDENTIFIER LPAREN argument_list RPAREN SEMICOLON"""
    check_declaration(p[1])  # Verifica se a função é válida (ex.: funções nativas)
    p[0] = ("function_call", p[1], p[3])

def p_argument_list(p):
    """argument_list : expression
                     | expression COMMA argument_list
                     | empty"""
    if len(p) == 2:  # Apenas um argumento ou vazio
        p[0] = [p[1]] if p[1] is not None else []
    else:  # Múltiplos argumentos
        p[0] = [p[1]] + p[3]

def p_empty(p):
    "empty :"
    p[0] = None

def p_error(p):
    if p:
        print(f"Erro de sintaxe na linha {p.lineno}: token inesperado '{p.value}'")
    else:
        print("Erro de sintaxe: EOF inesperado")

# Construção do parser
parser = yacc.yacc()

# Função principal para análise do arquivo
def main():
    if len(sys.argv) != 2:
        print("Uso: python parser.py <arquivo.txt>")
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        with open(filepath, 'r') as file:
            data = file.read()
            result = parser.parse(data, lexer=lexer)
            print("Análise concluída com sucesso:", result)
    except Exception as e:
        print("Erro:", str(e))

if __name__ == "__main__":
    main()