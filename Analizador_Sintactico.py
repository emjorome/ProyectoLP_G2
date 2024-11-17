import ply.yacc as yacc
import datetime

# Get the token map from the lexer.  This is required.
from Analizador_Lexico import tokens

def p_programa(p):
    '''programa : sentencias '''

def p_sentencias(p):
    '''sentencias : sentencia
                | sentencias sentencia'''
    
def p_sentencia(p):
    '''sentencia : asignacion 
                | impresion
                | impresion_vacia
                | expresion
                | condicion'''

def p_asignacion(p):
    '''asignacion : VARIABLE ASIGN VARIABLE'''

def p_impresionVacia(p):
    'impresion_vacia : PRINT RPAREN LPAREN'

def p_impresion(p):
    'impresion : PRINT RPAREN repiteValores LPAREN'

def p_valor(p):
  '''valor : NUMBER
          | FLOAT
          | VARIABLE'''
def p_valor_bol(p):
  '''valor : TRUE
          | FALSE'''

def p_repiteValores(p):
  '''repiteValores : valor COMMA repiteValores
                  | valor'''

def p_expresionAritmetica(p):
    """expresion : expresion PLUS expresion 
    | expresion MINUS expresion
    | expresion TIMES expresion 
    | expresion DIVIDE expresion
    | expresion MOD expresion"""

def p_expresionParentesis(p):
    """expresion : LPAREN expresion RPAREN"""

def p_expresionConstante(p):
    """expresion : NUMBER
                | FLOAT"""

def p_expresionVariable(p):
    """expresion : VARIABLE"""

def p_condicionComparacion(p):
    """condicion : expresion GREATER expresion 
    | expresion LESS expresion 
    | expresion GREATER_EQUALS expresion 
    | expresion LESS_EQUALS expresion 
    | expresion EQUALS expresion 
    | expresion NOT_EQUALS"""

def p_condicionLogica(p):
    """condicion : condicion AND condicion 
                | condicion OR condicion"""

def p_condicinNegacion(p):
    """condicion : NOT condicion"""

def p_condicionParentecis(p):
    """condicion : LPAREN condicion RPAREN"""

#Guardar datos
now = datetime.datetime.now()
usuario = "emjorome"
log_filename = f"sintactico-{usuario}-{now.strftime('%d%m%Y-%Hh%M')}.txt"

def guardar_log(mensaje):
    with open(log_filename, 'a') as log_file:
        log_file.write(mensaje + '\n')

# Error rule for syntax errors
def p_error(p):
    msg_error = "Error de sintaxis en la linea %d!" % p.lineno
    print(msg_error)
    guardar_log(msg_error)

# Build the parser
parser = yacc.yacc(debug=True)

while True:
   try:
       s = input('kotlin > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)

   if result:
        mensaje = f"Entrada: {s}\nResultado: Correcto\n"

   print(result)
   guardar_log(mensaje)