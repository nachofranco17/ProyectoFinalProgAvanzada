from Lexer.LexerMain import get_lexer
from ParserSQL import parse_sql
from Excepciones import TranslationError
import re

separacion = "-------------------------------------------"

sql_to_usql = {
    'SELECT': 'TRAEME',
    '*': 'TODO',
    'FROM': 'DE LA TABLA',
    'HAVING': 'WHERE DEL GROUP BY',
    'WHERE': 'DONDE',
    'GROUP BY': 'AGRUPANDO POR',
    'JOIN': 'MEZCLANDO',
    'ON': 'EN',
    'DISTINCT': 'LOS DISTINTOS',
    'COUNT': 'CONTANDO',
    'INSERT INTO': 'METE EN',
    'VALUES': 'LOS VALORES',
    'UPDATE': 'ACTUALIZA',
    'SET': 'SETEA',
    'DELETE FROM': 'BORRA DE LA',
    'ORDER BY': 'ORDENA POR',
    'LIMIT': 'COMO MUCHO',
    'EXISTS': 'EXISTE',
    'BETWEEN': 'ENTRE',
    'LIKE': 'PARECIDO A',
    'IS NULL': 'ES NULO',
    'NOT NULL': 'NO NULO',
    'ALTER TABLE': 'CAMBIA LA TABLA',
    'ADD COLUMN': 'AGREGA LA COLUMNA',
    'DROP COLUMN': 'ELIMINA LA COLUMNA',
    'CREATE TABLE': 'CREA LA TABLA',
    'DROP TABLE': 'TIRA LA TABLA',
    'DEFAULT': 'POR DEFECTO',
    'UNIQUE': 'UNICO',
    'PRIMARY KEY': 'CLAVE PRIMA',
    'FOREIGN KEY': 'CLAVE REFERENTE',
    'CAST': 'TRANSFORMA A',
    'AND': 'Y',
    'OR': 'O',
    'IN': 'EN ESTO:',
    'VARCHAR': 'VARCHAR',
    'INT': 'INT',
}


usql_to_sql = {v: k for k, v in sql_to_usql.items()}

aggregations = {'COUNT', 'SUM', 'AVG', 'MIN', 'MAX'}

def translate_query(usql_query, translation_dict):
    lexer = get_lexer()
    lexer.input(usql_query)
    tokens = list(lexer)  # Obtener todos los tokens en una lista

    translated_tokens = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        token_value = token.value
        token_type = token.type

        if token.type == 'STRING':
            translated_tokens.append(f"'{token_value}'")
            i += 1
            continue
        elif token.type == 'NUM':
            translated_tokens.append(str(token_value))
            i += 1
            continue
        else:
            token_str = str(token_value)
            token_upper = token_str.upper()

            if token_upper in translation_dict:
                translated_token = translation_dict[token_upper]
                # Verificar si el siguiente token es '('
                if (i + 1) < len(tokens) and tokens[i + 1].type == 'PARENIZQ':
                    if translated_token in aggregations:
                        # Append 'COUNT(' sin espacio
                        translated_tokens.append(f"{translated_token}(")
                        i += 2  # Saltar '('
                        continue
                    else:
                        # Append 'FUNC (' con espacio
                        translated_tokens.append(f"{translated_token} (")
                        i += 2  # Saltar '('
                        continue
                else:
                    translated_tokens.append(translated_token)
            else:
                # Append tal cual
                translated_tokens.append(token_str)
        i += 1

    # Ahora, ensamblar la consulta final con espacios adecuados
    final_query = ''
    for j, t in enumerate(translated_tokens):
        if j > 0:
            # No agregar espacio antes de ciertos tokens
            if t in {')', ',', ';'}:
                pass  # No espacio antes de ')', ',', ';'
            elif translated_tokens[j-1].endswith('('):
                pass  # No espacio después de '('
            else:
                final_query += ' '
        final_query += t

    # Opcional: Limpiar espacios innecesarios
    final_query = re.sub(r'\s+', ' ', final_query).strip()

    return final_query

def translate_usql_to_sql(usql_query):
    sql_query = translate_query(usql_query, usql_to_sql)
    print("USQL Query:", usql_query)
    print("\nSQL Query traducida:", sql_query)
    
    try:
        parse_sql(sql_query)
        print("La consulta es válida y fue traducida correctamente.\n" + separacion)
    except SyntaxError as e:
        raise TranslationError(f"Consulta SQL inválida: {e}")
    return sql_query

def translate_sql_to_usql(sql_query):
    return translate_query(sql_query, sql_to_usql)

if __name__ == "__main__":
    consultas_usql = [
        "TRAEME CONTANDO(*) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY CONTANDO(*) > 5;",
        "BORRA DE LA tabla_clientes DONDE edad ENTRE 18 Y 25;",
        "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;",
        "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';",
        "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);",
        "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';",
        "TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';",
        "CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO;",
        "CAMBIA LA TABLA empleados ELIMINA LA COLUMNA direccion;"
    ]

    for usql_query in consultas_usql:
        try:
            sql_query = translate_usql_to_sql(usql_query)
        except TranslationError as e:
            print(separacion)
            


