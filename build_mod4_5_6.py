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

def gen_mod4():
    save_notebook("modulo_4/01_funciones_y_lambdas.ipynb", "Funciones y Lambdas", [
        md_cell("## 1. Funciones Básicas\nLas funciones son bloques de código reutilizables. Te ahorran escribir lo mismo una y otra vez. Se definen con la palabra `def`."),
        code_cell('def saludar(nombre):\n    return f"¡Hola {nombre}, bienvenido!"\n\n# Usando la función\nmensaje = saludar("Leo")\nprint(mensaje)'),
        md_cell("## 2. Argumentos por Defecto\nPuedes darle a las funciones valores por defecto, por si el usuario olvida pasarlos."),
        code_cell('def hacer_cafe(tipo="Americano"):\n    print(f"Preparando un rico {tipo} ☕")\n\nhacer_cafe()            # Usa el default\nhacer_cafe("Espresso")  # Lo sobreescribe'),
        md_cell("## 3. Funciones Lambda\nSon funciones anónimas (sin nombre) y de una sola línea. Se usan para operaciones matemáticas rápidas o para ordenar listas."),
        code_cell('doble = lambda x: x * 2\nprint("El doble de 5 es:", doble(5))\n\n# Muy útil para ordenar listas de diccionarios\nusuarios = [{"nombre": "Ana", "edad": 30}, {"nombre": "Leo", "edad": 25}]\nusuarios_ordenados = sorted(usuarios, key=lambda u: u["edad"])\nprint("Ordenados por edad:", usuarios_ordenados)'),
        md_cell("## 🎯 Tu Turno\nCrea una función llamada `es_mayor_de_edad` que reciba un número (edad) y retorne `True` si es >= 18 y `False` si es menor.")
    ])
    save_notebook("modulo_4/02_modulos_y_paquetes.ipynb", "Módulos y Paquetes", [
        md_cell("## 1. Importando Módulos\nNo tienes que reinventar la rueda. Python viene con 'módulos' (archivos con código pre-hecho) listos para usar."),
        code_cell('import math\nimport random\n\nprint("Valor de Pi:", math.pi)\nprint("Número aleatorio entre 1 y 10:", random.randint(1, 10))'),
        md_cell("## 2. Creando tus Propios Módulos\nEn un proyecto real, divides tu código en varios archivos `.py`. En Jupyter/Colab esto es menos común, pero la idea es simple: si tienes un archivo `mates.py` con una función `sumar()`, puedes usar `from mates import sumar` en otro archivo."),
        md_cell("## 🎯 Tu Turno\nImporta el módulo `datetime`. Úsalo para imprimir la fecha y hora actual usando `datetime.datetime.now()`.")
    ])
    save_notebook("modulo_4/03_ejercicios_refuerzo.ipynb", "Ejercicios de Refuerzo Módulo 4", [
        md_cell("## 🧠 Ejercicios de Refuerzo: Módulo 4\n\n### Ejercicio 1: Calculadora Modular\nCrea una función `calculadora(a, b, operacion)`.\nLa operación puede ser 'suma', 'resta', 'multiplicacion' o 'division'. Retorna el resultado correspondiente. Usa un `match` o múltiples `if` dentro de la función."),
        code_cell('# Tu código aquí\n')
    ])

