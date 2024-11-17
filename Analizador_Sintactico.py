import ply.yacc as yacc
import datetime

# Get the token map from the lexer.  This is required.
from Analizador_Lexico import tokens

def p_programa(p):
    '''programa : sentencias 
                | programa'''
    
def p_sentencias(p):
    '''sentencia : asignacion 
                | impresion
                |impresion_vacia
                | funcion 
                | comparacionNumero 
                | comparacionBool'''

def p_impresionVacia(p):
    'impresion_vacia: PRINT RPAREN LPAREN'

def p_impresion(p):
    'impresion: PRINT RPAREN repiteValores LPAREN'

def p_valor(p):
  '''valor : ENTERO
          | FLOTANTE
          | VARIABLE'''
def p_valor_bol(p):
  '''valor : VERDADERO
          | FALSO'''

def p_repiteValores(p):
  '''repiteValores : valor COMA repiteValores
                  | valor'''

#Guardar datos
now = datetime.datetime.now()
usuario = "emjorome"
log_filename = f"sintactico-{usuario}-{now.strftime('%d%m%Y-%Hh%M')}.txt"

def guardar_log(mensaje):
    """Escribe un mensaje en el archivo de log."""
    with open(log_filename, 'a') as log_file:
        log_file.write(mensaje + '\n')

# Error rule for syntax errors
def p_error(p):
    msg_error = "Error de sintaxis en la linea %d!" % p.lineno
    print(msg_error)
    guardar_log(msg_error)

# Build the parser
parser = yacc.yacc()

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