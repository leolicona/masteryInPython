import json
import os

def md_cell(text):
    lines = [line + "\n" for line in text.split('\n')]
    if lines and lines[-1] == "\n":
        lines = lines[:-1]
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": lines
    }

def code_cell(code):
    lines = [line + "\n" for line in code.split('\n')]
    if lines and lines[-1] == "\n":
        lines = lines[:-1]
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": lines
    }

def save_notebook(filepath, title, cells):
    colab_link = f'<a href="https://colab.research.google.com/github/YOUR_USERNAME_AQUI/masteryInPython/blob/main/{filepath}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>\n\n'
    
    header_cell = md_cell(colab_link + f"# {title}")
    final_cells = [header_cell] + cells

    notebook = {
        "cells": final_cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.8.10"}
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

def generate_nb1():
    cells = [
        md_cell("## 1. ¿Por qué Python?\nPython es uno de los lenguajes de programación más populares del mundo. Es fácil de leer (casi como leer inglés), increíblemente versátil (se usa en desarrollo web, inteligencia artificial, automatización) y tiene una comunidad inmensa que ha creado herramientas para casi todo.\n\nEn este curso no solo aprenderás a programar, sino a *pensar* como un programador."),
        md_cell("## 2. El Entorno de Trabajo\nNormalmente, los programadores escriben código en editores como **Visual Studio Code** y lo ejecutan usando la terminal. Aquí estamos usando un **Jupyter Notebook**, que es un entorno interactivo perfecto para aprender. Cada bloque gris que ves abajo se llama **celda de código**.\n\n### Tu primer programa\nLa tradición dicta que nuestro primer programa debe saludar al mundo. En Python, hacemos esto con la instrucción `print()`."),
        code_cell('print("¡Hola Mundo!")'),
        md_cell("Para ejecutar la celda de arriba, haz clic en ella y presiona `Shift + Enter` (o dale al botón de 'Play' que aparece a la izquierda de la celda).\n\n## 3. Comentarios en Python\nEl código no es solo para que lo lean las máquinas; es para que lo lean los humanos. Los comentarios son notas que dejas en el código y que Python ignora por completo. Son vitales para explicar el *por qué* de tu lógica."),
        code_cell('# Esto es un comentario de una sola línea.\nprint("Esto sí se ejecuta")\n\n"""\nEsto es un comentario\nde múltiples líneas.\nSirve para explicaciones muy largas.\n"""\nprint("Y esto también se ejecuta")'),
        md_cell("## 🎯 Tu Turno\nEn la celda de abajo, escribe un programa que imprima tu nombre, y usa un comentario para indicar de qué país eres.")
    ]
    save_notebook("modulo_1/01_introduccion_y_entorno.ipynb", "Introducción y Entorno", cells)

def generate_nb2():
    cells = [
        md_cell("## 1. ¿Qué es una Variable?\nImagina que una variable es una caja con una etiqueta donde puedes guardar datos. Cuando necesites ese dato más adelante, simplemente llamas a la etiqueta de la caja.\n\nEn Python, no necesitas decirle de qué material es la caja (qué tipo de dato vas a guardar), Python lo adivina por ti. Solo usas el signo `=` para asignar un valor a una variable."),
        code_cell('nombre = "Leo"       # Guardamos texto\nedad = 25          # Guardamos un número entero\naltura = 1.75      # Guardamos un número con decimales\n\nprint("Me llamo", nombre, "y tengo", edad, "años.")'),
        md_cell("### Reglas para nombrar variables:\n- Deben empezar con una letra o un guion bajo `_`.\n- No pueden contener espacios (usa `guion_bajo` conocido como *snake_case*).\n- No pueden ser palabras reservadas de Python (como `print`, `if`, `while`)."),
        md_cell("## 2. Tipos de Datos Básicos\nEn el ejemplo anterior vimos tres tipos de datos básicos:\n1. **Strings (`str`)**: Cadenas de texto. Siempre van entre comillas simples `''` o dobles `\"\"`.\n2. **Integers (`int`)**: Números enteros, sin decimales.\n3. **Floats (`float`)**: Números con decimales.\n\nPuedes usar la función `type()` para descubrir qué tipo de dato hay en una variable."),
        code_cell('misterio = 42\nprint(type(misterio))\n\nmisterio = "Cuarenta y dos"\nprint(type(misterio)) # ¡Python te permite cambiar el tipo de dato de una variable libremente!'),
        md_cell("## 3. Asignación Múltiple\nPython tiene un truco genial: puedes asignar valores a múltiples variables en una sola línea. Esto ahorra espacio y hace el código más limpio."),
        code_cell('x, y, z = 10, 20, 30\nprint(x, y, z)\n\n# También puedes dar el mismo valor a varias variables\na = b = c = 100\nprint(a, b, c)'),
        md_cell("## 4. El tipo de dato None\nA veces necesitas una caja vacía, una variable que exista pero que no tenga nada todavía. Para eso usamos `None`."),
        code_cell('resultado_pendiente = None\nprint(type(resultado_pendiente))'),
        md_cell("## 🎯 Tu Turno\nCrea tres variables: tu animal favorito (string), la cantidad de patas que tiene (int) y su peso aproximado en kg (float). Luego imprime una frase usando las tres variables.")
    ]
    save_notebook("modulo_1/02_variables_y_tipos_datos.ipynb", "Variables y Tipos de Datos", cells)

def generate_nb3():
    cells = [
        md_cell("## 1. Operaciones Matemáticas Básicas\nPython es esencialmente una calculadora muy potente. Puedes usar variables numéricas o números directamente."),
        code_cell('a = 10\nb = 3\n\nprint("Suma:", a + b)\nprint("Resta:", a - b)\nprint("Multiplicación:", a * b)\nprint("División:", a / b)      # Siempre devuelve un float\nprint("División entera:", a // b) # Devuelve un int, descarta decimales\nprint("Módulo:", a % b)        # Devuelve el resto de la división (muy útil para saber si un número es par)\nprint("Exponente:", a ** b)    # a elevado a la b (10 al cubo)'),
        md_cell("## 2. Booleanos: Cierto o Falso\nLos booleanos (`bool`) son un tipo de dato que solo puede tener dos valores: `True` (Verdadero) o `False` (Falso). Nota que la primera letra siempre va en mayúscula.\n\nSon la base de la toma de decisiones en programación. Normalmente los obtenemos al comparar cosas."),
        code_cell('es_mayor = 10 > 5\nprint("¿10 es mayor que 5?", es_mayor)\n\nprint("¿5 es igual a 5?", 5 == 5)    # Usamos == para comparar, = es para asignar\nprint("¿3 es diferente de 4?", 3 != 4)\nprint("¿10 es menor o igual a 10?", 10 <= 10)'),
        md_cell("## 3. Conversión de Tipos (Casting)\nA veces necesitas transformar un número en texto, o texto en número. Esto se llama *casting*."),
        code_cell('numero_texto = "100"\n# print(numero_texto + 50)  # Esto daría un error, no puedes sumar texto y número directamente.\n\nnumero_real = int(numero_texto)\nprint("Ahora sí:", numero_real + 50)\n\n# Puedes convertir a booleano. Casi todo es True, excepto el 0, las listas vacías o el None.\nprint("bool de 1:", bool(1))\nprint("bool de 0:", bool(0))\nprint("bool de texto vacío:", bool(""))'),
        md_cell("## 🎯 Tu Turno\nCalcula el área de un triángulo (base * altura / 2) usando variables para la base y la altura. Imprime el resultado.")
    ]
    save_notebook("modulo_1/03_numeros_y_booleanos.ipynb", "Números y Booleanos", cells)

def generate_nb4():
    cells = [
        md_cell("## 1. El poder de los Strings\nLos strings en Python son muy flexibles. Si tu texto incluye comillas simples, envuelve el string en comillas dobles (y viceversa). Si necesitas un texto de varias líneas (como un poema), usa tres comillas `'''`."),
        code_cell('frase = "El programador dijo: \'Python es genial\'."\npoema = """\nRosa roja\nCielo azul\nPython es chido\nY tú también\n"""\nprint(frase)\nprint(poema)'),
        md_cell("### F-Strings (Format Strings)\nLa forma más moderna y limpia de meter variables dentro de un texto en Python es usando f-strings. Pon una `f` antes de las comillas, y mete tus variables en `{}`."),
        code_cell('nombre = "Leo"\nmeta = "Maestro de Python"\n\nprint(f"Me llamo {nombre} y voy a ser un {meta}!")'),
        md_cell("## 2. Manipulación: Métodos de Strings\nUn string viene con \"herramientas\" integradas llamadas métodos para manipular su texto."),
        code_cell('texto = "  Python es asombroso  "\n\nprint("Original:", texto)\nprint("Mayúsculas:", texto.upper())\nprint("Minúsculas:", texto.lower())\nprint("Sin espacios a los lados:", texto.strip())\nprint("Reemplazando palabras:", texto.replace("asombroso", "increíble"))'),
        md_cell("## 3. Slicing (Rebanando Strings) y Búsqueda\nPuedes acceder a partes específicas de un string usando corchetes `[]`. En programación, **¡siempre empezamos a contar desde cero!**"),
        code_cell('palabra = "Programacion"\n\nprint("Primera letra:", palabra[0])\nprint("Última letra:", palabra[-1])   # Índices negativos cuentan desde el final\nprint("Las primeras 3 letras:", palabra[0:3]) # [inicio:fin] (el fin no se incluye)\nprint("Desde la índice 5 en adelante:", palabra[5:])\n\n# También podemos convertir un string en una lista de palabras usando split()\nfrase = "Manzana, Pera, Plátano"\nfrutas = frase.split(", ")\nprint("Frutas separadas:", frutas)'),
        md_cell("## 🎯 Tu Turno\nCrea una variable con el texto `\"    aprendiendo python en colab    \"`. Límpiala de espacios extra en los extremos, conviértela a mayúsculas usando métodos, y luego imprime las primeras 11 letras de esa nueva frase.")
    ]
    save_notebook("modulo_1/04_manipulacion_de_strings.ipynb", "Manipulación de Strings", cells)

def generate_nb5():
    cells = [
        md_cell("## 🧠 Ejercicios de Refuerzo: Módulo 1\n\n¡Felicidades por llegar hasta aquí! Es hora de poner a prueba todo lo que has aprendido en este módulo. No te preocupes si tienes que revisar los cuadernos anteriores, ¡los programadores de verdad buscan cosas en Google y en sus propios apuntes todo el tiempo!"),
        md_cell("### Ejercicio 1: El Cajero Automático\nEscribe un programa que simule un cajero automático muy simple. \n1. Define una variable `saldo_inicial` con un valor de 1000.\n2. Define una variable `retiro` con un valor de 350.\n3. Calcula el nuevo saldo y guárdalo en una variable `saldo_final`.\n4. Imprime un mensaje usando *f-strings* que diga: `\"Has retirado $350. Tu saldo actual es $650.\"`"),
        code_cell('# Tu código aquí\n'),
        md_cell("### Ejercicio 2: Analizador de Datos Personales\n1. Crea las siguientes variables con tus datos: `nombre`, `edad`, `ciudad`.\n2. Averigua cuántos caracteres (letras) tiene tu nombre. (Pista: usa la función `len(nombre)`).\n3. Imprime en mayúsculas el mensaje: `\"HOLA MI NOMBRE ES [TU NOMBRE], TENGO [EDAD] AÑOS Y VIVO EN [CIUDAD]. MI NOMBRE TIENE [NUM] LETRAS.\"`"),
        code_cell('# Tu código aquí\n'),
        md_cell("### Ejercicio 3: El truco de la Temperatura\nTienes una temperatura en grados Celsius: `celsius = 25.5`.\nLa fórmula para convertir a Fahrenheit es: `F = (C * 9/5) + 32`.\n\nEscribe el código para hacer la conversión e imprime el resultado así: `\"25.5ºC equivalen a X.XºF\"`."),
        code_cell('celsius = 25.5\n# Tu código aquí\n'),
        md_cell("### Ejercicio 4: Verificador de Paridad\nCrea una variable llamada `numero` con cualquier valor entero.\nUsa el operador módulo (`%`) para determinar si el número es divisible por 2 (o sea, si el residuo es cero). \nGuarda el resultado (que será un booleano `True` o `False`) en una variable llamada `es_par` e imprímela."),
        code_cell('# Tu código aquí\n'),
        md_cell("---\n*¡Si pudiste resolver esto, estás más que listo para el Módulo 2 donde aprenderemos a hacer que nuestros programas tomen sus propias decisiones!*")
    ]
    save_notebook("modulo_1/05_ejercicios_refuerzo.ipynb", "Ejercicios de Refuerzo Módulo 1", cells)

def main():
    print("Generando contenido para el Módulo 1...")
    generate_nb1()
    generate_nb2()
    generate_nb3()
    generate_nb4()
    generate_nb5()
    print("¡Módulo 1 generado con éxito!")

if __name__ == "__main__":
    main()
