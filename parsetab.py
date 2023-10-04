
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COLON COMMA DIVIDE DO ELSE ENDL EQUAL EQUALTO FLOAT FOR FUNCTION GREATERTHAN ID IF INT LBRACE LBRACKET LPAREN MINUS NUMBER OR PLUS PROGRAM RBRACE RBRACKET READ RETURN RPAREN SEMICOLON SMALLERTHAN STRING THEN TIMES TO VARS WHILE WRITE\n    program : PROGRAM ID SEMICOLON ENDL VARS define_vars define_function\n    \n    define_vars : type COLON id_list SEMICOLON define_vars\n                | empty\n    \n    type : INT\n         | FLOAT\n    \n    id_list : ID COMMA id_list\n            | ID\n    \n    define_function : FUNCTION type ID parameters ENDL VARS define_vars LBRACE statute RBRACE\n    \n    parameters : LPAREN type COLON id_list RPAREN\n    \n    statute : assignation statute\n            | decision statute\n            | condition statute\n            | no_condition statute\n            | return statute\n            | define_write statute\n            | read statute\n            | empty\n            \n    \n    assignation : ID EQUAL expression SEMICOLON\n                | ID GREATERTHAN expression SEMICOLON\n                | ID SMALLERTHAN expression SEMICOLON\n                | ID EQUALTO expression SEMICOLON\n                \n    \n    decision : IF LPAREN expression RPAREN THEN LBRACE statute RBRACE ELSE LBRACE statute RBRACE\n             | IF LPAREN expression RPAREN THEN LBRACE statute RBRACE\n    \n    condition : WHILE LPAREN expression RPAREN DO LBRACE statute RBRACE\n    \n    no_condition : FOR ID EQUAL expression TO expression DO LBRACE statute RBRACE\n    \n    return : RETURN LPAREN expression RPAREN SEMICOLON\n    \n    define_write : WRITE LPAREN write RPAREN SEMICOLON\n\n    \n    write : STRING\n          | expression\n          | STRING COMMA write\n          | expression COMMA write\n    \n    read : READ LPAREN id_list RPAREN SEMICOLON\n    \n    expression : expression PLUS term\n               | expression MINUS term\n               | expression GREATERTHAN term\n               | expression SMALLERTHAN term\n               | expression EQUALTO term\n    \n    expression : term\n    \n    term : term TIMES factor\n         | term DIVIDE factor\n    \n    term : factor\n    \n    factor : NUMBER\n    \n    factor : ID\n    \n    factor : PLUS factor\n           | MINUS factor\n    \n    factor : LPAREN expression RPAREN\n    empty :'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,12,53,],[0,-1,-8,]),'ID':([2,10,11,14,15,20,28,31,35,36,37,38,39,40,41,45,49,50,51,52,61,62,64,65,66,69,71,74,80,86,87,88,89,90,91,93,94,97,98,99,105,106,118,119,120,123,124,125,130,131,132,135,136,138,],[3,-4,-5,17,18,17,17,33,33,33,33,33,33,33,33,63,67,67,67,67,67,67,67,67,17,67,67,67,67,-18,67,67,67,67,67,67,67,-19,-20,-21,67,67,67,-26,-27,-32,33,33,-23,-24,33,33,-25,-22,]),'SEMICOLON':([3,16,17,24,67,68,70,72,73,75,76,77,92,95,103,104,107,108,109,110,111,112,113,114,115,],[4,19,-7,-6,-43,86,-38,-41,-42,97,98,99,-44,-45,119,120,123,-33,-34,-35,-36,-37,-39,-40,-46,]),'ENDL':([4,21,32,],[5,25,-9,]),'VARS':([5,25,],[6,27,]),'INT':([6,13,19,22,27,],[10,10,10,10,10,]),'FLOAT':([6,13,19,22,27,],[11,11,11,11,11,]),'FUNCTION':([6,7,9,19,23,],[-47,13,-3,-47,-2,]),'COLON':([8,10,11,26,],[14,-4,-5,28,]),'LBRACE':([9,19,23,27,29,116,117,129,133,],[-3,-47,-2,-47,31,124,125,132,135,]),'COMMA':([17,67,70,72,73,83,84,92,95,108,109,110,111,112,113,114,115,],[20,-43,-38,-41,-42,105,106,-44,-45,-33,-34,-35,-36,-37,-39,-40,-46,]),'RPAREN':([17,24,30,67,70,72,73,78,79,81,82,83,84,85,92,95,96,108,109,110,111,112,113,114,115,121,122,],[-7,-6,32,-43,-38,-41,-42,100,101,103,104,-28,-29,107,-44,-45,115,-33,-34,-35,-36,-37,-39,-40,-46,-30,-31,]),'LPAREN':([18,43,44,46,47,48,49,50,51,52,61,62,64,65,69,71,74,80,87,88,89,90,91,93,94,105,106,118,],[22,61,62,64,65,66,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'IF':([31,35,36,37,38,39,40,41,86,97,98,99,119,120,123,124,125,130,131,132,135,136,138,],[43,43,43,43,43,43,43,43,-18,-19,-20,-21,-26,-27,-32,43,43,-23,-24,43,43,-25,-22,]),'WHILE':([31,35,36,37,38,39,40,41,86,97,98,99,119,120,123,124,125,130,131,132,135,136,138,],[44,44,44,44,44,44,44,44,-18,-19,-20,-21,-26,-27,-32,44,44,-23,-24,44,44,-25,-22,]),'FOR':([31,35,36,37,38,39,40,41,86,97,98,99,119,120,123,124,125,130,131,132,135,136,138,],[45,45,45,45,45,45,45,45,-18,-19,-20,-21,-26,-27,-32,45,45,-23,-24,45,45,-25,-22,]),'RETURN':([31,35,36,37,38,39,40,41,86,97,98,99,119,120,123,124,125,130,131,132,135,136,138,],[46,46,46,46,46,46,46,46,-18,-19,-20,-21,-26,-27,-32,46,46,-23,-24,46,46,-25,-22,]),'WRITE':([31,35,36,37,38,39,40,41,86,97,98,99,119,120,123,124,125,130,131,132,135,136,138,],[47,47,47,47,47,47,47,47,-18,-19,-20,-21,-26,-27,-32,47,47,-23,-24,47,47,-25,-22,]),'READ':([31,35,36,37,38,39,40,41,86,97,98,99,119,120,123,124,125,130,131,132,135,136,138,],[48,48,48,48,48,48,48,48,-18,-19,-20,-21,-26,-27,-32,48,48,-23,-24,48,48,-25,-22,]),'RBRACE':([31,34,35,36,37,38,39,40,41,42,54,55,56,57,58,59,60,86,97,98,99,119,120,123,124,125,127,128,130,131,132,134,135,136,137,138,],[-47,53,-47,-47,-47,-47,-47,-47,-47,-17,-10,-11,-12,-13,-14,-15,-16,-18,-19,-20,-21,-26,-27,-32,-47,-47,130,131,-23,-24,-47,136,-47,-25,138,-22,]),'EQUAL':([33,63,],[49,80,]),'GREATERTHAN':([33,67,68,70,72,73,75,76,77,78,79,81,84,92,95,96,102,108,109,110,111,112,113,114,115,126,],[50,-43,89,-38,-41,-42,89,89,89,89,89,89,89,-44,-45,89,89,-33,-34,-35,-36,-37,-39,-40,-46,89,]),'SMALLERTHAN':([33,67,68,70,72,73,75,76,77,78,79,81,84,92,95,96,102,108,109,110,111,112,113,114,115,126,],[51,-43,90,-38,-41,-42,90,90,90,90,90,90,90,-44,-45,90,90,-33,-34,-35,-36,-37,-39,-40,-46,90,]),'EQUALTO':([33,67,68,70,72,73,75,76,77,78,79,81,84,92,95,96,102,108,109,110,111,112,113,114,115,126,],[52,-43,91,-38,-41,-42,91,91,91,91,91,91,91,-44,-45,91,91,-33,-34,-35,-36,-37,-39,-40,-46,91,]),'NUMBER':([49,50,51,52,61,62,64,65,69,71,74,80,87,88,89,90,91,93,94,105,106,118,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'PLUS':([49,50,51,52,61,62,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,84,87,88,89,90,91,92,93,94,95,96,102,105,106,108,109,110,111,112,113,114,115,118,126,],[69,69,69,69,69,69,69,69,-43,87,69,-38,69,-41,-42,69,87,87,87,87,87,69,87,87,69,69,69,69,69,-44,69,69,-45,87,87,69,69,-33,-34,-35,-36,-37,-39,-40,-46,69,87,]),'MINUS':([49,50,51,52,61,62,64,65,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,84,87,88,89,90,91,92,93,94,95,96,102,105,106,108,109,110,111,112,113,114,115,118,126,],[71,71,71,71,71,71,71,71,-43,88,71,-38,71,-41,-42,71,88,88,88,88,88,71,88,88,71,71,71,71,71,-44,71,71,-45,88,88,71,71,-33,-34,-35,-36,-37,-39,-40,-46,71,88,]),'STRING':([65,105,106,],[83,83,83,]),'TIMES':([67,70,72,73,92,95,108,109,110,111,112,113,114,115,],[-43,93,-41,-42,-44,-45,93,93,93,93,93,-39,-40,-46,]),'DIVIDE':([67,70,72,73,92,95,108,109,110,111,112,113,114,115,],[-43,94,-41,-42,-44,-45,94,94,94,94,94,-39,-40,-46,]),'TO':([67,70,72,73,92,95,102,108,109,110,111,112,113,114,115,],[-43,-38,-41,-42,-44,-45,118,-33,-34,-35,-36,-37,-39,-40,-46,]),'DO':([67,70,72,73,92,95,101,108,109,110,111,112,113,114,115,126,],[-43,-38,-41,-42,-44,-45,117,-33,-34,-35,-36,-37,-39,-40,-46,129,]),'THEN':([100,],[116,]),'ELSE':([130,],[133,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'define_vars':([6,19,27,],[7,23,29,]),'type':([6,13,19,22,27,],[8,15,8,26,8,]),'empty':([6,19,27,31,35,36,37,38,39,40,41,124,125,132,135,],[9,9,9,42,42,42,42,42,42,42,42,42,42,42,42,]),'define_function':([7,],[12,]),'id_list':([14,20,28,66,],[16,24,30,85,]),'parameters':([18,],[21,]),'statute':([31,35,36,37,38,39,40,41,124,125,132,135,],[34,54,55,56,57,58,59,60,127,128,134,137,]),'assignation':([31,35,36,37,38,39,40,41,124,125,132,135,],[35,35,35,35,35,35,35,35,35,35,35,35,]),'decision':([31,35,36,37,38,39,40,41,124,125,132,135,],[36,36,36,36,36,36,36,36,36,36,36,36,]),'condition':([31,35,36,37,38,39,40,41,124,125,132,135,],[37,37,37,37,37,37,37,37,37,37,37,37,]),'no_condition':([31,35,36,37,38,39,40,41,124,125,132,135,],[38,38,38,38,38,38,38,38,38,38,38,38,]),'return':([31,35,36,37,38,39,40,41,124,125,132,135,],[39,39,39,39,39,39,39,39,39,39,39,39,]),'define_write':([31,35,36,37,38,39,40,41,124,125,132,135,],[40,40,40,40,40,40,40,40,40,40,40,40,]),'read':([31,35,36,37,38,39,40,41,124,125,132,135,],[41,41,41,41,41,41,41,41,41,41,41,41,]),'expression':([49,50,51,52,61,62,64,65,74,80,105,106,118,],[68,75,76,77,78,79,81,84,96,102,84,84,126,]),'term':([49,50,51,52,61,62,64,65,74,80,87,88,89,90,91,105,106,118,],[70,70,70,70,70,70,70,70,70,70,108,109,110,111,112,70,70,70,]),'factor':([49,50,51,52,61,62,64,65,69,71,74,80,87,88,89,90,91,93,94,105,106,118,],[72,72,72,72,72,72,72,72,92,95,72,72,72,72,72,72,72,113,114,72,72,72,]),'write':([65,105,106,],[82,121,122,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMICOLON ENDL VARS define_vars define_function','program',7,'p_program','parser_1.py',6),
  ('define_vars -> type COLON id_list SEMICOLON define_vars','define_vars',5,'p_define_vars','parser_1.py',11),
  ('define_vars -> empty','define_vars',1,'p_define_vars','parser_1.py',12),
  ('type -> INT','type',1,'p_type','parser_1.py',17),
  ('type -> FLOAT','type',1,'p_type','parser_1.py',18),
  ('id_list -> ID COMMA id_list','id_list',3,'p_id_list','parser_1.py',23),
  ('id_list -> ID','id_list',1,'p_id_list','parser_1.py',24),
  ('define_function -> FUNCTION type ID parameters ENDL VARS define_vars LBRACE statute RBRACE','define_function',10,'p_define_function','parser_1.py',29),
  ('parameters -> LPAREN type COLON id_list RPAREN','parameters',5,'p_parameters','parser_1.py',34),
  ('statute -> assignation statute','statute',2,'p_statute','parser_1.py',39),
  ('statute -> decision statute','statute',2,'p_statute','parser_1.py',40),
  ('statute -> condition statute','statute',2,'p_statute','parser_1.py',41),
  ('statute -> no_condition statute','statute',2,'p_statute','parser_1.py',42),
  ('statute -> return statute','statute',2,'p_statute','parser_1.py',43),
  ('statute -> define_write statute','statute',2,'p_statute','parser_1.py',44),
  ('statute -> read statute','statute',2,'p_statute','parser_1.py',45),
  ('statute -> empty','statute',1,'p_statute','parser_1.py',46),
  ('assignation -> ID EQUAL expression SEMICOLON','assignation',4,'p_assignation','parser_1.py',52),
  ('assignation -> ID GREATERTHAN expression SEMICOLON','assignation',4,'p_assignation','parser_1.py',53),
  ('assignation -> ID SMALLERTHAN expression SEMICOLON','assignation',4,'p_assignation','parser_1.py',54),
  ('assignation -> ID EQUALTO expression SEMICOLON','assignation',4,'p_assignation','parser_1.py',55),
  ('decision -> IF LPAREN expression RPAREN THEN LBRACE statute RBRACE ELSE LBRACE statute RBRACE','decision',12,'p_decision','parser_1.py',60),
  ('decision -> IF LPAREN expression RPAREN THEN LBRACE statute RBRACE','decision',8,'p_decision','parser_1.py',61),
  ('condition -> WHILE LPAREN expression RPAREN DO LBRACE statute RBRACE','condition',8,'p_condition','parser_1.py',66),
  ('no_condition -> FOR ID EQUAL expression TO expression DO LBRACE statute RBRACE','no_condition',10,'p_no_condition','parser_1.py',71),
  ('return -> RETURN LPAREN expression RPAREN SEMICOLON','return',5,'p_return','parser_1.py',76),
  ('define_write -> WRITE LPAREN write RPAREN SEMICOLON','define_write',5,'p_define_write','parser_1.py',81),
  ('write -> STRING','write',1,'p_write','parser_1.py',87),
  ('write -> expression','write',1,'p_write','parser_1.py',88),
  ('write -> STRING COMMA write','write',3,'p_write','parser_1.py',89),
  ('write -> expression COMMA write','write',3,'p_write','parser_1.py',90),
  ('read -> READ LPAREN id_list RPAREN SEMICOLON','read',5,'p_read','parser_1.py',95),
  ('expression -> expression PLUS term','expression',3,'p_expression','parser_1.py',100),
  ('expression -> expression MINUS term','expression',3,'p_expression','parser_1.py',101),
  ('expression -> expression GREATERTHAN term','expression',3,'p_expression','parser_1.py',102),
  ('expression -> expression SMALLERTHAN term','expression',3,'p_expression','parser_1.py',103),
  ('expression -> expression EQUALTO term','expression',3,'p_expression','parser_1.py',104),
  ('expression -> term','expression',1,'p_expression_term','parser_1.py',109),
  ('term -> term TIMES factor','term',3,'p_term','parser_1.py',114),
  ('term -> term DIVIDE factor','term',3,'p_term','parser_1.py',115),
  ('term -> factor','term',1,'p_term_factor','parser_1.py',120),
  ('factor -> NUMBER','factor',1,'p_factor_number','parser_1.py',125),
  ('factor -> ID','factor',1,'p_factor_id','parser_1.py',130),
  ('factor -> PLUS factor','factor',2,'p_factor_unary','parser_1.py',135),
  ('factor -> MINUS factor','factor',2,'p_factor_unary','parser_1.py',136),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_grouped','parser_1.py',141),
  ('empty -> <empty>','empty',0,'p_empty','parser_1.py',149),
]
