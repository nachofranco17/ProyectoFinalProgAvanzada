
import time
from typing import Callable, Any
from Parte2 import partida
from VariablesGlobales import separación
from functools import partial

"""
    menu_principal lo único que hace es pedir la entrada del usuario y verificar que sea correcta.
    Se muestra en pantalla un mensaje en caso de que la entrada no sea válida. En caso de que lo sea, se llama a la función inicio
    que inicia el juego.
    
    Se hace uso de Partial para fijar los argumentos de la función partida, los cuales son la cantidad de preguntas, el puntaje, los premios y 
    por cuál pregunta vas (contador) respectivamente. Esto se hace primero para usar el Partial y 
    luego porque en nuestro caso la cantidad de preguntas ya esta prefijada como 5 (pero en otro contexto puede ser una variable). 
    El resto de argumentos son 0 por defecto y coherencia.
    
"""

def menu_principal() -> Any:
    entrada = input(f"{separación}\nBienvenido al Triviador Mundo, ingrese Empezar cuando esté listo \n{separación} \nEntrada: ")
    
    return error_a_menu() if control(entrada) is False else inicio()

def control(e: Any) -> bool:
    return e == "Empezar" or e == "empezar"

def inicio() -> None:
    print(separación, "\n|" + " " * 20 + "Iniciando Triviador Mundo" + " " * 17 + f"|\n{separación}")
    time.sleep(2)
    partida_de5: Callable[[],None] = partial(partida, 5, 0, 0, 0)
    partida_de5()

def mostrar_error() -> str:
    mensaje = "Salida: entrada incorrecta, por favor ingrese Empezar"
    return mensaje

def error_a_menu() -> Callable:
    print(mostrar_error())
    return menu_principal()

if __name__ == '__main__':
    menu_principal()