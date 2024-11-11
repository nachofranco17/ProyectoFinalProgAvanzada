import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Lexer.Tokens import palabras_reservadas

# Definiciones de tokens para palabras clave multi-palabra
def t_GROUP_BY(t):
    r'GROUP\s+BY'
    t.type = 'GROUP_BY'
    return t

def t_INSERT_INTO(t):
    r'INSERT\s+INTO'
    t.type = 'INSERT_INTO'
    return t

def t_DELETE_FROM(t):
    r'DELETE\s+FROM'
    t.type = 'DELETE_FROM'
    return t

def t_ORDER_BY(t):
    r'ORDER\s+BY'
    t.type = 'ORDER_BY'
    return t

def t_IS_NULL(t):
    r'IS\s+NULL'
    t.type = 'IS_NULL'
    return t

def t_NOT_NULL(t):
    r'NOT\s+NULL'
    t.type = 'NOT_NULL'
    return t

def t_PRIMARY_KEY(t):
    r'PRIMARY\s+KEY'
    t.type = 'PRIMARY_KEY'
    return t

def t_FOREIGN_KEY(t):
    r'FOREIGN\s+KEY'
    t.type = 'FOREIGN_KEY'
    return t

def t_ALTER_TABLE(t):
    r'ALTER\s+TABLE'
    t.type = 'ALTER_TABLE'
    return t

def t_ADD_COLUMN(t):
    r'ADD\s+COLUMN'
    t.type = 'ADD_COLUMN'
    return t

def t_DROP_COLUMN(t):
    r'DROP\s+COLUMN'
    t.type = 'DROP_COLUMN'
    return t

def t_CREATE_TABLE(t):
    r'CREATE\s+TABLE'
    t.type = 'CREATE_TABLE'
    return t

def t_DROP_TABLE(t):
    r'DROP\s+TABLE'
    t.type = 'DROP_TABLE'
    return t

def t_DE_LA_TABLA(t):
    r'DE\s+LA\s+TABLA'
    t.type = 'DE_LA_TABLA'
    return t

def t_AGRUPANDO_POR(t):
    r'AGRUPANDO\s+POR'
    t.type = 'AGRUPANDO_POR'
    return t

def t_BORRA_DE_LA(t):
    r'BORRA\s+DE\s+LA'
    t.type = 'BORRA_DE_LA'
    return t

def t_MEZCLANDO(t):
    r'MEZCLANDO'
    t.type = 'MEZCLANDO'
    return t

def t_WHERE_DEL_GROUP_BY(t):
    r'WHERE\s+DEL\s+GROUP\s+BY'
    t.type = 'WHERE_DEL_GROUP_BY'
    return t

def t_METE_EN(t):
    r'METE\s+EN'
    t.type = 'METE_EN'
    return t

def t_LOS_VALORES(t):
    r'LOS\s+VALORES'
    t.type = 'LOS_VALORES'
    return t

def t_CAMBIA_LA_TABLA(t):
    r'CAMBIA\s+LA\s+TABLA'
    t.type = 'CAMBIA_LA_TABLA'
    return t

def t_AGREGA_LA_COLUMNA(t):
    r'AGREGA\s+LA\s+COLUMNA'
    t.type = 'AGREGA_LA_COLUMNA'
    return t

def t_ELIMINA_LA_COLUMNA(t):
    r'ELIMINA\s+LA\s+COLUMNA'
    t.type = 'ELIMINA_LA_COLUMNA'
    return t

def t_CREA_LA_TABLA(t):
    r'CREA\s+LA\s+TABLA'
    t.type = 'CREA_LA_TABLA'
    return t

def t_TIRA_LA_TABLA(t):
    r'TIRA\s+LA\s+TABLA'
    t.type = 'TIRA_LA_TABLA'
    return t

def t_POR_DEFECTO(t):
    r'POR\s+DEFECTO'
    t.type = 'POR_DEFECTO'
    return t

def t_CLAVE_PRIMA(t):
    r'CLAVE\s+PRIMA'
    t.type = 'CLAVE_PRIMA'
    return t

def t_CLAVE_REFERENTE(t):
    r'CLAVE\s+REFERENTE'
    t.type = 'CLAVE_REFERENTE'
    return t

def t_LOS_DISTINTOS(t):
    r'LOS\s+DISTINTOS'
    t.type = 'LOS_DISTINTOS'
    return t

