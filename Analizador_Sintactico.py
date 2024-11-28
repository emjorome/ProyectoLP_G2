import ply.yacc as yacc
import datetime

resultados_sintactico = []
validar_sintaxis = True

# Get the token map from the lexer.  This is required.
from Analizador_Lexico import tokens

# Inicio del programa ----------- APORTE DE EMILIO ROMERO 
def p_programa(p):
    '''programa : sentencias '''
# sentencias
def p_sentencias(p):
    '''sentencias : sentencia
                | sentencias sentencia'''
# fin de aporte ----------------- Aporte de EMILIO ROMERO

#declaracion de variables -----------Aporte kEVIN Quintuña

def p_empty(p):
    '''empty :'''
    pass
#Aporte Pedro Luna 11/26
#Agregar todas las variables y estructuras declaradas y creadas
variables = {}
estructuras = {}
#Final Aporte Pedro Luna

def p_sentencia(p):
    '''sentencia : asignacion 
                 | impresion
                 | impresion_vacia
                 | expresion
                 | condicion
                 | estructura
                 | declaracion_variable
                 | funcion
                 | empty 
                 | retorno
                 | clase
                 | constructorPri'''   
    
#declaracion de variables -----------Aporte kQ
def p_declaracion_variable(p):
    '''declaracion_variable : VAL VARIABLE ASIGN valor
                            | VAR VARIABLE ASIGN valor
                            | VAL VARIABLE ASIGN estructura
                            | VAR VARIABLE ASIGN estructura
                            | VAL VARIABLE ASIGN creacionObjeto
                            | VAR VARIABLE ASIGN creacionObjeto'''
    # Aporte Pedro Luna 11/26
    # Guardar variable en el diccionario
    if p[1] == 'VAL' or p[1] == 'VAR':
        variables[p[2]] = p[4]  # Asignar valor o estructura a la variable
    # Final Aporte Pedro Luna
#--------------------------------------- Aporte kEVIN Quintuña

def p_asignacion(p):
    '''asignacion : VARIABLE ASIGN VARIABLE
                    | VARIABLE ASIGN expresion
                    | VARIABLE ASIGN condicion
                    | VARIABLE ASIGN estructura
                    | VARIABLE ASIGN creacionObjeto''' #---------agrega la estructura de lista
    #Aporte Pedro Luna 11/26
    # Comprobamos que la variable está declarada
    if p[1] not in variables:
        mensaje = f"Error semántico: La variable {p[1]} no ha sido declarada."
        #guardar_log(mensaje)
        print(mensaje)
        return

    # Si la asignación es con otra variable, verificamos que ambas tengan el mismo tipo
    if isinstance(p[3], str) and p[3] in variables:
        if type(variables[p[1]]) != type(variables[p[3]]):
            mensaje = f"Error semántico: Incompatibilidad de tipos entre {p[1]} y {p[3]}."
            #guardar_log(mensaje)
            print(mensaje)
            return
        variables[p[1]] = variables[p[3]]

    # Si la asignación es con una expresión o estructura, verificamos que el tipo sea compatible
    if isinstance(p[3], (int, float, str, bool)):
        variables[p[1]] = p[3]
#Final Aporte Pedro Luna

#Inicia aporte Pedro Luna
def p_impresionVacia(p):
    'impresion_vacia : PRINT LPAREN RPAREN'

def p_impresion(p):
    'impresion : PRINT LPAREN repiteValores RPAREN'

def p_valor(p):
  '''valor : NUMBER
          | FLOAT
          | VARIABLE
        | STRING'''

def p_valor_bol(p):
  '''valor : TRUE
          | FALSE'''

def p_repiteValores(p):
  '''repiteValores : valor COMMA repiteValores
                  | valor'''

def p_solicitud(p):
    'solicitud : INPUT LPAREN DOUBLE_QUOTA DOUBLE_QUOTA RPAREN'


#Termina Aporte Pedro Luna

#Funcion para armar aritmetica --------------  APORTE DE EMILIO ROMERO
def p_expresionAritmetica(p):
    """expresion : expresion PLUS expresion 
                | expresion MINUS expresion
                | expresion TIMES expresion 
                | expresion DIVIDE expresion
                | expresion MOD expresion"""
    # Aporte Pedro Luna 11/26
    # Verificar si las variables están declaradas
    if isinstance(p[1], str) and p[1] not in variables:
        print(f"Error semántico: La variable {p[1]} no ha sido inicializada.")
        return
    if isinstance(p[3], str) and p[3] not in variables:
        print(f"Error semántico: La variable {p[3]} no ha sido inicializada.")
        return

    # Validar que los tipos de las variables sean compatibles para la operación
    valor1 = variables[p[1]] if isinstance(p[1], str) else p[1]
    valor3 = variables[p[3]] if isinstance(p[3], str) else p[3]
    if type(valor1) != type(valor3):
        print(f"Error semántico: Los tipos de {p[1]} y {p[3]} son incompatibles para la operación.")
        return
    # Final Aporte Pedro Luna

