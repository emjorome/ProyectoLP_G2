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
           #Modificadores y Anotaciones de Funciones
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
            'listOf':'LISTOF'


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
    'COMMA',
    'DOUBLE_QUOTA',
    'INMUT_LISTOF',
    'VALUE',
    'STRING',
#Kevin Quintuna     
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
t_DOUBLE_QUOTA= r'"' 
t_COMMA= r','

# De asignacion
t_ASIGN = r'='
t_SUMASIGN = r'\+='
t_RESTASIGN = r'-='
t_MULTASIGN = r'\*='
t_DIVASIGN = r'/='
t_MODASIGN = r'%='

# Operadores de comparación
t_EQUALS = r'=='
t_NOT_EQUALS = r'!='
t_GREATER = r'>'
t_LESS = r'<'
t_GREATER_EQUALS = r'>='
t_LESS_EQUALS = r'<='


def t_STRING(t):
    r'"[^"]*"'  # Coincide con cualquier secuencia de caracteres entre comillas dobles
    t.value = t.value[1:-1]  # Remueve las comillas al principio y al final
    return t
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
def t_AND(t):
    r'&&'
    t.type = bool(t.value)
    return t

def t_OR(t):
    r'\|\|'
    t.type = bool(t.value)
    return t

def t_NOT(t):
    r'!'
    t.type = bool(t.value)
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
fun main() {
    var a = 10
    var b = 20
    var c = a + b * 2

    if (c >= 30 && b != 0) {
        println("Resultado: $c")
    } else {
        println("Valor de b es cero")
    }

    for (i in 1..5) {
        println("Iteración $i")
    }
}
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)