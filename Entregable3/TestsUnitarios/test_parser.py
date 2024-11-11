import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from ParserSQL import parse_sql, parser
from Lexer.LexerMain import get_lexer

class TestParser(unittest.TestCase):
    #def test_delete_statement(self):
    #    consulta_sql = "DELETE FROM clientes WHERE edad BETWEEN 18 AND 25;"
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = ('DELETE', 'clientes', ('BETWEEN', 'edad', 18, 25))
    #    self.assertEqual(parse_tree, expected_tree)
        
    def test_select_all(self):
        consulta_sql = "SELECT * FROM usuarios WHERE edad > 18;"
        parse_tree = parse_sql(consulta_sql)
        expected_tree = (
            'SELECT',
            None,  # opt_distinct
            '*',  # select_list
            ['usuarios'],  # table_list
            None,  # opt_join_clause
            ('edad', '>', 18),  # opt_where_clause
            None,  # opt_group_by_clause
            None,  # opt_having_clause
            None,  # opt_order_by_clause
        )
        self.assertEqual(parse_tree, expected_tree)
            
    #def test_select_distinct(self):
    #    consulta_sql = "SELECT DISTINCT nombre FROM clientes WHERE ciudad = 'Madrid';"
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = (
    #        'SELECT',
    #        'DISTINCT',  # opt_distinct
    #        ['nombre'],  # select_list
    #        ['clientes'],  # table_list
    #        None,  # opt_join_clause
    #        ('ciudad', '=', 'Madrid'),  # opt_where_clause
    #        None,  # opt_group_by_clause
    #        None,  # opt_having_clause
    #        None,  # opt_order_by_clause
    #        ';'  # PUNTO_Y_COMA
    #    )
    #    self.assertEqual(parse_tree, expected_tree)
#
    #def test_insert_statement(self):
    #    consulta_sql = "INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 25);"
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = (
    #        'INSERT',
    #        'usuarios',  # identifier
    #        ['nombre', 'edad'],  # column_list
    #        ['Juan', 25]  # value_list
    #    )
    #    self.assertEqual(parse_tree, expected_tree)
#
    #def test_update_statement(self):
    #    consulta_sql = "UPDATE empleados SET salario = 3000 WHERE puesto = 'ingeniero';"
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = (
    #        'UPDATE',
    #        'empleados',  # identifier
    #        [('salario', 3000)],  # assignment_list
    #        ('puesto', '=', 'ingeniero')  # opt_where_clause
    #    )
    #    self.assertEqual(parse_tree, expected_tree)
#
    #def test_alter_table_add_column(self):
    #    consulta_sql = "ALTER TABLE empleados ADD COLUMN direccion VARCHAR(255) NOT NULL;"
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = (
    #        'ALTER_TABLE_ADD',
    #        'empleados',  # identifier
    #        ('direccion', ('VARCHAR', 255), ['NOT NULL'])  # column_definition
    #    )
    #    self.assertEqual(parse_tree, expected_tree)
    #    
    #def test_alter_table_drop_column(self):
    #    consulta_sql = "ALTER TABLE empleados DROP COLUMN direccion;"
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = (
    #        'ALTER_TABLE_DROP',
    #        'empleados',  # identifier
    #        'direccion'  # identifier
    #    )
    #    self.assertEqual(parse_tree, expected_tree)
    #    
    #def test_create_table(self):
    #    consulta_sql = """CREATE TABLE productos (
    #        id INT PRIMARY_KEY,
    #        nombre VARCHAR(100) UNIQUE,
    #        precio INT DEFAULT 0,
    #        categoria VARCHAR(50) NOT NULL
    #    );"""
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = (
    #        'CREATE_TABLE',
    #        'productos',  # identifier
    #        [
    #            ('id', 'INT', ['PRIMARY_KEY']),
    #            ('nombre', ('VARCHAR', 100), ['UNIQUE']),
    #            ('precio', 'INT', ['DEFAULT']),
    #            ('categoria', ('VARCHAR', 50), ['NOT NULL'])
    #        ]  # column_definition list
    #    )
    #    self.assertEqual(parse_tree, expected_tree)
    #    
    #def test_drop_table(self):
    #    consulta_sql = "DROP TABLE productos;"
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = (
    #        'DROP_TABLE',
    #        'productos',  # identifier
    #        ';'  # PUNTO_Y_COMA
    #    )
    #    self.assertEqual(parse_tree, expected_tree)
    #    
    #def test_select_count_group_by_having(self):
    #    consulta_sql = "SELECT COUNT(*) FROM ventas GROUP BY producto HAVING COUNT(*) > 5;"
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = (
    #        'SELECT',
    #        None,  # opt_distinct
    #        [('COUNT', '*')],  # select_list
    #        ['ventas'],  # table_list
    #        None,  # opt_join_clause
    #        None,  # opt_where_clause
    #        ('GROUP_BY', ['producto']),  # opt_group_by_clause
    #        ('HAVING', ('COUNT', '*', '>', 5)),  # opt_having_clause
    #        None,  # opt_order_by_clause
    #        ';'  # PUNTO_Y_COMA
    #    )
    #    self.assertEqual(parse_tree, expected_tree)
    #    
    #def test_select_with_order_by_and_limit(self):
    #    consulta_sql = "SELECT nombre, edad FROM usuarios WHERE edad >= 21 OR ciudad LIKE 'Montevideo%' ORDER BY edad LIMIT 10;"
    #    parse_tree = parse_sql(consulta_sql)
    #    expected_tree = (
    #        'SELECT',
    #        None,  # opt_distinct
    #        ['nombre', 'edad'],  # select_list
    #        ['usuarios'],  # table_list
    #        None,  # opt_join_clause
    #        ('OR', ('>=', 'edad', 21), ('LIKE', 'ciudad', 'Montevideo%')),  # opt_where_clause
    #        None,  # opt_group_by_clause
    #        None,  # opt_having_clause
    #        ('ORDER_BY', ['edad']),  # opt_order_by_clause
    #        ';'  # PUNTO_Y_COMA
    #    )
    #    self.assertEqual(parse_tree, expected_tree)

if __name__ == '__main__':
    unittest.main()