#Funcion que permite a una expresion estar en parentesis
def p_expresionParentesis(p):
    """expresion : LPAREN expresion RPAREN"""

#Funcion que señala que valores puede tomar la expresion
def p_expresionConstante(p):
    """expresion : NUMBER
                | FLOAT
                | TRUE
                | FALSE
                | condicion"""

#Funcion si la expresion esta en una variable
def p_expresionVariable(p):
    """expresion : VARIABLE"""
    # Aporte Pedro Luna 11/26
    if p[1] not in variables:
        mensaje = f"Error semántico: La variable {p[1]} no ha sido declarada."
        #guardar_log(mensaje)
        print(mensaje)
        return
    #Final Aporte Pedro Luna

#Funcion que permite como es la estructura de una condicion
def p_condicionComparacion(p):
    """condicion : expresion GREATER expresion 
    | expresion LESS expresion 
    | expresion GREATER_EQUALS expresion 
    | expresion LESS_EQUALS expresion 
    | expresion EQUALS expresion 
    | expresion NOT_EQUALS expresion"""

#Funcion con condicionales logicos
def p_condicionLogica(p):
    """condicion : condicion AND condicion 
                | condicion OR condicion"""

#Funcion con condicional not
def p_condicinNegacion(p):
    """condicion : NOT condicion
                | NOT expresion"""

#Funcion que permite que una condicion este entre parentesis
def p_condicionParentecis(p):
    """condicion : LPAREN condicion RPAREN"""

#------------------------------------------------FIN DE APORTE DE EMILIO ROMERO

#Aporte kevin Quintuña-----------
#reglas para la listas

# Listas
def p_estructura_lista(p):
    '''estructura : LISTOF LPAREN repiteValores RPAREN
                  | LISTOF LPAREN RPAREN
                  | MUTABLELISTOF LPAREN repiteValores RPAREN
                  | MUTABLELISTOF LPAREN RPAREN'''
    estructuras[p[1]] = p[3]  # Guardar la lista en la estructura


# Mapas
def p_estructura_mapa(p):
    '''estructura : MAPOF LPAREN pareskv_mapa RPAREN
                  | MUTABLEMAPOF LPAREN pareskv_mapa RPAREN'''

def p_pares_kv_mapa(p):
    '''pareskv_mapa : valor TO_FROM_KV valor COMMA pareskv_mapa
                    | valor TO_FROM_KV valor'''

# Conjuntos
def p_estructura_conjunto(p):
    '''estructura : SETOF LPAREN repiteValores RPAREN
                  | SETOF LPAREN RPAREN
                  | MUTABLESETOF LPAREN repiteValores RPAREN
                  | MUTABLESETOF LPAREN RPAREN'''

# Manejo de errores
"""def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}' (tipo: {p.type}, línea: {p.lineno}, posición: {p.lexpos})")
    else:
        print("Error de sintaxis: Fin inesperado de entrada")
"""
#Funcion que reconoce los tipos de datos -------- APORTE DE EMILIO ROMERO
"""def p_tipoDato(p):
    '''tipoDato : INT 
                | BOOLEAN
                | LONG
                | DOUBLE
                | CHAR
                | BYTE''' """

#Funcion que almacena la estructura del retorno    
def p_retorno(p):
    '''retorno : RETURN objetoRetorno'''

#Funcion que devuelve los retornos posibles
def p_objetoRetorno(p):
    '''objetoRetorno : valor
                    | condicion
                    | expresion
                    | TRUE
                    | FALSE
                    | estructura
                    | empty'''

#----------------- ----------------------------FIN APORTE DE EMILIO ROMERO

# ESTRUCTURAS DE CONTROL
def p_estructura_control_for(p):
    '''estructura : FOR LPAREN VARIABLE IN valor RANGE_TO valor RPAREN LLLAVE sentencias RLLAVE'''

def p_estructura_control_while(p): # --------APORTE DE EMILIO ROMERO
    '''estructura : WHILE condicion LLLAVE sentencias RLLAVE'''

# DECLARACION DE TIPOS DE FUNCIONES
# Declaración de funciones

# Parámetros de funciones
def p_parametros(p):
    '''parametros : VARIABLE COLON VARIABLE ASIGN valor COMMA parametros
                  | VARIABLE COLON VARIABLE ASIGN valor
                  | VARIABLE COLON VARIABLE COMMA parametros
                  | VARIABLE COLON VARIABLE
                  | empty'''
    
