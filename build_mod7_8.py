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
    
    final_cells = [header_cell]
    for i, cell in enumerate(cells):
        final_cells.append(cell)
        if cell["cell_type"] == "markdown":
            src = "".join(cell["source"])
            if "🎯 Tu Turno" in src or "### Ejercicio" in src or "### Reto" in src:
                needs_empty = True
                if i < len(cells) - 1 and cells[i+1]["cell_type"] == "code":
                    needs_empty = False
                if needs_empty:
                    final_cells.append(code_cell("# Escribe tu código aquí\n"))

    notebook = {
        "cells": final_cells,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"codemirror_mode": {"name": "ipython", "version": 3}, "file_extension": ".py", "mimetype": "text/x-python", "name": "python", "nbconvert_exporter": "python", "pygments_lexer": "ipython3", "version": "3.8.10"}
        },
        "nbformat": 4, "nbformat_minor": 4
    }
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

def gen_mod7():
    save_notebook("modulo_7/01_clases_y_objetos.ipynb", "Clases y Objetos", [
        md_cell("## 1. El Paradigma de POO\nEn la Programación Orientada a Objetos, agrupamos **datos** (variables) y **comportamientos** (funciones) dentro de una misma estructura llamada **Clase**. Puedes pensar en una Clase como un plano arquitectónico, y en un **Objeto** (o instancia) como la casa construida con ese plano."),
        code_cell('class Perro:\n    # El método __init__ es el "constructor". Se llama automáticamente al crear un nuevo Perro.\n    def __init__(self, nombre, raza):\n        self.nombre = nombre  # "self" se refiere al objeto específico que estamos creando\n        self.raza = raza\n        \n    def ladrar(self):\n        return f"{self.nombre} dice: ¡Guau!"\n\n# Creando objetos (instancias)\nmi_perro = Perro("Firulais", "Labrador")\notro_perro = Perro("Rex", "Pastor Alemán")\n\nprint(mi_perro.ladrar())\nprint(f"La raza de Rex es {otro_perro.raza}")'),
        md_cell("## 🎯 Tu Turno\nCrea una clase `Coche` con atributos `marca` y `color`. Añade un método `arrancar()` que imprima 'El coche marca [marca] de color [color] ha arrancado'. Luego crea una instancia de tu coche favorito y haz que arranque.")
    ])
    save_notebook("modulo_7/02_metodos_y_encapsulamiento.ipynb", "Métodos y Encapsulamiento", [
        md_cell("## 1. Encapsulamiento\nEs una buena práctica ocultar los datos internos de una clase para que no se modifiquen accidentalmente desde afuera. En Python, indicamos que una variable es 'privada' poniendo un guion bajo `_` o dos `__` al principio de su nombre."),
        code_cell('class CuentaBancaria:\n    def __init__(self, titular, saldo_inicial):\n        self.titular = titular\n        self.__saldo = saldo_inicial  # Variable "privada"\n        \n    def depositar(self, cantidad):\n        if cantidad > 0:\n            self.__saldo += cantidad\n            return f"Depósito exitoso. Nuevo saldo: {self.__saldo}"\n        return "Cantidad inválida"\n        \n    def ver_saldo(self):\n        return f"El saldo de {self.titular} es {self.__saldo}"\n\ncuenta = CuentaBancaria("Leo", 1000)\nprint(cuenta.depositar(500))\n# print(cuenta.__saldo)  # Esto daría un error, __saldo está protegido desde el exterior.\nprint(cuenta.ver_saldo())'),
        md_cell("## 🎯 Tu Turno\nCrea una clase `Usuario` con atributos `username` y `__password`. Crea un método `verificar_password(intento)` que devuelva True si el intento coincide con el password, y False si no.")
    ])
    save_notebook("modulo_7/03_herencia_y_polimorfismo.ipynb", "Herencia y Polimorfismo", [
        md_cell("## 1. Herencia\nLa herencia permite crear una clase nueva (hija) que hereda todos los métodos y atributos de otra clase (padre). Usamos `super()` para llamar a los métodos del padre."),
        code_cell('class Animal:\n    def __init__(self, nombre):\n        self.nombre = nombre\n    def hacer_sonido(self):\n        pass\n\nclass Gato(Animal):\n    def __init__(self, nombre, vidas=7):\n        super().__init__(nombre) # Llama al __init__ de Animal\n        self.vidas = vidas\n    \n    def hacer_sonido(self):\n        return "¡Miau!"\n\nmichi = Gato("Garfield")\nprint(f"{michi.nombre} hace {michi.hacer_sonido()} y tiene {michi.vidas} vidas.")'),
        md_cell("## 🎯 Tu Turno\nCrea una superclase `Empleado` con atributo `sueldo` y un método que imprima el sueldo. Luego crea una subclase `Gerente` que herede de Empleado pero cuyo método de sueldo sume un bono extra de 1000 al sueldo base.")
    ])
    save_notebook("modulo_7/04_ejercicios_poo.ipynb", "Ejercicios Prácticos de POO", [
        md_cell("## 🧠 Ejercicios de Refuerzo: Módulo 7 (POO)\n\n### Ejercicio 1: El Sistema de Biblioteca\nCrea dos clases:\n1. `Libro`: con atributos `titulo`, `autor` y `prestado` (booleano, por defecto False).\n2. `Biblioteca`: con una lista de `Libros`. Debe tener métodos para `agregar_libro(libro)`, `prestar_libro(titulo)` y `devolver_libro(titulo)`.\nEscribe código para probar tu sistema agregando y prestando libros.")
    ])

