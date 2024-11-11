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
           
if __name__ == '__main__':
    unittest.main()
