from TraductorConsultas import translate_usql_to_sql, TranslationError, separacion
from Lexer.LexerMain import get_lexer

class QueryBuilder:
    def __init__(self):
        self.parts = {
            'command': '',
            'columns': '',
            'table': '',
            'values': '',
            'set': '',
            'join': '',
            'on': '',
            'where': '',
            'group_by': '',
            'having': '',
            'order_by': '',
            'limit': '',
            'alter_table': '',
            'add_column': '',
            'drop_column': '',
            'create_table': '',
            'drop_table': '',
            'existing_query': '',
        }
        
    def traeme(self, *columns):
        if columns:
            columns_str = ', '.join(columns)
            self.parts['columns'] = columns_str
        else:
            self.parts['columns'] = 'TODO'
        self.parts['command'] = 'TRAEME'
        return self
    
    def de_la_tabla(self, table_name):
        self.parts['table'] = f'DE LA TABLA {table_name}'
        return self
    
    def donde(self, condition):
        if self.parts['where']:
            self.parts['where'] += f' Y {condition}'
        else:
            self.parts['where'] = f'DONDE {condition}'
        return self
    
    def agrupando_por(self, *columns):
        columns_str = ', '.join(columns)
        self.parts['group_by'] = f'AGRUPANDO POR {columns_str}'
        return self
    
    def where_del_group_by(self, condition):
        self.parts['having'] = f'WHERE DEL GROUP BY {condition}'
        return self
    
    def mezclando(self, table_name):
        self.parts['join'] = f'MEZCLANDO {table_name}'
        return self
    
    def en(self, condition):
        self.parts['on'] = f'EN {condition}'
        return self
    
    def los_distintos(self):
        if self.parts['columns']:
            self.parts['columns'] = f'LOS DISTINTOS {self.parts["columns"]}'
        else:
            self.parts['columns'] = 'LOS DISTINTOS TODO'
        return self
    
    def contando(self, column='*'):
        self.parts['columns'] = f'CONTANDO({column})'
        return self
    
    def mete_en(self, table_name, *columns):
        columns_str = ', '.join(columns)
        self.parts['command'] = f'METE EN {table_name} ({columns_str})'
        return self
    
    def los_valores(self, *values):
        values_str = ', '.join(values)
        self.parts['values'] = f'LOS VALORES ({values_str})'
        return self
    
    def actualiza(self, table_name):
        self.parts['command'] = f'ACTUALIZA {table_name}'
        return self
    
    def setea(self, **assignments):
        assignments_str = ', '.join(f"{k} = {v}" for k, v in assignments.items())
        self.parts['set'] = f'SETEA {assignments_str}'
        return self
    
    def borra_de_la(self, table_name):
        self.parts['command'] = f'BORRA DE LA {table_name}'
        return self
    
    def ordena_por(self, *columns):
        columns_str = ', '.join(columns)
        self.parts['order_by'] = f'ORDENA POR {columns_str}'
        return self
    
    def como_mucho(self, limit_value):
        self.parts['limit'] = f'COMO MUCHO {limit_value}'
        return self
    
    def crea_la_tabla(self, table_name):
        self.parts['create_table'] = f'CREA LA TABLA {table_name}'
        return self
    
    def tira_la_tabla(self, table_name):
        self.parts['drop_table'] = f'TIRA LA TABLA {table_name}'
        return self
    
    def cambia_la_tabla(self, table_name):
        self.parts['alter_table'] = f'CAMBIA LA TABLA {table_name}'
        return self
    
    def agrega_la_columna(self, column_definition):
        if self.parts['add_column']:
            self.parts['add_column'] += f', {column_definition}'
        else:
            self.parts['add_column'] = f'AGREGA LA COLUMNA {column_definition}'
        return self
    
    def elimina_la_columna(self, column_name):
        self.parts['drop_column'] = f'ELIMINA LA COLUMNA {column_name}'
        return self
    
    def condicion_entre(self, column, val1, val2):
        condition = f"{column} ENTRE {val1} Y {val2}"
        self.donde(condition)
        return self
    
    def parecido_a(self, column, pattern):
        condition = f"{column} PARECIDO A '{pattern}'"
        self.donde(condition)
        return self
    
    def es_nulo(self, column):
        condition = f"{column} ES NULO"
        self.donde(condition)
        return self
    
    def no_nulo(self, column):
        condition = f"{column} NO NULO"
        self.donde(condition)
        return self
        
    def select(self, *columns):
        if columns:
            columns_str = ', '.join(columns)
        else:
            columns_str = 'TODO'
        self.parts['command'] = 'TRAEME'
        self.parts['columns'] = columns_str
        return self
    
    def from_table(self, table_name):
        self.parts['table'] = f'DE LA TABLA {table_name}'
        return self
    
    def where(self, condition):
        if self.parts['where']:
            self.parts['where'] += f' Y {condition}'
        else:
            self.parts['where'] = f'DONDE {condition}'
        return self
    
    def join(self, table_name, on_condition):
        self.parts['join'] = f'MEZCLANDO {table_name}'
        self.parts['on'] = f'EN {on_condition}'
        return self
    
    def group_by(self, *columns):
        columns_str = ', '.join(columns)
        self.parts['group_by'] = f'AGRUPANDO POR {columns_str}'
        return self
    
    def having(self, condition):
        self.parts['having'] = f'WHERE DEL GROUP BY {condition}'
        return self
    
    def order_by(self, *columns):
        columns_str = ', '.join(columns)
        self.parts['order_by'] = f'ORDENA POR {columns_str}'
        return self
    
    def limit(self, limit_value):
        self.parts['limit'] = f'COMO MUCHO {limit_value}'
        return self
    
    def from_existing(self, existing_query):
        self.parts['existing_query'] = existing_query.strip(';')
        return self
    
    def build(self):
        if self.parts['existing_query']:
            base_query = self.parts['existing_query']
            additional_parts = [
                self.parts['where'],
                self.parts['group_by'],
                self.parts['having'],
                self.parts['order_by'],
                self.parts['limit'],
                self.parts['values'],
            ]
            additional_query = ' '.join(part for part in additional_parts if part)
            if additional_query:
                query = f"{base_query} {additional_query}"
            else:
                query = f"{base_query}"
        elif self.parts['command']:
            query_parts = [
                self.parts['command'],
                self.parts['columns'],
                self.parts['table'],
                self.parts['join'],
                self.parts['on'],
                self.parts['set'],
                self.parts['where'],
                self.parts['group_by'],
                self.parts['having'],
                self.parts['order_by'],
                self.parts['limit'],
                self.parts['values'],
            ]
            query = ' '.join(part for part in query_parts if part)
            query = query.strip() + ';'
        elif self.parts['create_table']:
            query_parts = [
                self.parts['create_table'],
                self.parts['columns'],
            ]
            query = ' '.join(part for part in query_parts if part)
            query = query.strip()
        elif self.parts['alter_table']:
            query_parts = [
                self.parts['alter_table'],
                self.parts['add_column'],
                self.parts['drop_column'],
            ]
            query = ' '.join(part for part in query_parts if part)
            query = query.strip()
        elif self.parts['drop_table']:
            query_parts = [
                self.parts['drop_table'],
            ]
            query = ' '.join(part for part in query_parts if part)
            query = query.strip()
        else:
            query = ''
        
        return query.rstrip(';') + ';'
    
