#Aporte de PEDRO LUNA
import ply.lex as lex
import ply.yacc as yacc

reserved= {'if':'IF',
           'else':'ELSE',
           'while':'WHILE',
           'for':'FOR',
           'print':'PRINT',
           'do':'DO',
           'continue':'CONTINUE',
           'break':'BREAK',
           #Modificadores de flujo
           'public':'PUBLIC',
           'private':'PRIVATE',
           'protected':'PROTECTED',
           'open':'OPEN',
           'abstract':'ABSTRACT',
           'final':'FINAL',
           'override':'OVERRIDE',
           'lateinit':'LATEINIT',
           'const':'CONST',
           #Funciones y clases
           'fun':'FUN',
           'class':'CLASS',
           'interface':'INTERFACE',
           'object':'OBJECT',
           'data':'DATA',
           'enum':'ENUM',
           'sealed':'SEALED',
           'companion':'COMPANION',
           'init':'INIT',
           'this':'THIS',
           'super':'SUPER',
           #Manejo de Excepciones
           'try':'TRY',
           'catch':'CATCH',
           'finally':'FINALLY',
           'throw':'THROW',
           #Declaración de Variables y Tipos
            'val':'VAL',
           'var':'VAR',
           'typealias':'TYPEALIAS',
           'is':'IS',
           'in':'IN',
           'as':'AS',
           'null':'NULL',
           'true':'TRUE',
           'false':'FALSE',
           #Modificadores y Anotaciones de Funciones
           'suspend':'SUSPEND'


           }

# List of token names.   This is always required
tokens = ((
   'NUMBER',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
    'MOD',
    'VARIABLE',
    'PUYCO',
    'FLOAT',
    'LCOR',
     'RCOR')+ tuple(reserved.values()))


# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MOD   =   r'%'
t_PUYCO = r';'
t_LCOR = r'\['
t_RCOR  = r'\]'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value= float(t.value)
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'VARIABLE')
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

# Test it out
data = '''
3 + 4 * 10 ABC _123 123 print(variable)
  + -20 *2  - ; 3.5
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)