def p_funcion(p):
    '''funcion : FUN VARIABLE LPAREN parametros RPAREN COLON VARIABLE LLLAVE sentencias RLLAVE
               | FUN VARIABLE LPAREN parametros RPAREN LLLAVE empty RLLAVE
               | FUN VARIABLE LPAREN parametros RPAREN COLON VARIABLE ASIGN sentencias'''

#TEMRMINA Aporte kevin Quintuña-----------

#Clases y Herencia -------------------- APORTE DE EMILIO ROMERO
def p_repetirThis(p):
    '''repetirThis : THIS DOT VARIABLE ASIGN valor repetirThis
                | THIS DOT VARIABLE ASIGN valor'''

def p_formarThis(p):
    '''formarThis : THIS LPAREN repiteValores RPAREN'''

def p_repetir_declaracion_variable(p):
    '''repetirDeclaracion : declaracion_variable repetirDeclaracion
                        | declaracion_variable'''
    
def p_creacionObjeto(p):
    '''creacionObjeto : VARIABLE LPAREN RPAREN
                    | VARIABLE LPAREN repiteValores RPAREN'''

def p_clase(p):
    '''clase : CLASS VARIABLE LLLAVE sentencias RLLAVE
            | CLASS VARIABLE LLLAVE RLLAVE
            | OPEN CLASS VARIABLE LLLAVE sentencias RLLAVE
            | OPEN CLASS VARIABLE LLLAVE RLLAVE
            | CLASS VARIABLE COLON VARIABLE LPAREN RPAREN LLLAVE sentencias RLLAVE
            | CLASS VARIABLE COLON VARIABLE LPAREN RPAREN LLLAVE RLLAVE'''
    
def p_constructorPri(p):
    '''constructorPri : CLASS VARIABLE LPAREN parametros RPAREN LLLAVE repetirDeclaracion RLLAVE
                    | CLASS VARIABLE LPAREN parametros RPAREN LLLAVE RLLAVE
                    | CLASS VARIABLE LPAREN parametros RPAREN LLLAVE repetirDeclaracion constructorSec RLLAVE'''
    
def p_constructorSecundario(p):
    '''constructorSec : CONSTRUCTOR LPAREN parametros RPAREN COLON formarThis LLLAVE repetirThis RLLAVE
                    | CONSTRUCTOR LPAREN parametros RPAREN COLON LLLAVE repetirThis RLLAVE
                    | CONSTRUCTOR LPAREN parametros RPAREN COLON formarThis LLLAVE RLLAVE
                    | CONSTRUCTOR LPAREN parametros RPAREN COLON LLLAVE RLLAVE'''

#------------------------------- FIN APORTE DE EMILIO ROMERO

#Guardar datos
#Guardar datos
now = datetime.datetime.now()
usuario = "LunaPedro17"
log_filename = f"logsSintacticos/sintactico-{usuario}-{now.strftime('%d%m%Y-%Hh%M')}.txt"

def guardar_log(mensaje):
    with open(log_filename, 'a') as log_file:
        log_file.write(mensaje + '\n')

# Error rule for syntax errors
#def p_error(p):
#   msg_error = "Error de sintaxis en la linea %d!" % p.lineno
#   print(msg_error)
#   guardar_log(msg_error)

# Guardar datos
import datetime  # Asegúrate de importar este módulo si aún no lo has hecho
now = datetime.datetime.now()
#usuario = "Kevin-QQ-82"
usuario = "emjorome"

log_filename = f"logsSintacticos/sintactico-{usuario}-{now.strftime('%d%m%Y-%Hh%M')}.txt"

def guardar_log(mensaje):
    with open(log_filename, 'a') as log_file:
        log_file.write(mensaje + '\n')

def p_error(p):
    if p:
        msg_error = f"Error de sintaxis en el token '{p.value}' (línea {p.lineno}, posición {p.lexpos})"
    else:
        msg_error = "Error de sintaxis: Fin inesperado de entrada"
    #guardar_log(msg_error)
    resultados_sintactico.append(msg_error)
    global validar_sintaxis
    validar_sintaxis = False
    print(msg_error)

# Build the parser
parser = yacc.yacc(debug=True)

"""while True:
   try:
       s = input('kotlin > ')
   except EOFError:
       break
   if not s: continue

   result = parser.parse(s)
   mensaje = f"Entrada: {s}\nResultado: {result}\n"

   print(result)
   guardar_log(mensaje)"""

def vaciar_resultados_sintactios():
    resultados_sintactico.clear()

def analizar_sintaxis(codigo):
    global validar_sintaxis
    validar_sintaxis = True

    #while True:
    """try:
        s = codigo
    except EOFError:
        break
    if not s: continue"""
    s = codigo
    result = parser.parse(s)
    mensaje = f"Entrada: {s}\nResultado: {result}\n"

    if validar_sintaxis:
        resultados_sintactico.append(mensaje)
    print(mensaje)

    return resultados_sintactico
