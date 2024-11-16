import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import ply.lex as lex
from Lexer.Tokens import tokens, palabras_reservadas
from Lexer.ReglasLexer import *

lexer = lex.lex()

def tokenize(input_string):
    lexer.input(input_string)
    return list(lexer)

def get_lexer():
    return lexer

# Lista de consultas para probar
def probarConsultas(): # pragma: no cover
    consultas = [
        # Consulta 1
        "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;",
        # Consulta 2
        "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';",
        # Consulta 3
        "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);",
        # Consulta 4
        "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';",
        # Consulta 5
        "BORRA DE LA tabla_clientes DONDE edad ENTRE 18 Y 25;",
        # Consulta 6
        "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;",
        # Consulta 7
        "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;",
        # Consulta 8
        """CREA LA TABLA productos (
            id INT CLAVE PRIMA,
            nombre VARCHAR(100) UNICO,
            precio INT POR DEFECTO 0,
            categoria VARCHAR(50) NO NULO
        );""",
        # Consulta 9
        "TIRA LA TABLA productos;",
        # Consulta 10
        "TRAEME CONTANDO(*) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY CONTANDO(*) > 5;",
        # Consulta 11
        "TRAEME nombre, edad DE LA TABLA usuarios DONDE edad >= 21 OR ciudad PARECIDO A 'Montevideo%' ORDENA POR edad COMO MUCHO 10;",
    ]

    for idx, consulta in enumerate(consultas, start=1):
        print("-" * 60)
        print(f"Consulta {idx}:")
        print(consulta)
        lexer.input(consulta)
        for tok in lexer:
            print(tok)
            
if __name__ == '__main__':
    probarConsultas()
        
        
        
        