def t_ORDENA_POR(t):
    r'ORDENA\s+POR'
    t.type = 'ORDENA_POR'
    return t

def t_COMO_MUCHO(t):
    r'COMO\s+MUCHO'
    t.type = 'COMO_MUCHO'
    return t

def t_EN_ESTO(t):
    r'EN\s+ESTO:'
    t.type = 'EN_ESTO'
    return t

def t_PARECIDO_A(t):
    r'PARECIDO\s+A'
    t.type = 'PARECIDO_A'
    return t

def t_ES_NULO(t):
    r'ES\s+NULO'
    t.type = 'ES_NULO'
    return t

def t_NO_NULO(t):
    r'NO\s+NULO'
    t.type = 'NO_NULO'
    return t

def t_TRANSFORMA_A(t):
    r'TRANSFORMA\s+A'
    t.type = 'TRANSFORMA_A'
    return t

def t_Y(t):
    r'Y'
    t.type = 'Y'
    return t

# Definiciones de tokens para palabras clave de una sola palabra
t_SELECT = r'SELECT'
t_ASTERISCO = r'\*'
t_FROM = r'FROM'
t_WHERE = r'WHERE'
t_JOIN = r'JOIN'
t_ON = r'ON'
t_DISTINCT = r'DISTINCT'
t_COUNT = r'COUNT'
t_VALUES = r'VALUES'
t_UPDATE = r'UPDATE'
t_SET = r'SET'
t_HAVING = r'HAVING'
t_EXISTS = r'EXISTS'
t_IN = r'IN'
t_BETWEEN = r'BETWEEN'
t_LIKE = r'LIKE'
t_CAST = r'CAST'
t_DEFAULT = r'DEFAULT'
t_UNIQUE = r'UNIQUE'
t_AND = r'AND'
t_TRAEME = r'TRAEME'
t_TODO = r'TODO'
t_DONDE = r'DONDE'
t_EN = r'EN'
t_CONTANDO = r'CONTANDO'
t_ACTUALIZA = r'ACTUALIZA'
t_SETEA = r'SETEA'
t_EXISTE = r'EXISTE'
t_ENTRE = r'ENTRE'
t_UNICO = r'UNICO'
t_OR = r'OR'
t_VARCHAR = r'VARCHAR'
t_INT = r'INT'
t_PUNTO = r'\.'
t_SUM = r'SUM'
t_AVG = r'AVG'
t_MIN = r'MIN'
t_MAX = r'MAX'

# Definiciones de operadores compuestos
t_MAYOR_IGUAL = r'>='
t_MENOR_IGUAL = r'<='
t_DIFERENTE = r'!='

# Definiciones de operadores simples
t_MAYOR_QUE = r'>'
t_MENOR_QUE = r'<'
t_IGUAL = r'='

t_COMA = r','
t_PUNTO_Y_COMA = r';'
t_PARENIZQ = r'\('
t_PARENDER = r'\)'

# Reglas para números con coma
def t_FLOAT(t):
    r'\d+,\d+'
    t.value = float(t.value.replace(',', '.'))
    return t

# Reglas para números enteros
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Reglas para strings
def t_STRING(t):
    r'\'(.*?)\''
    t.value = t.value.strip("'")
    return t

# Ignorar comentarios de 1 línea
def t_comment_single_line(t):
    r'--.*'
    pass

# Ignorar comentarios multilínea
def t_comment_multiline(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    pass

# Ignorar espacios y tabulaciones y nueva línea
t_ignore = ' \t'

# Contar número de líneas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Regla para identificadores
def t_ID(t):
    r'([a-zA-Z_][a-zA-Z0-9_]*)|("([^"]+)")|(\[([^\]]+)\])'
    if t.value.startswith('"') and t.value.endswith('"'):
        t.value = t.value[1:-1]
        t.type = 'ID'
    elif t.value.startswith('[') and t.value.endswith(']'):
        t.value = t.value[1:-1]
        t.type = 'ID'
    else:
        value_upper = t.value.upper()
        if value_upper in palabras_reservadas:
            t.type = palabras_reservadas[value_upper]
        else:
            t.type = 'ID'
    return t

# Manejo de errores
def t_error(t):
    print(f"Token no reconocido: {t.value[0]}")
    t.lexer.skip(1)
    
