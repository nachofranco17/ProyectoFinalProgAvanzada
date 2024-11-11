

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from TraductorConsultas import translate_usql_to_sql, TranslationError

class TestTraductor(unittest.TestCase):
    def test_translate_select(self):
        usql_query = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        sql_query = translate_usql_to_sql(usql_query)
        expected_sql = "SELECT * FROM usuarios WHERE edad > 18;"
        self.assertEqual(sql_query, expected_sql)

    def test_translate_invalid(self):
        usql_query = "TRAEME DE LA TABLA usuarios DONDE edad > 18;"
        with self.assertRaises(TranslationError):
            translate_usql_to_sql(usql_query)

    def test_translate_insert(self):
        usql_query = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        sql_query = translate_usql_to_sql(usql_query)
        expected_sql = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);"
        self.assertEqual(sql_query, expected_sql)

    def test_translate_update(self):
        usql_query = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        sql_query = translate_usql_to_sql(usql_query)
        expected_sql = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero';"
        self.assertEqual(sql_query, expected_sql)

    def test_translate_delete(self):
        usql_query = "BORRA DE LA clientes DONDE edad ENTRE 18 Y 25;"
        sql_query = translate_usql_to_sql(usql_query)
        expected_sql = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25;"
        self.assertEqual(sql_query, expected_sql)

                                          
if __name__ == '__main__':
    unittest.main()
