#Aporte de PEDRO LUNA
import ply.lex as lex
import ply.yacc as yacc

            #Modificadores de flujo
reserved= {'if':'IF',
           'else':'ELSE',
           'when': 'WHEN', 
           'while':'WHILE',
           'for':'FOR',
           'print':'PRINT',
           'do':'DO',
           'continue':'CONTINUE',
           'break':'BREAK',
            'return':'return',
          #Modificadores de visibilidad y tipo
           'public':'PUBLIC',
           'private':'PRIVATE',
           'protected':'PROTECTED',
           'internal': 'INTERNAL',
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
           #Modificadores y Anotaciones de Funciones -Aporte Kevin
           'suspend':'SUSPEND',
           'inline':'INLINE', 
           'noinline':'NOINLINE', 
           'crossinline':'CROSSINLINE',
           'trailrec': 'TRAILREC',
           'operator':'OPERATOR',
           'infix':'INFIX',
           'out':'OUT',
           'reified':'REIFIED', 
           'by':'BY',
           'delegate':'DELEGATE',
           'yield':'YIELD',
           'package':'PACKAGE', 
           'import':'IMPORT',
           'where':'WHERE',
           'typeof':'field',
            'listOf':'LISTOF', #fin aporte Kevin Quintuña
           'inline':'INLINE',
           'noinline':'NOINLINE',
           'crossinline':'CROSSINLINE',
           'tailrec':'TAILREC',
           'operator':'OPERATOR',
           'infix':'INFIX',
           'out':'OUT',
           'reified':'REIFIED',
           #Control de Concurrencia y Delegación
           'by':'BY',
           'delegate':'DELEGATE',
           'yield':'YIELD',
           #Otros
           'package':'PACKAGE',
           'import':'IMPORT',
           'where':'WHERE',
           'typeof':'TYPEOF',
           'field':'FIELD',
           #Palabras reservadas de Emilio Romero - listas, mapas y conjuntos
           'listOf':'LISTOF',
           'mapOf':'MAPOF',
           'setOf':'SETOF',
           'mutableListOf': 'MUTABLELISTOF',
           'mutableMapOf': 'MUTABLEMAPOF',
           'mutableSetOf': 'MUTABLESETOF',
           #Fin aporte de palabras reservadas de Emilio Romero
            'println':'PRINT',
           'println':'PRINTLN',
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
    'RCOR',
    #Kevin Quintuna   
    'COMMA',
    'DOUBLE_QUOTA',
    'STRING',
    'EQUALS', #------VERIFICAR SI ES PALABRA RESERVADA
    'ASIGN',
    'SUMASIGN',
    'RESTASIGN',
    'MULTASIGN',
    'DIVASIGN',
    'MODASIGN',
    'NOT_EQUALS',
    'GREATER',
    'LESS',
    'GREATER_EQUALS',
    'LESS_EQUALS',
    'AND',
    'OR',
    'NOT',
    'RANGE_TO',
    'COLON',
    #Tokens - Parte de Emilio Romero
    'LLLAVE',
    'RLLAVE',
    'COMMENTLINEA',
    'COMMENTMULTI',
    'INTERPOLACION',
    'DOLAR'
    #Fin aporte de Tokens - Emilio Romero
    )+ tuple(reserved.values()))
    

# Regular expression rules for simple tokens
#operadores aritmeticos
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD   =   r'%'

# simbolos Especiales
t_PUYCO = r';'
t_LCOR = r'\['
t_RCOR  = r'\]'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
#Aporte Kevin Quintuña
t_DOUBLE_QUOTA= r'"' 
t_COMMA= r','
t_COLON= r':'
#Fin aporte Kevin Quintuña
#Fin aporte Pedro Luna 9/11
#Regular expression of Emilio Romero
t_LLLAVE = r'\{'
t_RLLAVE = r'\}'
#Fin aporte de expresiones regulares - Emilio Romero

# operadores De asignacion -Aporte Kevin  uintuña
t_ASIGN = r'='
t_SUMASIGN = r'\+='
t_RESTASIGN = r'-='
t_MULTASIGN = r'\*='
t_DIVASIGN = r'/='
t_MODASIGN = r'%='

#operadores logicos-- operadores logicos
t_AND = r'&&' 
t_OR  = r"\|\|"
t_NOT = r"!"

# Operadores de comparación
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUALS = r'>='
t_LESS_EQUALS = r'<='

#operadores extra 
t_RANGE_TO = r'\.\.'


#Fin Aporte Kevin Quintuña

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
#OPERADORES LOGICOS

#Fin Aporte Kevin Quintuña

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Funciones de Emilio Romero
def t_COMMENTLINEA(t): #funcion comment linea
    r'//.*'
    return t

def t_COMMENTMULTI(t): #funcion comment multilinea
    r'\/\*([^*]|\*+[^*/])*\*+\/'
    return t

def t_INTERPOLACION(t): #funcion interpolacion
    r'\$[a-zA-Z_][a-zA-Z_0-9]*'
    return t
    
def t_DOLAR(t): #funcion dolar
    r'\$'
    return t
#Fin aporte funciones de Emilio Romero

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

"""
#Extraer datos de algoritmo_Emilio.kt
with open("algoritmo_Emilio.kt", "r") as file:
    data_Emilio = file.read()

#Creacion de archivo log
import datetime
now = datetime.datetime.now()
log_emjorome = f"lexico-emjorome-{now.strftime('%d%m%Y-%Hh%M')}.txt"

# Give the lexer some input
lexer.input(data_Emilio)

# Tokenize
with open(log_emjorome,"w") as log_file: #creacion archivo log
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
        log_file.write(f"{tok}\n") #escribir el archivo

"""
#Extraer datos
with open("algoritmoKevinQuintuna.kt", "r") as file:
    data_ = file.read()

#Creacion de archivo log
import datetime
now = datetime.datetime.now()
#creacion de logs
log_ = f"lexico-Kevin-QQ-82-{now.strftime('%d%m%Y-%Hh%M')}.txt"

# Give the lexer some input
lexer.input(data_)

# Tokenize
with open(log_,"w") as log_file: #creacion archivo log
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
        log_file.write(f"{tok}\n") #escribir el archivo




