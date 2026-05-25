import os
import json

def md_cell(text):
    lines = [line + "\n" for line in text.split('\n')]
    if lines and lines[-1] == "\n": lines = lines[:-1]
    return {"cell_type": "markdown", "metadata": {}, "source": lines}

def code_cell(code):
    lines = [line + "\n" for line in code.split('\n')]
    if lines and lines[-1] == "\n": lines = lines[:-1]
    return {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": lines}

def save_notebook(filepath, title, cells):
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    colab_link = f'<a href="https://colab.research.google.com/github/YOUR_USERNAME_AQUI/masteryInPython/blob/main/{filepath}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>\n\n'
    header_cell = md_cell(colab_link + f"# {title}")
    notebook = {
        "cells": [header_cell] + cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.8.10"}
        },
        "nbformat": 4, "nbformat_minor": 4
    }
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

def gen_mod7():
    save_notebook("modulo_7/01_ejercicios_integrales.ipynb", "Módulo 7: Práctica Integral", [
        md_cell("## 🎯 Retos Integrales\nEste módulo está dedicado 100% a la práctica. Los siguientes ejercicios combinan múltiples conceptos del lenguaje (estructuras de datos, bucles, manejo de errores y funciones) y están ordenados de menor a mayor dificultad."),
        md_cell("### Nivel 1: El Validador de Nombres\n**Conceptos:** Strings, Condicionales, Bucles, Listas.\n\nEscribe una función `limpiar_nombres(lista)` que reciba una lista de strings.\n- Debe descartar los nombres que tengan menos de 3 letras.\n- Debe descartar los nombres que contengan números (pista: investiga el método `.isalpha()`).\n- Debe retornar una nueva lista con los nombres válidos, todos convertidos a MAYÚSCULAS.\n\nPrueba con: `['Ana', 'Lu1s', 'Jo', 'Maria', 'Pedro9']`"),
        code_cell('# Escribe tu código aquí\n'),
        md_cell("### Nivel 2: Analizador de Texto\n**Conceptos:** Strings, Diccionarios, Bucles.\n\nTienes el siguiente párrafo:\n`\"Python es genial. Python es fácil. Aprender Python es divertido!\"`\n\nEscribe un código que:\n1. Elimine los puntos y signos de exclamación.\n2. Convierta todo a minúsculas.\n3. Cuente cuántas veces aparece cada palabra y guarde el resultado en un diccionario.\n\n*El resultado debería ser algo como: `{'python': 3, 'es': 3, 'genial': 1, 'fácil': 1, ...}`*"),
        code_cell('texto = "Python es genial. Python es fácil. Aprender Python es divertido!"\n# Escribe tu código aquí\n'),
        md_cell("### Nivel 3: Gestión de Inventario Inteligente\n**Conceptos:** Diccionarios anidados, Funciones, Manejo de Errores.\n\nCrea un sistema de inventario donde el diccionario principal tenga el nombre del producto como clave, y como valor otro diccionario con el `precio` y el `stock`.\n\nCrea dos funciones:\n1. `agregar_stock(producto, cantidad)`: Suma la cantidad al stock del producto.\n2. `vender(producto, cantidad)`: Resta la cantidad. Si la cantidad solicitada es mayor al stock, debe **lanzar una excepción** (usando `raise ValueError(...)`) advirtiendo que no hay stock suficiente.\n\nPrueba ambas funciones usando un bloque `try/except` para capturar la venta fallida."),
        code_cell('inventario = {\n    "manzanas": {"precio": 1.5, "stock": 50},\n    "peras": {"precio": 2.0, "stock": 20}\n}\n# Escribe tu código aquí\n'),
        md_cell("### Nivel 4: Cifrado César\n**Conceptos:** Strings, Matemáticas, Bucles, Funciones.\n\nEl Cifrado César es una técnica de encriptación antigua donde cada letra se desplaza un número determinado de posiciones en el alfabeto.\nEscribe una función `cifrar(texto, desplazamiento)` que desplace las letras.\n\n*Pista: Puedes usar las funciones integradas `ord(letra)` (que te da el número ASCII de la letra) y `chr(numero)` (que convierte el número de vuelta a letra).* Para simplificar, asume que no nos importan los límites del abecedario (z -> a), solo suma el desplazamiento."),
        code_cell('# Escribe tu código aquí\n'),
        md_cell("### Nivel 5: Simulador Bancario con Log de Operaciones\n**Conceptos:** Todo (While, Funciones, Manejo de Archivos, Errores).\n\nEscribe un programa de consola que se ejecute en un bucle `while True` mostrando un menú:\n1. Depositar\n2. Retirar\n3. Ver Saldo\n4. Salir\n\nReglas:\n- Si el usuario ingresa una letra en lugar de un monto, atrapa el `ValueError` y dile que ingrese un número válido.\n- Cada vez que ocurra un depósito o retiro exitoso, escribe una línea en un archivo de texto `historial.txt` con la operación (ej. `'Depósito de $100 exitoso'`).\n- El bucle termina cuando elige Salir."),
        code_cell('# Escribe tu código aquí\n')
    ])

if __name__ == "__main__":
    gen_mod7()
    print("Módulo 7 generado")
