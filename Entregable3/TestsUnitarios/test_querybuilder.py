import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from QueryBuilder import QueryBuilder

class TestQueryBuilder(unittest.TestCase):
    def test_select_query(self):
        query = (QueryBuilder()
                 .traeme('nombre', 'edad')
                 .de_la_tabla('usuarios')
                 .donde("edad > 18")
                 .build())
        expected_query = "TRAEME nombre, edad DE LA TABLA usuarios DONDE edad > 18;"
        self.assertEqual(query, expected_query)

    def test_insert_query(self):
        query = (QueryBuilder()
                 .mete_en('usuarios', 'nombre', 'edad')
                 .los_valores("'Juan'", '25')
                 .build())
        expected_query = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        self.assertEqual(query, expected_query)

    def test_update_query(self):
        query = (QueryBuilder()
                 .actualiza('empleados')
                 .setea(salario='3000')
                 .donde("puesto = 'ingeniero'")
                 .build())
        expected_query = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        self.assertEqual(query, expected_query)

    def test_delete_query(self):
        query = (QueryBuilder()
                 .borra_de_la('clientes')
                 .donde("edad ENTRE 18 Y 25")
                 .build())
        expected_query = "BORRA DE LA clientes DONDE edad ENTRE 18 Y 25;"
        self.assertEqual(query, expected_query)

    def test_join_query(self):
        query = (QueryBuilder()
                 .traeme('TODO')
                 .de_la_tabla('pedidos')
                 .mezclando('clientes')
                 .en('pedidos.cliente_id = clientes.id')
                 .donde("clientes.ciudad = 'Barcelona'")
                 .build())
        expected_query = ("TRAEME TODO DE LA TABLA pedidos MEZCLANDO clientes EN "
                          "pedidos.cliente_id = clientes.id DONDE clientes.ciudad = 'Barcelona';")
        self.assertEqual(query, expected_query)
        
    def test_group_by_having_query(self):
        query = (QueryBuilder()
                 .traeme('categoria', 'SUM(precio)')
                 .de_la_tabla('productos')
                 .agrupando_por('categoria')
                 .where_del_group_by('SUM(precio) > 1000')
                 .build())
        expected_query = ("TRAEME categoria, SUM(precio) DE LA TABLA productos "
                          "AGRUPANDO POR categoria WHERE DEL GROUP BY SUM(precio) > 1000;")
        self.assertEqual(query, expected_query)
        
    def test_order_by_limit_query(self):
        query = (QueryBuilder()
                 .traeme('nombre', 'edad')
                 .de_la_tabla('usuarios')
                 .ordena_por('edad')
                 .como_mucho('10')
                 .build())
        expected_query = "TRAEME nombre, edad DE LA TABLA usuarios ORDENA POR edad COMO MUCHO 10;"
        self.assertEqual(query, expected_query)
    
    def test_drop_table_query(self):
        query = (QueryBuilder()
                 .tira_la_tabla('productos')
                 .build())
        expected_query = "TIRA LA TABLA productos;"
        self.assertEqual(query, expected_query)
        
    def test_alter_table_add_drop_column(self):
        query = (QueryBuilder()
                 .cambia_la_tabla('empleados')
                 .agrega_la_columna('direccion VARCHAR(255) NO NULO')
                 .elimina_la_columna('telefono')
                 .build())
        expected_query = ("CAMBIA LA TABLA empleados AGREGA LA COLUMNA direccion VARCHAR(255) NO NULO "
                          "ELIMINA LA COLUMNA telefono;")
        self.assertEqual(query, expected_query)
    
    def test_between_condition_query(self):
        query = (QueryBuilder()
                 .traeme('nombre')
                 .de_la_tabla('clientes')
                 .condicion_entre('edad', '18', '25')
                 .build())
        expected_query = "TRAEME nombre DE LA TABLA clientes DONDE edad ENTRE 18 Y 25;"
        self.assertEqual(query, expected_query)
        
    def test_like_condition_query(self):
        query = (QueryBuilder()
                 .traeme('nombre')
                 .de_la_tabla('clientes')
                 .parecido_a('nombre', 'J%')
                 .build())
        expected_query = "TRAEME nombre DE LA TABLA clientes DONDE nombre PARECIDO A 'J%';"
        self.assertEqual(query, expected_query)
        
    def test_null_conditions_query(self):
        query = (QueryBuilder()
                 .traeme('nombre')
                 .de_la_tabla('clientes')
                 .es_nulo('direccion')
                 .build())
        expected_query = "TRAEME nombre DE LA TABLA clientes DONDE direccion ES NULO;"
        self.assertEqual(query, expected_query)

        query = (QueryBuilder()
                 .traeme('nombre')
                 .de_la_tabla('clientes')
                 .no_nulo('email')
                 .build())
        expected_query = "TRAEME nombre DE LA TABLA clientes DONDE email NO NULO;"
        self.assertEqual(query, expected_query)
        
    def test_from_existing_query(self):
        existing_query = "TRAEME * DE LA TABLA ventas"
        query = (QueryBuilder()
                 .from_existing(existing_query)
                 .donde("fecha > '2022-01-01'")
                 .ordena_por('fecha')
                 .build())
        expected_query = "TRAEME * DE LA TABLA ventas DONDE fecha > '2022-01-01' ORDENA POR fecha;"
        self.assertEqual(query, expected_query)
           
if __name__ == '__main__':
    unittest.main()
