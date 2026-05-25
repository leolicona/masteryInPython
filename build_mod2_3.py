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

def gen_mod2():
    # 01
    save_notebook("modulo_2/01_operadores_basicos.ipynb", "Operadores Básicos y Lógicos", [
        md_cell("## 1. Operadores Aritméticos y de Asignación\nYa vimos la suma y la resta. A veces queremos actualizar una variable usando su propio valor (como sumar puntos en un juego)."),
        code_cell('puntos = 10\npuntos = puntos + 5   # Forma tradicional\nprint(puntos)\n\npuntos += 5          # Forma corta (asignación con adición)\nprint(puntos)'),
        md_cell("## 2. Operadores Lógicos (and, or, not)\nPara tomar decisiones complejas, necesitamos combinar varias preguntas de verdadero/falso."),
        code_cell('tiene_llave = True\nes_de_dia = False\n\nprint("Puede entrar si tiene llave Y es de día:", tiene_llave and es_de_dia)\nprint("Puede entrar si tiene llave O es de día:", tiene_llave or es_de_dia)\nprint("¿NO es de día?", not es_de_dia)'),
        md_cell("## 🎯 Tu Turno\nCrea dos variables: `edad = 20` y `tiene_licencia = True`. Imprime si la persona puede conducir (debe ser mayor o igual a 18 AND tener licencia).")
    ])
    # 02
    save_notebook("modulo_2/02_condicionales_y_match.ipynb", "Condicionales (If, Elif, Else) y Match", [
        md_cell("## 1. Condicionales If / Else\nEl `if` (si ocurre esto) permite que tu código tome distintos caminos. El código dentro de un `if` **debe estar indentado** (llevar espacios al principio)."),
        code_cell('clima = "lluvia"\n\nif clima == "lluvia":\n    print("Lleva paraguas")\nelif clima == "nublado":\n    print("Lleva chamarra")\nelse:\n    print("Día soleado, ponte lentes")'),
        md_cell("## 2. La sentencia Match (Python 3.10+)\nCuando tienes muchísimos `elif` seguidos comprobando la misma variable, es mejor usar `match` (similar al switch de otros lenguajes)."),
        code_cell('dia = "Lunes"\n\nmatch dia:\n    case "Lunes":\n        print("Inicio de semana")\n    case "Viernes":\n        print("¡Por fin!")\n    case _:\n        print("Día normal") # El _ significa "cualquier otro caso"'),
        md_cell("## 🎯 Tu Turno\nEscribe un código que verifique el valor de una variable `nota` (de 0 a 10). Si es mayor o igual a 6, imprime 'Aprobado'. De lo contrario, imprime 'Reprobado'.")
    ])
    # 03
    save_notebook("modulo_2/03_bucles_while_y_for.ipynb", "Bucles While y For", [
        md_cell("## 1. Bucle While\nUn `while` repite un bloque de código **mientras** una condición sea Verdadera. ¡Cuidado con crear bucles infinitos!"),
        code_cell('contador = 3\nwhile contador > 0:\n    print(f"Despegue en {contador}...")\n    contador -= 1\nprint("¡Fuego!")'),
        md_cell("## 2. Bucle For\nEl `for` se usa para recorrer colecciones de elementos (como las letras de un string, o un rango de números)."),
        code_cell('palabra = "Python"\nfor letra in palabra:\n    print(f"Dame una {letra}!")\n\nprint("---")\n# Usando range(inicio, fin)\nfor i in range(1, 4):\n    print(f"Intento número {i}")'),
        md_cell("## 3. Break y Continue\n`break` rompe el bucle por completo. `continue` salta directamente a la siguiente repetición."),
        code_cell('for numero in range(1, 10):\n    if numero == 3:\n        continue  # Se salta el 3\n    if numero == 6:\n        break     # Se detiene al llegar a 6\n    print(numero)'),
        md_cell("## 🎯 Tu Turno\nUsa un bucle `for` y `range()` para imprimir la tabla de multiplicar del 5 (desde 5x1 hasta 5x10).")
    ])
    # 04
    save_notebook("modulo_2/04_ejercicios_refuerzo.ipynb", "Ejercicios de Refuerzo Módulo 2", [
        md_cell("## 🧠 Ejercicios de Refuerzo: Módulo 2\n\n### Ejercicio 1: Clasificador de Edades\nCrea una variable `edad`. Escribe un condicional que imprima:\n- 'Niño' si es menor a 12.\n- 'Adolescente' si está entre 12 y 17.\n- 'Adulto' si tiene 18 o más."),
        code_cell('# Tu código aquí\n'),
        md_cell("### Ejercicio 2: El Cajero Automático (Mejorado)\nTienes un `saldo = 500`. Usa un bucle `while` que pregunte al usuario cuánto quiere retirar (puedes simular el retiro restando números manualmente en el código o usar un límite de intentos). O más fácil: \nCrea un bucle que reste 100 de saldo hasta que el saldo sea 0, imprimiendo el saldo restante en cada paso."),
        code_cell('saldo = 500\n# Tu código aquí\n'),
        md_cell("### Ejercicio 3: FizzBuzz\nEl clásico problema de entrevistas de programación. Imprime números del 1 al 15.\n- Si el número es divisible por 3, imprime 'Fizz'.\n- Si es divisible por 5, imprime 'Buzz'.\n- Si es divisible por ambos, imprime 'FizzBuzz'.\n- Si no es divisible por ninguno, imprime el número."),
        code_cell('# Tu código aquí\n')
    ])