def gen_mod8():
    save_notebook("modulo_8/01_calentamiento_logico.ipynb", "Bootcamp: Calentamiento", [
        md_cell("## 🔥 Bootcamp: Calentamiento Lógico\n\n### Reto 1: Inversor de Strings\nEscribe una función que reciba un string y lo devuelva invertido. **Restricción:** No puedes usar `string[::-1]`. Debes usar un bucle `for` o `while`."),
        md_cell("### Reto 2: Detector de Palíndromos\nUn palíndromo se lee igual de derecha a izquierda. Escribe una función que reciba una frase, elimine espacios, convierta a minúsculas y verifique si es un palíndromo (ej: 'Anita lava la tina' -> True)."),
        md_cell("### Reto 3: FizzBuzz Clásico\nEscribe una función que imprima los números del 1 al 100. Pero para múltiplos de 3 imprime 'Fizz', para múltiplos de 5 imprime 'Buzz', y para múltiplos de ambos imprime 'FizzBuzz'.")
    ])
    save_notebook("modulo_8/02_arrays_y_strings_avanzados.ipynb", "Bootcamp: Arrays y Strings", [
        md_cell("## 🤺 Bootcamp: Arrays y Strings\n\n### Reto 1: Two Sum (El clásico de LeetCode)\nDada una lista de números enteros `nums` y un entero `target`, devuelve los **índices** de los dos números que sumados dan como resultado `target`.\nEj: `nums = [2, 7, 11, 15], target = 9`. Salida: `[0, 1]` (porque 2+7=9)."),
        md_cell("### Reto 2: Compresión de Strings\nDada una cadena de caracteres consecutivos (ej: `aabcccccaaa`), devuélvela comprimida usando el conteo de letras repetidas (ej: `a2b1c5a3`). Si la cadena comprimida no es más corta que la original, devuelve la original.")
    ])
    save_notebook("modulo_8/03_hashmaps_y_diccionarios.ipynb", "Bootcamp: Hashmaps (Diccionarios)", [
        md_cell("## 🗺️ Bootcamp: El poder de los Hashmaps\n\n### Reto 1: Elemento Mayoritario\nDada una lista de tamaño `n`, encuentra el elemento mayoritario (el que aparece más de `n/2` veces). Usa un diccionario para contar las frecuencias de forma eficiente ($O(n)$)."),
        md_cell("### Reto 2: Agrupando Anagramas\nDada una lista de palabras, agrupa los anagramas (palabras que tienen las mismas letras). \nEj: `['eat', 'tea', 'tan', 'ate', 'nat', 'bat']` -> `[['eat','tea','ate'], ['tan','nat'], ['bat']]`.\n*Pista: Una palabra ordenada alfabéticamente (usando `tuple(sorted(palabra))`) es una excelente clave para un diccionario.*")
    ])
    save_notebook("modulo_8/04_matematicas_y_recursividad.ipynb", "Bootcamp: Mates y Recursividad", [
        md_cell("## 🧮 Bootcamp: Matemáticas y Recursividad\n\n### Reto 1: Fibonacci con Memoización\nLa serie de Fibonacci clásica (recursiva) es extremadamente lenta para números grandes. Implementa una función recursiva de Fibonacci que utilice un diccionario `memo = {}` para almacenar los resultados previamente calculados (Memoización) y lograr que `fib(50)` se calcule al instante."),
        md_cell("### Reto 2: Criba de Eratóstenes\nEscribe un algoritmo eficiente para encontrar todos los números primos menores a un número `n`. (Investiga el algoritmo de la Criba de Eratóstenes e impleméntalo).")
    ])
    save_notebook("modulo_8/05_retos_de_entrevistas_tecnicas.ipynb", "Bootcamp: Entrevistas Técnicas", [
        md_cell("## 💼 Bootcamp: Nivel Entrevista de Trabajo\n\n### Reto 1: Valid Parentheses\nDada una cadena que solo contiene los caracteres `'('`, `')'`, `'{'`, `'}'`, `'['` y `']'`, determina si la cadena de entrada es válida usando una Pila (Stack / Lista). Ej: `{[()]}` es True, `{[(])}` es False."),
        md_cell("### Reto 2: Búsqueda Binaria (Binary Search)\nDada una lista de números enteros **ordenada** y un objetivo, escribe una función que encuentre el índice del objetivo usando el algoritmo de búsqueda binaria ($O(\\log n)$). Si no existe, retorna -1.")
    ])
    save_notebook("modulo_8/06_mini_proyectos_de_consola.ipynb", "Bootcamp: Proyectos de Consola", [
        md_cell("## 🎮 Bootcamp: Proyectos Finales\n\n### Reto 1: Generador de Contraseñas Seguras\nUsa el módulo `random` y `string`. Pregunta al usuario la longitud de la contraseña, si quiere mayúsculas, números y símbolos. Genera una contraseña aleatoria que cumpla las reglas."),
        md_cell("### Reto 2: Tic-Tac-Toe (El Gato)\nConstruye un juego de Gato jugable en consola para dos jugadores. Debes imprimir el tablero 3x3 y tener una lógica robusta para verificar si un jugador ha ganado en filas, columnas o diagonales después de cada turno.")
    ])

if __name__ == "__main__":
    gen_mod7()
    gen_mod8()
    print("Módulos 7 y 8 generados exitosamente!")
