import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from Analizador_Lexico import tokens

def p_programa(p):
    '''programa : sentencias 
                | programa'''
    
def p_sentencias(p):
    '''sentencia : asignacion 
                | impresion 
                | funcion 
                | comparacionNumero 
                | comparacionBool'''

# Error rule for syntax errors
def p_error(p):
    print("Error de sintaxis en la linea %d!" % p.lineno)

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)