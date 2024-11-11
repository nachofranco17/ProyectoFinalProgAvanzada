import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
from Lexer.LexerMain import get_lexer, tokenize
from Lexer.Tokens import tokens

class TestLexer(unittest.TestCase):
    def setUp(self):
        self.lexer = get_lexer()

    def test_borra_de_la(self):
        consulta = "BORRA DE LA tabla_clientes DONDE edad ENTRE 18 Y 25;"
        tokens = tokenize(consulta)
        expected_tokens = [
            ('BORRA_DE_LA', 'BORRA DE LA'),
            ('ID', 'tabla_clientes'),
            ('DONDE', 'DONDE'),
            ('ID', 'edad'),
            ('ENTRE', 'ENTRE'),
            ('NUM', 18),
            ('Y', 'Y'),
            ('NUM', 25),
            ('PUNTO_Y_COMA', ';'),
        ]
        self.assertEqual([(tok.type, tok.value) for tok in tokens], expected_tokens)

    def test_traeme_todo_de_la_tabla(self):
        consulta = "TRAEME TODO DE LA TABLA usuarios DONDE edad > 18;"
        tokens = tokenize(consulta)
        expected_tokens = [
            ('TRAEME', 'TRAEME'),
            ('TODO', 'TODO'),
            ('DE_LA_TABLA', 'DE LA TABLA'),
            ('ID', 'usuarios'),
            ('DONDE', 'DONDE'),
            ('ID', 'edad'),
            ('MAYOR_QUE', '>'),
            ('NUM', 18),
            ('PUNTO_Y_COMA', ';'),
        ]
        self.assertEqual([(tok.type, tok.value) for tok in tokens], expected_tokens)
    
    def test_traeme_los_distintos(self):
        consulta = "TRAEME LOS DISTINTOS nombre DE LA TABLA clientes DONDE ciudad = 'Madrid';"
        tokens = tokenize(consulta)
        expected_tokens = [
            ('TRAEME', 'TRAEME'),
            ('LOS_DISTINTOS', 'LOS DISTINTOS'),
            ('ID', 'nombre'),
            ('DE_LA_TABLA', 'DE LA TABLA'),
            ('ID', 'clientes'),
            ('DONDE', 'DONDE'),
            ('ID', 'ciudad'),
            ('IGUAL', '='),
            ('STRING', 'Madrid'),
            ('PUNTO_Y_COMA', ';'),
        ]
        self.assertEqual([(tok.type, tok.value) for tok in tokens], expected_tokens)
        
    def test_mete_en_valores(self):
        consulta = "METE EN usuarios (nombre, edad) LOS VALORES ('Juan', 25);"
        tokens = tokenize(consulta)
        expected_tokens = [
            ('METE_EN', 'METE EN'),
            ('ID', 'usuarios'),
            ('PARENIZQ', '('),
            ('ID', 'nombre'),
            ('COMA', ','),
            ('ID', 'edad'),
            ('PARENDER', ')'),
            ('LOS_VALORES', 'LOS VALORES'),
            ('PARENIZQ', '('),
            ('STRING', 'Juan'),
            ('COMA', ','),
            ('NUM', 25),
            ('PARENDER', ')'),
            ('PUNTO_Y_COMA', ';'),
        ]
        self.assertEqual([(tok.type, tok.value) for tok in tokens], expected_tokens)
        
    def test_actualiza_setea(self):
        consulta = "ACTUALIZA empleados SETEA salario = 3000 DONDE puesto = 'ingeniero';"
        tokens = tokenize(consulta)
        expected_tokens = [
            ('ACTUALIZA', 'ACTUALIZA'),
            ('ID', 'empleados'),
            ('SETEA', 'SETEA'),
            ('ID', 'salario'),
            ('IGUAL', '='),
            ('NUM', 3000),
            ('DONDE', 'DONDE'),
            ('ID', 'puesto'),
            ('IGUAL', '='),
            ('STRING', 'ingeniero'),
            ('PUNTO_Y_COMA', ';'),
        ]
        self.assertEqual([(tok.type, tok.value) for tok in tokens], expected_tokens)
        
    def test_crea_la_tabla(self):
        consulta = """CREA LA TABLA productos (
            id INT CLAVE PRIMA,
            nombre VARCHAR(100) UNICO,
            precio INT POR DEFECTO 0,
            categoria VARCHAR(50) NO NULO
        );"""
        tokens = tokenize(consulta)
        expected_tokens = [
            ('CREA_LA_TABLA', 'CREA LA TABLA'),
            ('ID', 'productos'),
            ('PARENIZQ', '('),
            ('ID', 'id'),
            ('INT', 'INT'),
            ('CLAVE_PRIMA', 'CLAVE PRIMA'),
            ('COMA', ','),
            ('ID', 'nombre'),
            ('VARCHAR', 'VARCHAR'),
            ('PARENIZQ', '('),
            ('NUM', 100),
            ('PARENDER', ')'),
            ('UNICO', 'UNICO'),
            ('COMA', ','),
            ('ID', 'precio'),
            ('INT', 'INT'),
            ('POR_DEFECTO', 'POR DEFECTO'),
            ('NUM', 0),
            ('COMA', ','),
            ('ID', 'categoria'),
            ('VARCHAR', 'VARCHAR'),
            ('PARENIZQ', '('),
            ('NUM', 50),
            ('PARENDER', ')'),
            ('NO_NULO', 'NO NULO'),
            ('PARENDER', ')'),
            ('PUNTO_Y_COMA', ';'),
        ]
        self.assertEqual([(tok.type, tok.value) for tok in tokens], expected_tokens)
        
    
    def test_tira_la_tabla(self):
        consulta = "TIRA LA TABLA productos;"
        tokens = tokenize(consulta)
        expected_tokens = [
            ('TIRA_LA_TABLA', 'TIRA LA TABLA'),
            ('ID', 'productos'),
            ('PUNTO_Y_COMA', ';'),
        ]
        self.assertEqual([(tok.type, tok.value) for tok in tokens], expected_tokens)
        
    def test_contando_group_by(self):
        consulta = "TRAEME CONTANDO(*) DE LA TABLA ventas AGRUPANDO POR producto WHERE DEL GROUP BY CONTANDO(*) > 5;"
        tokens = tokenize(consulta)
        expected_tokens = [
            ('TRAEME', 'TRAEME'),
            ('CONTANDO', 'CONTANDO'),
            ('PARENIZQ', '('),
            ('ASTERISCO', '*'),
            ('PARENDER', ')'),
            ('DE_LA_TABLA', 'DE LA TABLA'),
            ('ID', 'ventas'),
            ('AGRUPANDO_POR', 'AGRUPANDO POR'),
            ('ID', 'producto'),
            ('WHERE_DEL_GROUP_BY', 'WHERE DEL GROUP BY'),
            ('CONTANDO', 'CONTANDO'),
            ('PARENIZQ', '('),
            ('ASTERISCO', '*'),
            ('PARENDER', ')'),
            ('MAYOR_QUE', '>'),
            ('NUM', 5),
            ('PUNTO_Y_COMA', ';'),
        ]
        self.assertEqual([(tok.type, tok.value) for tok in tokens], expected_tokens)
        
    def test_traeme_nombre_edad_order_by(self):
        consulta = "TRAEME nombre, edad DE LA TABLA usuarios DONDE edad >= 21 OR ciudad PARECIDO A 'Montevideo%' ORDENA POR edad COMO MUCHO 10;"
        tokens = tokenize(consulta)
        expected_tokens = [
            ('TRAEME', 'TRAEME'),
            ('ID', 'nombre'),
            ('COMA', ','),
            ('ID', 'edad'),
            ('DE_LA_TABLA', 'DE LA TABLA'),
            ('ID', 'usuarios'),
            ('DONDE', 'DONDE'),
            ('ID', 'edad'),
            ('MAYOR_IGUAL', '>='),
            ('NUM', 21),
            ('OR', 'OR'),
            ('ID', 'ciudad'),
            ('PARECIDO_A', 'PARECIDO A'),
            ('STRING', 'Montevideo%'),
            ('ORDENA_POR', 'ORDENA POR'),
            ('ID', 'edad'),
            ('COMO_MUCHO', 'COMO MUCHO'),
            ('NUM', 10),
            ('PUNTO_Y_COMA', ';'),
        ]
        self.assertEqual([(tok.type, tok.value) for tok in tokens], expected_tokens)
     
if __name__ == '__main__':
    unittest.main()
