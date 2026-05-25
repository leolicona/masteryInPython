# Plan: Curso de Python para Google Colab

Este plan detalla la creación de un curso interactivo de Python diseñado específicamente para ser consumido a través de Google Colab y alojado en tu repositorio de GitHub. 

## Contexto y Objetivo
El objetivo es construir una serie de cuadernos de Jupyter (`.ipynb`) organizados por módulos. Cada módulo contendrá lecciones teóricas con ejercicios prácticos integrados y cuadernos dedicados exclusivamente a ejercicios de refuerzo. Al alojar estos archivos en GitHub, podremos generar enlaces que abrirán automáticamente los cuadernos en Google Colab (mediante la URL `colab.research.google.com/github/...`).

## Estructura de Carpetas y Archivos

El curso estará organizado de la siguiente manera dentro del repositorio `masteryInPython`:

### README.md
El archivo principal del repositorio. Contendrá la descripción del curso, el temario y los botones interactivos de "Open in Colab" para acceder a cada lección directamente.

---

### Módulo 1: Primeros Pasos con Python
*Fundamentos del lenguaje, configuración del entorno y sintaxis básica.*

- `modulo_1/01_introduccion_y_entorno.ipynb`
  - Por qué aprender Python en tiempos de AI
  - Comandos básicos de Python en la terminal.
  - Sintaxis e indentación básica.
  - Comentarios en Python: líneas simples y multilínea.
- `modulo_1/02_variables_y_tipos_datos.ipynb`
  - Variables: asignación, nomenclatura y convenciones.
  - Asignación múltiple de variables.
  - Tipos de datos en Python: strings, números y colecciones.
  - Tipo de dato None en Python.
- `modulo_1/03_numeros_y_booleanos.ipynb`
  - Manipulación y conversión de tipos numéricos.
  - Booleanos: True, False y casting a bool.
- `modulo_1/04_manipulacion_de_strings.ipynb`
  - Manejo de comillas, múltiples líneas y búsqueda en strings.
  - Slicing, replace y split para manipular strings.
- `modulo_1/05_ejercicios_refuerzo.ipynb`
  - *Cuaderno dedicado a practicar todo lo aprendido en el Módulo 1.*

---

### Módulo 2: Lógica de Programación y Control de Flujo
*Tomar decisiones y repetir acciones basadas en condiciones.*

- `modulo_2/01_operadores_basicos.ipynb`
  - Operadores aritméticos: suma, resta, módulo y precedencia.
  - Operadores de asignación y operador walrus (`:=`).
  - Operadores lógicos (and, or, not) con booleanos.
- `modulo_2/02_condicionales_y_match.ipynb`
  - Condicionales: if, elif, else y uso de `pass`.
  - Sentencia `match` (Python 3.10+) para control de flujo estructural.
- `modulo_2/03_bucles_while_y_for.ipynb`
  - Bucles `while`: condiciones, break y continue.
  - Bucles `for`: recorrido de secuencias, rangos y listas.
- `modulo_2/04_ejercicios_refuerzo.ipynb`
  - *Ejercicios prácticos integrando condicionales y bucles.*

---

### Módulo 3: Estructuras de Datos Fundamentales
*Cómo almacenar, organizar y manipular colecciones de datos.*

- `modulo_3/01_listas_y_tuplas.ipynb`
  - Listas: creación, modificación, métodos esenciales y slicing.
  - Tuplas: ordenadas, inmutables y manejo de duplicados.
- `modulo_3/02_conjuntos_y_diccionarios.ipynb`
  - Conjuntos (Sets): creación, métodos y operaciones de conjuntos (unión, intersección).
  - Diccionarios: pares clave-valor, ordenamiento y anidación.
- `modulo_3/03_ejercicios_refuerzo.ipynb`
  - *Ejercicios para dominar el manejo y combinación de estructuras de datos.*

---

### Módulo 4: Modularización del Código
*Escribir código reutilizable y organizado.*

- `modulo_4/01_funciones_y_lambdas.ipynb`
  - Definición y uso de funciones con argumentos y `return`.
  - Funciones lambda (anónimas) y funciones como ciudadanos de primera clase (fábrica de funciones).
- `modulo_4/02_modulos_y_paquetes.ipynb`
  - Importación de módulos estándar.
  - Cómo organizar y separar código en múltiples archivos.
- `modulo_4/03_ejercicios_refuerzo.ipynb`
  - *Retos prácticos creando y consumiendo funciones personalizadas.*

---

### Módulo 5: Manejo de Errores y Archivos
*Hacer programas robustos y persistentes.*

- `modulo_5/01_manejo_de_errores.ipynb`
  - Captura y manejo de excepciones con `try`, `except`, `else` y `finally`.
  - Lanzamiento de errores personalizados con `raise`.
- `modulo_5/02_manejo_de_archivos.ipynb`
  - Lectura y escritura de archivos de texto (txt, csv) usando el gestor de contexto `with open()`.
- `modulo_5/03_ejercicios_refuerzo.ipynb`
  - *Ejercicios leyendo datos de un archivo, procesándolos sin que el programa falle por errores, y guardando resultados.*

---

### Módulo 6: Trabajo Práctico Final con Implementación de AI
*Unir todos los conocimientos en un proyecto del mundo real.*

- `modulo_6/01_intro_apis_y_requests.ipynb`
  - Conceptos básicos de APIs REST.
  - Uso de la librería `requests` para hacer peticiones HTTP (GET, POST).
  - Manejo de respuestas en formato JSON.
- `modulo_6/02_proyecto_final_chatbot_ai.ipynb`
  - **El Proyecto:** Creación de un script interactivo (chatbot o analizador de texto) de línea de comandos.
  - Integración con una API de Inteligencia Artificial (por ejemplo, Google Gemini API o la API gratuita de Hugging Face).
  - Uso de funciones para modularizar la lógica, manejo de errores para fallos de red, estructuras de control para el ciclo de chat y diccionarios para guardar el historial de la conversación.

## Implementación Técnica
Para la creación de los cuadernos:
1. Se generarán los archivos `.ipynb` estructurados en formato JSON válido.
2. Cada cuaderno incluirá celdas de tipo `markdown` (para teoría, explicaciones e instrucciones de ejercicios) y celdas de tipo `code` (con ejemplos funcionales y espacios para que resuelvas los problemas).
3. Se añadirá el badge de "Open in Colab" en el Markdown de cada cuaderno y en el `README.md` principal para asegurar una navegación fluida.