def gen_mod3():
    # 01
    save_notebook("modulo_3/01_listas_y_tuplas.ipynb", "Listas y Tuplas", [
        md_cell("## 1. Listas\nUna lista es una colección ordenada que puede contener varios elementos. Se definen usando corchetes `[]`."),
        code_cell('frutas = ["manzana", "banana", "cereza"]\nprint("Lista original:", frutas)\n\n# Accediendo a elementos\nprint("El primer elemento es:", frutas[0])\n\n# Modificando\nfrutas[1] = "kiwi"\n\n# Agregando al final\nfrutas.append("naranja")\n\n# Eliminando\nfrutas.remove("manzana")\nprint("Lista modificada:", frutas)'),
        md_cell("## 2. Tuplas\nLas tuplas son como las listas, pero **no se pueden modificar** una vez creadas (son inmutables). Son más rápidas y seguras si tienes datos fijos. Se definen con paréntesis `()`."),
        code_cell('coordenadas = (10.5, 20.3)\nprint(coordenadas[0])\n# coordenadas[0] = 15.0  <-- ¡Esto daría error!'),
        md_cell("## 🎯 Tu Turno\nCrea una lista con 3 de tus películas favoritas. Agrega una más usando `append`, y luego usa un bucle `for` para imprimir cada película de la lista.")
    ])
    # 02
    save_notebook("modulo_3/02_conjuntos_y_diccionarios.ipynb", "Conjuntos y Diccionarios", [
        md_cell("## 1. Conjuntos (Sets)\nUn conjunto es una colección desordenada que **no permite elementos duplicados**. Son geniales para eliminar duplicados de una lista de forma rápida. Se usan llaves `{}`."),
        code_cell('numeros = {1, 2, 2, 3, 3, 4}\nprint("Conjunto sin duplicados:", numeros)\n\n# Operaciones de conjuntos\nA = {1, 2, 3}\nB = {3, 4, 5}\nprint("Unión:", A | B)           # Todos los elementos\nprint("Intersección:", A & B)    # Solo los que están en ambos'),
        md_cell("## 2. Diccionarios (Dicts)\nSon colecciones de pares `clave: valor`. Es como un diccionario de la vida real: buscas una palabra (clave) y encuentras su significado (valor)."),
        code_cell('usuario = {\n    "nombre": "Leo",\n    "edad": 25,\n    "es_admin": True\n}\n\n# Accediendo\nprint("Nombre:", usuario["nombre"])\n\n# Modificando / Agregando\nusuario["edad"] = 26\nusuario["ciudad"] = "CDMX"    # Si no existe, se crea\nprint("Diccionario actualizado:", usuario)'),
        md_cell("## 🎯 Tu Turno\nCrea un diccionario que represente a tu mascota (nombre, especie, edad). Imprime solo su nombre.")
    ])
    # 03
    save_notebook("modulo_3/03_ejercicios_refuerzo.ipynb", "Ejercicios de Refuerzo Módulo 3", [
        md_cell("## 🧠 Ejercicios de Refuerzo: Módulo 3\n\n### Ejercicio 1: Eliminando Duplicados\nTienes una lista: `invitados = ['Ana', 'Juan', 'Pedro', 'Ana', 'Luis', 'Juan']`.\nUsa un Set para eliminar los nombres duplicados y guarda el resultado en una nueva lista limpia. Imprímela."),
        code_cell('invitados = ["Ana", "Juan", "Pedro", "Ana", "Luis", "Juan"]\n# Tu código aquí\n'),
        md_cell("### Ejercicio 2: Inventario de Tienda\n1. Crea un diccionario `inventario` con 3 productos como claves y sus cantidades como valores (ej. 'manzanas': 10).\n2. Un cliente compra 2 manzanas. Actualiza el valor en el diccionario.\n3. Agrega un nuevo producto al inventario.\n4. Imprime el inventario usando un bucle for para mostrar `Producto: Cantidad`."),
        code_cell('# Tu código aquí\n')
    ])

if __name__ == "__main__":
    gen_mod2()
    gen_mod3()
    print("Módulos 2 y 3 generados")
