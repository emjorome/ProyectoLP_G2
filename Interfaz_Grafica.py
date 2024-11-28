import Analizador_Lexico as a_l
import Analizador_Sintactico as a_s
import tkinter as tk
from tkinter import ttk

from Analizador_Sintactico import resultados_semantico


def analizar_codigo():
    """Simula el análisis del código y muestra resultados en la pantalla derecha."""
    codigo = entrada_codigo.get("1.0", tk.END)  # Obtener el texto ingresado
    if not codigo.strip():
        salida_resultados.insert(tk.END, "Error: No se ingresó código.\n")
        return
    
    #Borrar resultados anteriores de la pantalla
    salida_resultados.delete("1.0", tk.END)  # Limpia resultados anteriores

    #ANALIZADOR LEXICO
    #Se extraen los resultados del analizador lexico
    resultados_lexicos = a_l.analizar_lexico(codigo.strip())

    # Muestra los resultados en la pantalla
    if resultados_lexicos:
        salida_resultados.insert(tk.END, "Resultados del análisis léxico:\n")
        for resultado in resultados_lexicos:
            salida_resultados.insert(tk.END, resultado + "\n")
    else:
        salida_resultados.insert(tk.END, "No se encontraron tokens.\n")
        return

    a_l.vaciar_resultados()

    if a_l.validar_lexico:
        salida_resultados.insert(tk.END, "✓ Léxico: Sin errores.\n\n")
    else:
        salida_resultados.insert(tk.END, "ERROR en el léxico, por favor verifique.\n")
        return

    #ANALIZADOR SINTACTICO
    # Se extraen los resultados del analizador sintactico y semanticos
    resultados_sintacticos = a_s.analizar_sintaxis(codigo.strip())
    resultados_semanticos = a_s.resultados_semantico

    # Muestra los resultados en la pantalla
    if resultados_sintacticos:
        salida_resultados.insert(tk.END, "Resultados del análisis sintáctico:\n")
        for resultado in resultados_sintacticos:
            salida_resultados.insert(tk.END, resultado + "\n")
    else:
        salida_resultados.insert(tk.END, "Error en el compilador. No se encuentra sintaxis.\n")
        return

    a_s.vaciar_resultados_sintactios()

    if a_s.validar_sintaxis:
        salida_resultados.insert(tk.END, "✓ Sintáctico: Sin errores.\n\n")
    else:
        salida_resultados.insert(tk.END, "ERROR en la sintaxis, por favor verifique.\n")
        return

    #ANALIZADOR SEMANTICO
    if resultados_semanticos:
        for resultado in resultados_semanticos:
            salida_resultados.insert(tk.END, resultado + "\n")
        salida_resultados.insert(tk.END, "ERROR en la semántica, por favor verifique.\n")
        a_s.vaciar_resultados_semanticos()
        return
    else:
        salida_resultados.insert(tk.END, "Resultado del análisis semántico:\n")
        salida_resultados.insert(tk.END, "✓ Semántico: Sin errores.\n\n")

    a_s.vaciar_resultados_semanticos()

    # Mensaje de verificacion exitosa
    salida_resultados.insert(tk.END, "Análisis completado.\n")
    salida_resultados.insert(tk.END, "TODO CORRECTO\n")


# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz del Analizador de Código Kotlin")
root.geometry("800x600")
root.config(bg="black")

# Crear un frame principal para dividir las áreas
frame_principal = ttk.Frame(root)
frame_principal.pack(fill=tk.BOTH, expand=True)

# Crear dos subframes para las áreas izquierda y derecha
frame_izquierdo = ttk.Frame(frame_principal, width=400)
frame_derecho = ttk.Frame(frame_principal, width=400)
frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)

# Área de entrada (izquierda)
label_izquierdo = ttk.Label(frame_izquierdo, text="Código Kotlin", background="black", foreground="white")
label_izquierdo.pack(anchor="nw", padx=5, pady=5)

entrada_codigo = tk.Text(frame_izquierdo, wrap=tk.WORD, background = "black", foreground="white")
entrada_codigo.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Área de salida (derecha)
label_derecho = ttk.Label(frame_derecho, text="Resultados del Análisis", background="black", foreground="white")
label_derecho.pack(anchor="nw", padx=5, pady=5)

salida_resultados = tk.Text(frame_derecho, wrap=tk.WORD, state=tk.NORMAL, background= "black", foreground="white")
salida_resultados.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Botón de análisis
boton_analizar = ttk.Button(root, text="Analizar Código", command=analizar_codigo)
boton_analizar.pack(pady=10)

# Iniciar el loop principal de la interfaz
root.mainloop()
