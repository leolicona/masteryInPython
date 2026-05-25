import os
import json

COURSE_STRUCTURE = {
    "modulo_1": [
        "01_introduccion_y_entorno.ipynb",
        "02_variables_y_tipos_datos.ipynb",
        "03_numeros_y_booleanos.ipynb",
        "04_manipulacion_de_strings.ipynb",
        "05_ejercicios_refuerzo.ipynb"
    ],
    "modulo_2": [
        "01_operadores_basicos.ipynb",
        "02_condicionales_y_match.ipynb",
        "03_bucles_while_y_for.ipynb",
        "04_ejercicios_refuerzo.ipynb"
    ],
    "modulo_3": [
        "01_listas_y_tuplas.ipynb",
        "02_conjuntos_y_diccionarios.ipynb",
        "03_ejercicios_refuerzo.ipynb"
    ],
    "modulo_4": [
        "01_funciones_y_lambdas.ipynb",
        "02_modulos_y_paquetes.ipynb",
        "03_ejercicios_refuerzo.ipynb"
    ],
    "modulo_5": [
        "01_manejo_de_errores.ipynb",
        "02_manejo_de_archivos.ipynb",
        "03_ejercicios_refuerzo.ipynb"
    ],
    "modulo_6": [
        "01_intro_apis_y_requests.ipynb",
        "02_proyecto_final_chatbot_ai.ipynb"
    ]
}

def create_notebook(filepath, title):
    # Nota: el usuario deberá reemplazar YOUR_USERNAME_AQUI
    colab_link = f'<a href="https://colab.research.google.com/github/YOUR_USERNAME_AQUI/masteryInPython/blob/main/{filepath}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
    
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    colab_link + "\n\n",
                    f"# {title}\n"
                ]
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Escribe tu código aquí\n"
                ]
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.8.10"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 4
    }
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, indent=2, ensure_ascii=False)

def main():
    for mod, notebooks in COURSE_STRUCTURE.items():
        if not os.path.exists(mod):
            os.makedirs(mod)
        for nb in notebooks:
            filepath = os.path.join(mod, nb)
            title = nb.replace('.ipynb', '').replace('_', ' ').title()
            create_notebook(filepath, title)
            print(f"Created {filepath}")

if __name__ == "__main__":
    main()
