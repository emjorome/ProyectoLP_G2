#Aporte de PEDRO LUNA
import ply.lex as lex

resultados = []
validar_lexico = True

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
            'return':'RETURN',     
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
           'typeof':'field',#fin aporte Kevin Quintuña
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
           'constructor': 'CONSTRUCTOR',
           #Fin aporte de palabras reservadas de Emilio Romero
            'print':'PRINT',
           'println':'PRINTLN',
            'to': 'TO_FROM_KV',
           'input':'INPUT',
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
    'DOT',
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
    'PROPERTY',
    'METHOD',
    #Tipos de datos
    'STRING',
    'GENERIC_TYPE',

    #Tokens - Parte de Emilio Romero
    'LLLAVE',
    'RLLAVE',
    'COMMENTLINEA',
    'COMMENTMULTI',
    'INTERPOLACION',
    'DOLAR',
    'BYTE',
    'SHORT',
    'INT',
    'LONG',
    'DOUBLE',
    'BOOLEAN',
    'CHAR',
    'NULLABLE_TYPE'
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
t_DOT= r'\.'
#Fin aporte Kevin Quintuña
#Inicio Aporte Pedro Luna
# Expresiones regulares para tipos de datos en Kotlin
t_BYTE = r'Byte'
t_SHORT = r'Short'
t_INT = r'Int'
t_LONG = r'Long'
t_DOUBLE = r'Double'
t_BOOLEAN = r'Boolean'
t_CHAR = r'Char'
t_NULLABLE_TYPE = r'(Byte|Short|Int|Long|Float|Double|Boolean|Char|String)\?'

#Fin aporte Pedro Luna
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

#---------aportes extra kevin q------------revisar el string no funciona


def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    return t
def t_GENERIC_TYPE(t):
    r'<[^>]+>'  # Identificador seguido de <contenido> y cerrado por >
    return t
def t_METHOD(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*\.[a-zA-Z_][a-zA-Z_0-9]*\([^\)]*\)'  # Identificador seguido de un punto y otro identificador que termina con paréntesis
    return t

def t_PROPERTY(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*\.[a-zA-Z_][a-zA-Z_0-9]*'  # Identificador seguido de un punto y otro identificador
    return t



#----------

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

#Inicio Aporte Pedro Luna
def t_LONG_NUMBER(t):
    r'\d+L'
    t.value = int(t.value[:-1])
    return t
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    resultados.append("Illegal character '%s'" % t.value[0])
    #aseguro que el validador lexico indique que el codigo no es validado
    global validar_lexico
    validar_lexico = False
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = ""

# Give the lexer some input
lexer.input(data)

while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)

def vaciar_resultados():
    resultados.clear()

def analizar_lexico(codigo):
    lexer.lineno = 1
    #Inicializo que el la variable para una siguiente ejecucion de codigo
    global validar_lexico
    validar_lexico = True

    lexer.input(codigo)

    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input

        resultados.append(f"(Token -> {tok.type} | Valor -> {tok.value} | Linea -> {tok.lineno})")

    print(validar_lexico)
    return resultados


'''


// Clase con propiedades y funciones
class Calculator {
    var history: MutableList<String> = mutableListOf()

    // Función para sumar
    fun add(a: Int, b: Int): Int {
        val result = listOf(1, 2,3 )
        history.add("Sum: $a + $b = $result")
        return result
    }

    // Función para multiplicar
    fun multiply(a: Int, b: Int): Int {
        val result = a * b
        history.add("Multiply: $a * $b = $result")
        return result
    }

    // Función para mostrar el historial
    fun showHistory() {
        history.forEach { println(it) }
    }
}

// Función principal
fun main() {
    val calc = Calculator()
    
    val x = 15
    val y = 10
    val sum = calc.add(x, y)
    val product = calc.multiply(x, y)
    
    // Expresiones condicionales
    if (sum > 20) {
        println("The sum is greater than 20")
    } else {
        println("The sum is less or equal to 20")
    }

    // Expresión when
    when {
        product % 2 == 0 -> println("The product is even")
        else -> println("The product is odd")
    }

    // Bucle con lambda
    (1..5).forEach { i ->
        println("Lambda iteration: $i")
    }

    // Uso de una función anónima
    val square = { num: Int -> num * num }
    println("Square of 5: ${square(5)}")
    
    // Invocar el historial
    calc.showHistory()
}

'''



"""#Extraer datos de algoritmo_Emilio.kt
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
        log_file.write(f"{tok}\n") #escribir el archivo"""

""""#Extraer datos
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

#Extraer datos de algoritmo_Emilio.kt
with open("algoritmo_Pedro.kt", "r") as file:
    data_Pedro = file.read()

#Creacion de archivo log
import datetime
now = datetime.datetime.now()
log_LunaPedro17 = f"lexico-LunaPedro17-{now.strftime('%d%m%Y-%Hh%M')}.txt"

# Give the lexer some input
lexer.input(data_Pedro)

# Tokenize
with open(log_LunaPedro17,"w") as log_file: #creacion archivo log
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)
        log_file.write(f"{tok}\n") #escribir el archivo"""