def gen_mod5():
    save_notebook("modulo_5/01_manejo_de_errores.ipynb", "Manejo de Errores", [
        md_cell("## 1. Try / Except\nLos errores en programación (excepciones) detienen tu código abruptamente. Con `try` y `except` puedes atrapar esos errores y manejarlos con gracia."),
        code_cell('try:\n    resultado = 10 / 0\nexcept ZeroDivisionError:\n    print("¡Error! No puedes dividir entre cero.")\nexcept Exception as e:\n    print(f"Ocurrió un error inesperado: {e}")\nprint("El programa sigue funcionando...")'),
        md_cell("## 2. Finally\nEl bloque `finally` se ejecuta **siempre**, haya ocurrido un error o no. Es útil para cerrar archivos o conexiones a bases de datos."),
        code_cell('try:\n    numero = int("10")\n    print("El número es", numero)\nexcept ValueError:\n    print("Eso no es un número")\nfinally:\n    print("Operación de conversión terminada.")'),
        md_cell("## 🎯 Tu Turno\nCrea un `try/except` que intente acceder al índice 10 de la lista `[1, 2, 3]`. Atrapa el `IndexError` e imprime un mensaje amigable.")
    ])
    save_notebook("modulo_5/02_manejo_de_archivos.ipynb", "Lectura y Escritura de Archivos", [
        md_cell("## 1. Escribir Archivos\nUsamos la función `open()` con el modo `'w'` (write) para crear y escribir archivos. El bloque `with` asegura que el archivo se cierre automáticamente al terminar."),
        code_cell('with open("mi_diario.txt", "w") as archivo:\n    archivo.write("Día 1: Python es increíble.\\n")\n    archivo.write("Mañana aprenderé sobre APIs.")\nprint("Archivo creado con éxito.")'),
        md_cell("## 2. Leer Archivos\nUsamos el modo `'r'` (read) para leer el contenido."),
        code_cell('with open("mi_diario.txt", "r") as archivo:\n    contenido = archivo.read()\n    print("Contenido del archivo:\\n", contenido)'),
        md_cell("## 🎯 Tu Turno\nEscribe un archivo llamado `lista_compras.txt` que contenga 3 cosas que quieres comprar. Luego, lee el archivo e imprímelo línea por línea usando un bucle `for`.")
    ])
    save_notebook("modulo_5/03_ejercicios_refuerzo.ipynb", "Ejercicios de Refuerzo Módulo 5", [
        md_cell("## 🧠 Ejercicios de Refuerzo: Módulo 5\n\n### Ejercicio 1: Lector Seguro\nEscribe una función `leer_archivo(nombre_archivo)` que intente leer el contenido de un archivo usando `try`. Si el archivo no existe (error `FileNotFoundError`), debe retornar el mensaje 'El archivo no fue encontrado'.")
    ])

def gen_mod6():
    save_notebook("modulo_6/01_intro_apis_y_requests.ipynb", "Introducción a APIs y Requests", [
        md_cell("## 1. ¿Qué es una API?\nUna API (Application Programming Interface) es como un mesero en un restaurante. Tú (el cliente) le das tu orden al mesero (la API), este la lleva a la cocina (el servidor), y luego te trae la comida (los datos).\n\nEn Python, la librería más popular para ser el cliente es `requests`."),
        code_cell('import requests\n\n# Vamos a pedir datos a una API pública y gratuita\nrespuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")\n\nif respuesta.status_code == 200:\n    datos = respuesta.json()\n    print(f"Nombre: {datos[\'name\']}")\n    print(f"Peso: {datos[\'weight\']}")\nelse:\n    print("Error al conectar con la API")'),
        md_cell("## 🎯 Tu Turno\nUsa la API de Pokémon para buscar a 'charmander' e imprime su altura ('height').")
    ])
    save_notebook("modulo_6/02_proyecto_final_chatbot_ai.ipynb", "Proyecto Final: Chatbot AI", [
        md_cell("## 🚀 Proyecto Final: Chatbot con Gemini AI\nVamos a unir funciones, bucles `while`, manejo de errores (`try/except`) y llamadas a APIs para construir un asistente que hable contigo usando la API de Google Gemini.\n\n*Nota: Para que este código funcione, necesitarás generar tu propia API KEY gratuita en Google AI Studio (aistudio.google.com).*"),
        code_cell('import requests\n\n# 1. Configuración\nAPI_KEY = "PON_TU_API_KEY_AQUI"\nURL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"\n\ndef preguntar_a_gemini(texto):\n    # 2. Preparamos los datos en formato JSON como lo pide la API\n    payload = {"contents": [{"parts": [{"text": texto}]}]}\n    headers = {"Content-Type": "application/json"}\n    \n    # 3. Hacemso la petición POST protegida por try/except\n    try:\n        respuesta = requests.post(URL, json=payload, headers=headers)\n        if respuesta.status_code == 200:\n            datos = respuesta.json()\n            return datos["candidates"][0]["content"]["parts"][0]["text"]\n        else:\n            return "Error en la API."\n    except Exception as e:\n        return f"Error de conexión: {e}"\n\n# 4. El bucle infinito interactivo\nprint("🤖 Chatbot iniciado. Escribe \'salir\' para terminar.")\nwhile True:\n    usuario = input("Tú: ")\n    if usuario.lower() == "salir":\n        print("🤖 Adiós!")\n        break\n    \n    if API_KEY != "PON_TU_API_KEY_AQUI":\n        respuesta_bot = preguntar_a_gemini(usuario)\n        print(f"🤖 Bot: {respuesta_bot}")\n    else:\n        print("🤖 Bot: (Por favor configura tu API KEY en el código primero)")\n        break')
    ])

if __name__ == "__main__":
    gen_mod4()
    gen_mod5()
    gen_mod6()
    print("Módulos 4, 5 y 6 generados")
