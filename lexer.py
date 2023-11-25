import ply.lex as lex

# Reserved words
reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'do' : 'DO',
   'VARS' : 'VARS',
   'int' : 'INT',
   'float' : 'FLOAT',
   'string' : 'STRING',
   'bool' : 'BOOL',
   'true' : 'TRUE',
   'false' : 'FALSE',
   'program' : 'PROGRAM',
   'function' : 'FUNCTION',
   'return' : 'RETURN',
   'read' : 'READ',
   'write' : 'WRITE',
   'main' : 'MAIN'
}

# List of token names.   This is always required
tokens = [
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'EQUAL',
   'EQUALTO',
   'LBRACKET',
   'RBRACKET',
   'LBRACE',
   'RBRACE',
   'COLON',
   'SEMICOLON',
   'COMMA',
   'GREATERTHAN',
   'SMALLERTHAN',
   'OR',
   'ENDL',
   'ID',
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_EQUAL   = r'='
t_EQUALTO = r'=='
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_COLON   = r':'
t_SEMICOLON = r';'
t_COMMA   = r','
t_GREATERTHAN = '>'
t_SMALLERTHAN = '<'
t_OR = r'\|'

# A regular expression rule with some action code
def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t

# A regular expression rule with some action code
def t_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = str(t.value)
    return t

def t_TRUE(t):
    r'TRUE'
    t.value = True
    return t

def t_FALSE(t):
    r'FALSE'
    t.value = False
    return t

#Defines PROGRAM before id so it doesnt gets confused
def t_PROGRAM(t):
    r'PROGRAM'
    t.type = reserved.get(t.value, 'PROGRAM')
    return t

#Defines VARS
def t_VARS(t):
    r'VARS'
    t.type = reserved.get(t.value, 'VARS')
    return t

#Defines Function
def t_FUNCTION(t):
    r'FUNCTION'
    t.type = reserved.get(t.value, 'FUNCTION')
    return t

#Defines return
def t_RETURN(t):
    r'RETURN'
    t.type = reserved.get(t.value, 'RETURN')
    return t

#Defines do to use with conditionals
def t_DO(t):
    r'DO'
    t.type = reserved.get(t.value, 'DO')
    return t

# Identifiers handler
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test
#data = " true > bool while (x + 2) string do{ write read for x to y do 1 \"Hola\"} main"
#lexer.input(data)

# Print tokens
#for token in lexer:
#    print(token)
