import pandas as pd
import numpy as np
import time
from VariablesGlobales import separación
from typing import List, Tuple, Callable
from itertools import chain
from ClaseMaybe import Maybe, control

# Se lee el csv. Lo de latin-1 es para que no de error al leer el archivo
dataset = pd.read_csv("JEOPARDY_CSV.csv", encoding ='latin-1')

# Esto es para que muestre todo el contenido de las columnas en caso que se precise
pd.set_option('display.max_colwidth', None)
pd.set_option("display.max_columns", None)

# Se toma un paquete de 5 preguntas aleatorias
paquete = dataset.sample(5)

# Se toman las columnas que se van a usar cada una por separado para facilitar el manejo y tener más claridad de lo que se usa
# en cada momento
rondas = paquete['Round']
categorias = paquete['Category']
premios = paquete['Value']
preguntas = paquete['Question']
respuestas = paquete['Answer']

"""
    partida es la función principal del juego. Se encarga de llevar a cabo el juego en sí.
    Sus argumentos ya están prefijados a efectos de que a la hora de hacer los tests no haya problemas del tipo OutofBounds con los índices
    Empezando en 0, dicha función va haciendo las preguntas (contador) hasta que se llegue a la cantidad de preguntas prefijadas (k).

"""

def partida(k: int = 5, pun: int = 0, prem: int = 0, contador: int = 0) -> None:
    
    while contador != k:
        respuesta, opciones_usuario = hacer_pregunta(contador)
                
        if control_respuesta(respuesta) is False:
            print(f"Entrada incorrecta, por favor ingrese una letra válida\n{separación}")
            return partida(k, pun, prem, contador)
        else:
            (n_pun, n_prem, veri) = verificar_respuesta(respuesta, opciones_usuario, contador, pun, prem)
            time.sleep(2)
            
            if veri is False:
                print(f"Respuesta incorrecta. La respuesta correcta era: {respuestas.iloc[contador]}\n{separación}")
            else:
                print(f"Respuesta correcta! Ganaste: {premios.iloc[contador]}\n{separación}")
            return partida(k, n_pun, n_prem, contador + 1)
            
    print("|" + " " * 23 +  "Fin de la partida" + " " * 22 + f"|\n{separación}\nPuntaje: {pun} | Premios totales: ${prem}\n{separación}")
    return None

"""
    Esta funcion dispara el funcionamiento de mostrar la pregunta y devuelve la respuesta del usuario y las opciones que le aparecieron
    (provistas por la función mostrar pregunta) para luego ver si eligió bien o no.

"""

def hacer_pregunta(n: int) -> Tuple[str, List[str]]:
    opciones_usuario = mostrar_pregunta(n)
    respuesta = input(f"{separación}\nRespuesta: ")
    
    return (respuesta, opciones_usuario)

"""
    mostrar_pregunta se encarga de mostrar la pregunta en pantalla. Se le pasa el índice de la pregunta para buscar su información dentro
    del paquete de preguntas. Usando el índice es que se muestra la ronda, la categoría, el premio, la pregunta y las opciones. 
    Luego se mezclan las opciones para que la opción correcta no quede siempre en la misma posición del array de opciones.
    
"""

def mostrar_pregunta(n: int) -> List[str]:
    mensaje_pregunta = f"Ronda: {rondas.iloc[n]} | Categoría: {categorias.iloc[n]} | Premios: {premios.iloc[n]}\n{separación}\nPregunta N°{n + 1}: {preguntas.iloc[n]}\nOpciones:"
    opciones_pregunta = list(chain(buscar_opciones(categorias.iloc[n], n), [respuestas.iloc[n]]))
    
    np.random.shuffle(opciones_pregunta)
    letras = ['A) ', 'B) ', 'C) ']
    
    opcionesFinal = list(map(lambda x, y: x + y, letras, opciones_pregunta))
    print(mensaje_pregunta, *opcionesFinal, sep = " | ")
    
    return opciones_pregunta

"""
    buscar_opciones se encarga de buscar las opciones posibles para la pregunta. Se le pasa la categoría de la pregunta para que busque respuestas
    de preguntas de la misma categoría sin incluir la respuesta de la pregunta original. 
    Si no encuentra dos opciones posibles, busca respuestas de cualquier otra pregunta
    
"""
    
def buscar_opciones(categoria: str, r: int) -> List[str]:
    opciones = list(dataset.loc[(dataset['Category'] == categoria) & (dataset['Answer'] != respuestas.iloc[r])]["Answer"].iloc[0:2])
    n_faltantes = 2 - len(opciones)
    
    opciones_extra = list(dataset.loc[dataset['Answer'] != respuestas.iloc[r]]["Answer"].sample(n_faltantes))
    
    return opciones if len(opciones) == 2 else list(chain(opciones, opciones_extra))


"""
    control_respuesta verifica que la respuesta del usuario sea válida. En caso de que no lo sea, se le pide que ingrese una letra válida.

"""

def control_respuesta(r: str) -> bool:
    return r.lower() in ['a', 'b', 'c']

"""
    traducir_respuesta se encarga de traducir la respuesta del usuario a un número y poder usarlo como índice en el array de opciones y 
    comparar luego con la respuesta correcta.

"""

def traducir_respuesta(r: str) -> int:
    return 0 if r == 'a' else 1 if r == 'b' else 2
    
"""
    El decorador simplemente simula el procesamiento de la respuesta
    cada vez que se la quiere verificar

"""

def decorador_verificacion(func : Callable) -> Callable:
    def wrapper(*args, **kwargs):
        print(f"Verificando opcion {args[0]}")
        
        result = func(*args, **kwargs)
        return result
    
    return wrapper


"""
    verificar_respuesta se encarga de verificar si el usuario le embocó a la respuesta o no. Se usa un Maybe Monad 
    para ver si el premio es None o si puede ser tratado como un int, porque los premios pueden 
    tener formatos del tipo '$10,000', '$2000', '3,000', 'None', etc.

"""

@decorador_verificacion
def verificar_respuesta(r: str, opciones: List[str], n: int, c_puntos: int, c_premios: int) -> Tuple[int, int, bool]:
    n_res = traducir_respuesta(r)
    verificador = opciones[n_res] == respuestas.iloc[n]
    
    v_premio = Maybe(premios.iloc[n]).bind(lambda x: control(x)).value
    n_premio = v_premio if isinstance(v_premio, int) else 0
    
    (c_puntos, c_premios) = (c_puntos + 10, c_premios + n_premio) if verificador is True else (c_puntos, c_premios)
    
    return (c_puntos, c_premios, verificador)


