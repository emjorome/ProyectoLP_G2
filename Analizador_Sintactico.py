import ply.yacc as yacc
import datetime

# Get the token map from the lexer.  This is required.
from Analizador_Lexico import tokens

# APORTE DE EMILIO ROMERO
def p_programa(p):
    '''programa : sentencias '''

def p_sentencias(p):
    '''sentencias : sentencia
                | sentencias sentencia'''
    
def p_sentencia(p):
    '''sentencia : asignacion 
                | impresion
                | impresion_vacia
                | solicitud
                | expresion
                | condicion
                | estructura_lista
                | declaracion_variable''' #-----------------'''
    
#declaracion de variables -----------Aporte kQ
def p_declaracion_variable(p):
    """declaracion_variable : VAL VARIABLE ASIGN valor
                | VAR VARIABLE ASIGN valor
                """   
#--------------------------------------- 

def p_asignacion(p):
    '''asignacion : VARIABLE ASIGN VARIABLE
                    | VARIABLE ASIGN expresion
                    | VARIABLE ASIGN condicion
                    | VARIABLE ASIGN estructura_lista''' #---------agrega la estructura de lista
#Inicia aporte Pedro Luna
def p_impresionVacia(p):
    'impresion_vacia : PRINT LPAREN RPAREN'

def p_impresion(p):
    'impresion : PRINT LPAREN repiteValores RPAREN'

def p_valor(p):
  '''valor : NUMBER
          | FLOAT
          | VARIABLE
         | estructura_lista'''

def p_valor_bol(p):
  '''valor : TRUE
          | FALSE'''

def p_repiteValores(p):
  '''repiteValores : valor COMMA repiteValores
                  | valor'''

def p_solicitud(p):
    'solicitud : INPUT LPAREN DOUBLE_QUOTA DOUBLE_QUOTA RPAREN'


#Termina Aporte Pedro Luna


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
                | FLOAT
                | TRUE
                | FALSE
                | condicion"""

def p_expresionVariable(p):
    """expresion : VARIABLE"""

def p_condicionComparacion(p):
    """condicion : expresion GREATER expresion 
    | expresion LESS expresion 
    | expresion GREATER_EQUALS expresion 
    | expresion LESS_EQUALS expresion 
    | expresion EQUALS expresion 
    | expresion NOT_EQUALS expresion"""

def p_condicionLogica(p):
    """condicion : condicion AND condicion 
                | condicion OR condicion"""

def p_condicinNegacion(p):
    """condicion : NOT condicion
                | NOT expresion"""

def p_condicionParentecis(p):
    """condicion : LPAREN condicion RPAREN"""
#FIN DE APORTE DE EMILIO ROMERO

#Aporte kevin Quintuña-----------
#reglas para la listas
def p_elementos_lista(p):
    """elementos_lista : valor COMMA elementos_lista
                       | valor"""


def p_estructura_lista(p):
    """estructura_lista : LISTOF LPAREN elementos_lista RPAREN
                  | MUTABLELISTOF LPAREN elementos_lista RPAREN"""

#reglas para mapas
def p_estructura_mapa(p):
    """estructura_mapa : MAPOF LPAREN pareskv_mapa RPAREN
                  | MUTABLEMAPOF LPAREN pareskv_mapa RPAREN"""


def p_pareskv_mapa(p):
    """pareskv_mapa : clave TO_FROM_KV valor COMMA pareskv_mapa
                    | clave TO_FROM_KV valor"""

# reglas para conjuntos
def p_clave(p):
    """clave : valor"""

def p_estructura_conjunto(p):
    """estructura_conjunto : MUTABLESETOF LPAREN elementos_lista RPAREN"""



#Guardar datos
#Guardar datos
now = datetime.datetime.now()
usuario = "LunaPedro17"
log_filename = f"logsSintacticos/sintactico-{usuario}-{now.strftime('%d%m%Y-%Hh%M')}.txt"

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
   mensaje = f"Entrada: {s}\nResultado: {result}\n"

   print(result)
   print(mensaje)
   guardar_log(mensaje)