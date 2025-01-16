
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN COMMA CONST DIVIDE ELSE EQUAL FALSE FLOAT FLOAT_LITERAL GREATER GREATER_EQUAL IDENTIFIER IF INPUT INT INTEGER_LITERAL LBRACE LESS LESS_EQUAL LPAREN MINUS MULTIPLY NOT NOTEQUAL PLUS PRINT PROGRAM RBRACE RPAREN SEMICOLON STR STRING_LITERAL TRUE WHILEprogram : PROGRAM IDENTIFIER LBRACE declarations statements RBRACEdeclarations : declarations declaration\n                    | emptydeclaration : type IDENTIFIER SEMICOLON\n                   | type IDENTIFIER COMMA identifiers SEMICOLONtype : INT\n            | FLOAT\n            | STRidentifiers : IDENTIFIER\n                   | IDENTIFIER COMMA identifiersstatements : statements statement\n                   | statementstatement : declaration\n                 | assignment\n                 | if_statement\n                 | while_statement\n                 | print_statement\n                 | input_statement\n                 | function_callassignment : IDENTIFIER ASSIGN expression SEMICOLONexpression : INTEGER_LITERAL\n                   | FLOAT_LITERAL\n                   | STRING_LITERAL\n                   | IDENTIFIER\n                   | expression PLUS expression\n                   | expression MINUS expression\n                   | expression MULTIPLY expression\n                   | expression DIVIDE expression\n                   | expression EQUAL expression\n                   | expression NOTEQUAL expression\n                   | expression GREATER expression\n                   | expression LESS expression\n                   | expression GREATER_EQUAL expression\n                   | expression LESS_EQUAL expression\n                   | LPAREN expression RPARENif_statement : IF LPAREN expression RPAREN LBRACE statements RBRACE else_statementelse_statement : ELSE LBRACE statements RBRACE\n                      | emptywhile_statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACEprint_statement : PRINT LPAREN argument_list RPAREN SEMICOLONinput_statement : INPUT LPAREN argument_list RPAREN SEMICOLONfunction_call : IDENTIFIER LPAREN argument_list RPAREN SEMICOLONargument_list : expression\n                     | expression COMMA argument_list\n                     | emptyempty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,27,],[0,-1,]),'IDENTIFIER':([2,4,5,6,8,9,10,11,12,13,14,15,16,17,18,19,20,25,26,28,29,31,32,33,34,40,44,45,50,51,52,53,54,55,56,57,58,59,60,63,81,83,84,85,86,87,88,90,91,92,93,94,96,97,98,99,],[3,-46,7,-3,7,-2,-12,30,-14,-15,-16,-17,-18,-19,-6,-7,-8,35,35,-11,-13,35,35,35,35,35,-4,64,-20,35,35,35,35,35,35,35,35,35,35,35,-42,64,-5,7,7,-40,-41,7,7,-46,-39,-36,-38,7,7,-37,]),'LBRACE':([3,66,67,95,],[4,85,86,97,]),'INT':([4,5,6,8,9,10,12,13,14,15,16,17,28,29,44,50,81,84,85,86,87,88,90,91,92,93,94,96,97,98,99,],[-46,18,-3,18,-2,-12,-14,-15,-16,-17,-18,-19,-11,-13,-4,-20,-42,-5,18,18,-40,-41,18,18,-46,-39,-36,-38,18,18,-37,]),'FLOAT':([4,5,6,8,9,10,12,13,14,15,16,17,28,29,44,50,81,84,85,86,87,88,90,91,92,93,94,96,97,98,99,],[-46,19,-3,19,-2,-12,-14,-15,-16,-17,-18,-19,-11,-13,-4,-20,-42,-5,19,19,-40,-41,19,19,-46,-39,-36,-38,19,19,-37,]),'STR':([4,5,6,8,9,10,12,13,14,15,16,17,28,29,44,50,81,84,85,86,87,88,90,91,92,93,94,96,97,98,99,],[-46,20,-3,20,-2,-12,-14,-15,-16,-17,-18,-19,-11,-13,-4,-20,-42,-5,20,20,-40,-41,20,20,-46,-39,-36,-38,20,20,-37,]),'IF':([4,5,6,8,9,10,12,13,14,15,16,17,28,29,44,50,81,84,85,86,87,88,90,91,92,93,94,96,97,98,99,],[-46,21,-3,21,-2,-12,-14,-15,-16,-17,-18,-19,-11,-13,-4,-20,-42,-5,21,21,-40,-41,21,21,-46,-39,-36,-38,21,21,-37,]),'WHILE':([4,5,6,8,9,10,12,13,14,15,16,17,28,29,44,50,81,84,85,86,87,88,90,91,92,93,94,96,97,98,99,],[-46,22,-3,22,-2,-12,-14,-15,-16,-17,-18,-19,-11,-13,-4,-20,-42,-5,22,22,-40,-41,22,22,-46,-39,-36,-38,22,22,-37,]),'PRINT':([4,5,6,8,9,10,12,13,14,15,16,17,28,29,44,50,81,84,85,86,87,88,90,91,92,93,94,96,97,98,99,],[-46,23,-3,23,-2,-12,-14,-15,-16,-17,-18,-19,-11,-13,-4,-20,-42,-5,23,23,-40,-41,23,23,-46,-39,-36,-38,23,23,-37,]),'INPUT':([4,5,6,8,9,10,12,13,14,15,16,17,28,29,44,50,81,84,85,86,87,88,90,91,92,93,94,96,97,98,99,],[-46,24,-3,24,-2,-12,-14,-15,-16,-17,-18,-19,-11,-13,-4,-20,-42,-5,24,24,-40,-41,24,24,-46,-39,-36,-38,24,24,-37,]),'ASSIGN':([7,],[25,]),'LPAREN':([7,21,22,23,24,25,26,31,32,33,34,40,51,52,53,54,55,56,57,58,59,60,63,],[26,31,32,33,34,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'RBRACE':([8,9,10,12,13,14,15,16,17,28,29,44,50,81,84,87,88,90,91,92,93,94,96,98,99,],[27,-13,-12,-14,-15,-16,-17,-18,-19,-11,-13,-4,-20,-42,-5,-40,-41,92,93,-46,-39,-36,-38,99,-37,]),'INTEGER_LITERAL':([25,26,31,32,33,34,40,51,52,53,54,55,56,57,58,59,60,63,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'FLOAT_LITERAL':([25,26,31,32,33,34,40,51,52,53,54,55,56,57,58,59,60,63,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'STRING_LITERAL':([25,26,31,32,33,34,40,51,52,53,54,55,56,57,58,59,60,63,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'RPAREN':([26,33,34,35,37,38,39,41,42,43,46,47,48,49,61,63,70,71,72,73,74,75,76,77,78,79,80,82,],[-46,-46,-46,-24,-21,-22,-23,62,-43,-45,66,67,68,69,80,-46,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-44,]),'SEMICOLON':([30,35,36,37,38,39,62,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,89,],[44,-24,50,-21,-22,-23,81,-9,84,87,88,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,-10,]),'COMMA':([30,35,37,38,39,42,64,70,71,72,73,74,75,76,77,78,79,80,],[45,-24,-21,-22,-23,63,83,-25,-26,-27,-28,-29,-30,-31,-32,-33,-34,-35,]),'PLUS':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,51,-21,-22,-23,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-35,]),'MINUS':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,52,-21,-22,-23,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-35,]),'MULTIPLY':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,53,-21,-22,-23,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-35,]),'DIVIDE':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,54,-21,-22,-23,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-35,]),'EQUAL':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,55,-21,-22,-23,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-35,]),'NOTEQUAL':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,56,-21,-22,-23,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-35,]),'GREATER':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,57,-21,-22,-23,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-35,]),'LESS':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,58,-21,-22,-23,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-35,]),'GREATER_EQUAL':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,59,-21,-22,-23,59,59,59,59,59,59,59,59,59,59,59,59,59,59,-35,]),'LESS_EQUAL':([35,36,37,38,39,42,46,47,61,70,71,72,73,74,75,76,77,78,79,80,],[-24,60,-21,-22,-23,60,60,60,60,60,60,60,60,60,60,60,60,60,60,-35,]),'ELSE':([92,],[95,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declarations':([4,],[5,]),'empty':([4,26,33,34,63,92,],[6,43,43,43,43,96,]),'statements':([5,85,86,97,],[8,90,91,98,]),'declaration':([5,8,85,86,90,91,97,98,],[9,29,29,29,29,29,29,29,]),'statement':([5,8,85,86,90,91,97,98,],[10,28,10,10,28,28,10,28,]),'type':([5,8,85,86,90,91,97,98,],[11,11,11,11,11,11,11,11,]),'assignment':([5,8,85,86,90,91,97,98,],[12,12,12,12,12,12,12,12,]),'if_statement':([5,8,85,86,90,91,97,98,],[13,13,13,13,13,13,13,13,]),'while_statement':([5,8,85,86,90,91,97,98,],[14,14,14,14,14,14,14,14,]),'print_statement':([5,8,85,86,90,91,97,98,],[15,15,15,15,15,15,15,15,]),'input_statement':([5,8,85,86,90,91,97,98,],[16,16,16,16,16,16,16,16,]),'function_call':([5,8,85,86,90,91,97,98,],[17,17,17,17,17,17,17,17,]),'expression':([25,26,31,32,33,34,40,51,52,53,54,55,56,57,58,59,60,63,],[36,42,46,47,42,42,61,70,71,72,73,74,75,76,77,78,79,42,]),'argument_list':([26,33,34,63,],[41,48,49,82,]),'identifiers':([45,83,],[65,89,]),'else_statement':([92,],[94,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM IDENTIFIER LBRACE declarations statements RBRACE','program',6,'p_program','parser.py',19),
  ('declarations -> declarations declaration','declarations',2,'p_declarations','parser.py',23),
  ('declarations -> empty','declarations',1,'p_declarations','parser.py',24),
  ('declaration -> type IDENTIFIER SEMICOLON','declaration',3,'p_declaration','parser.py',31),
  ('declaration -> type IDENTIFIER COMMA identifiers SEMICOLON','declaration',5,'p_declaration','parser.py',32),
  ('type -> INT','type',1,'p_type','parser.py',40),
  ('type -> FLOAT','type',1,'p_type','parser.py',41),
  ('type -> STR','type',1,'p_type','parser.py',42),
  ('identifiers -> IDENTIFIER','identifiers',1,'p_identifiers','parser.py',46),
  ('identifiers -> IDENTIFIER COMMA identifiers','identifiers',3,'p_identifiers','parser.py',47),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',51),
  ('statements -> statement','statements',1,'p_statements','parser.py',52),
  ('statement -> declaration','statement',1,'p_statement','parser.py',59),
  ('statement -> assignment','statement',1,'p_statement','parser.py',60),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',61),
  ('statement -> while_statement','statement',1,'p_statement','parser.py',62),
  ('statement -> print_statement','statement',1,'p_statement','parser.py',63),
  ('statement -> input_statement','statement',1,'p_statement','parser.py',64),
  ('statement -> function_call','statement',1,'p_statement','parser.py',65),
  ('assignment -> IDENTIFIER ASSIGN expression SEMICOLON','assignment',4,'p_assignment','parser.py',69),
  ('expression -> INTEGER_LITERAL','expression',1,'p_expression','parser.py',74),
  ('expression -> FLOAT_LITERAL','expression',1,'p_expression','parser.py',75),
  ('expression -> STRING_LITERAL','expression',1,'p_expression','parser.py',76),
  ('expression -> IDENTIFIER','expression',1,'p_expression','parser.py',77),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser.py',78),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser.py',79),
  ('expression -> expression MULTIPLY expression','expression',3,'p_expression','parser.py',80),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser.py',81),
  ('expression -> expression EQUAL expression','expression',3,'p_expression','parser.py',82),
  ('expression -> expression NOTEQUAL expression','expression',3,'p_expression','parser.py',83),
  ('expression -> expression GREATER expression','expression',3,'p_expression','parser.py',84),
  ('expression -> expression LESS expression','expression',3,'p_expression','parser.py',85),
  ('expression -> expression GREATER_EQUAL expression','expression',3,'p_expression','parser.py',86),
  ('expression -> expression LESS_EQUAL expression','expression',3,'p_expression','parser.py',87),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','parser.py',88),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE statements RBRACE else_statement','if_statement',8,'p_if_statement','parser.py',99),
  ('else_statement -> ELSE LBRACE statements RBRACE','else_statement',4,'p_else_statement','parser.py',103),
  ('else_statement -> empty','else_statement',1,'p_else_statement','parser.py',104),
  ('while_statement -> WHILE LPAREN expression RPAREN LBRACE statements RBRACE','while_statement',7,'p_while_statement','parser.py',111),
  ('print_statement -> PRINT LPAREN argument_list RPAREN SEMICOLON','print_statement',5,'p_print_statement','parser.py',115),
  ('input_statement -> INPUT LPAREN argument_list RPAREN SEMICOLON','input_statement',5,'p_input_statement','parser.py',119),
  ('function_call -> IDENTIFIER LPAREN argument_list RPAREN SEMICOLON','function_call',5,'p_function_call','parser.py',123),
  ('argument_list -> expression','argument_list',1,'p_argument_list','parser.py',128),
  ('argument_list -> expression COMMA argument_list','argument_list',3,'p_argument_list','parser.py',129),
  ('argument_list -> empty','argument_list',1,'p_argument_list','parser.py',130),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',137),
]
