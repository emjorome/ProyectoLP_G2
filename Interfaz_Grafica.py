#import Analizador_Lexico as a_l
#import Analizador_Sintactico as a_s
import tkinter as tk
from tkinter import ttk

def analizar_codigo():
    """Simula el análisis del código y muestra resultados en la pantalla derecha."""
    codigo = entrada_codigo.get("1.0", tk.END)  # Obtener el texto ingresado
    if not codigo.strip():
        salida_resultados.insert(tk.END, "Error: No se ingresó código.\n")
        return
    
    # Aquí integrar el analizador léxico, sintáctico y semántico. ----PENDIENTE
    salida_resultados.delete("1.0", tk.END)  # Limpia resultados anteriores
    salida_resultados.insert(tk.END, "Análisis completado:\n")
    salida_resultados.insert(tk.END, "✓ Léxico: Sin errores.\n")
    salida_resultados.insert(tk.END, "✓ Sintáctico: Sin errores.\n")
    salida_resultados.insert(tk.END, "✓ Semántico: Sin errores.\n")


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
label_izquierdo = ttk.Label(frame_izquierdo, text="Código Kotlin", background="grey")
label_izquierdo.pack(anchor="nw", padx=5, pady=5)

entrada_codigo = tk.Text(frame_izquierdo, wrap=tk.WORD, background = "black", foreground="white")
entrada_codigo.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Área de salida (derecha)
label_derecho = ttk.Label(frame_derecho, text="Resultados del Análisis", background="grey")
label_derecho.pack(anchor="nw", padx=5, pady=5)

salida_resultados = tk.Text(frame_derecho, wrap=tk.WORD, state=tk.NORMAL, background= "black", foreground="white")
salida_resultados.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Botón de análisis
boton_analizar = ttk.Button(root, text="Analizar Código", command=analizar_codigo)
boton_analizar.pack(pady=10)

# Iniciar el loop principal de la interfaz
root.mainloop()