#Probando la Fluent Interface

queries = []

query1 = (QueryBuilder()
         .select('nombre', 'edad')
         .from_table('usuarios')
         .where("edad > 18")
         .order_by('nombre')
         .build())
queries.append(query1)

#Tomando una consulta ya existente y agregando filtros
existing_query = "TRAEME * DE LA TABLA productos"

query2 = (QueryBuilder()
         .from_existing(existing_query)
         .where("precio < 100")
         .order_by('nombre')
         .build())
queries.append(query2)

query3 = (QueryBuilder()
         .select('*')
         .from_table('clientes')
         .where("ciudad = 'Madrid'")
         .where("edad >= 30")
         .build())
queries.append(query3)

query4 = (QueryBuilder()
         .traeme('LOS DISTINTOS nombre')
         .de_la_tabla('clientes')
         .donde("ciudad = 'Madrid'")
         .ordena_por('nombre')
         .build())
queries.append(query4)

query5 = (QueryBuilder()
         .mete_en('usuarios', 'nombre', 'edad')
         .los_valores("'Juan'", '25')
         .build())
queries.append(query5)

query6 = (QueryBuilder()
         .actualiza('empleados')
         .setea(salario='3000')
         .donde("puesto = 'ingeniero'")
         .build())
queries.append(query6)

query7 = (QueryBuilder()
         .borra_de_la('clientes')
         .donde("edad ENTRE 18 Y 25")
         .build())
queries.append(query7)

query8 = (QueryBuilder()
         .traeme('TODO')
         .de_la_tabla('pedidos')
         .mezclando('clientes')
         .en('pedidos.cliente_id = clientes.id')
         .donde("clientes.ciudad = 'Barcelona'")
         .build())
queries.append(query8)

# Construyendo las consultas en SQL y USQL 
for idx, query in enumerate(queries, start=1):
    try:
        print(f"Consulta {idx}")
        sql_query = translate_usql_to_sql(query)
    except TranslationError as e:
        print(separacion)
        print(f"Error en la traducción de la Consulta {idx}:")
        print(e)
        print(separacion)
    






