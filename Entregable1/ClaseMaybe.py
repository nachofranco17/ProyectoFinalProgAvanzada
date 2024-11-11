from __future__ import annotations
from typing import TypeVar, Optional, Generic, Callable

T = TypeVar('T')
U = TypeVar('U')

"""
    Maybe es una clase que se encarga de manejar los casos en los que el valor de una variable puede ser None o no
    Cuando el valor que se le pasa al Maybe es None, el bind no hace nada y devuelve el mismo Maybe que es del tipo None
    Cuando el valor que se le pasa al Maybe no es None, el bind aplica la función que se le pasa como argumento que
    en nuestro caso es el handler que se encarga de transformar el string a un int.
"""

class Maybe(Generic[T]):
    def __init__(self, value: Optional[T]) -> None:
        self.value = value
        
    def bind(self, func: Callable[[T], Maybe[U]]) -> Maybe[T] | Maybe[U]:
        return self if self.value is None else func(self.value)

def control(s: str) -> Maybe[int]:
    return Maybe(None) if s == 'None' else Maybe(handler(s))
    
def handler(s: str) -> int:
    try:
        return int(s.strip("$").replace(',', ''))
    except ValueError:
        return int(s.replace(',', ''))
  

            
