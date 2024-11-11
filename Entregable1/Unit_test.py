import unittest
from Principal import control, mostrar_error
from Parte2 import traducir_respuesta, control_respuesta, buscar_opciones, mostrar_pregunta

class TestPrincipal(unittest.TestCase):

    def test_control(self):
        self.assertTrue(control("Empezar"))
        self.assertTrue(control("empezar"))
        self.assertFalse(control("salir"))

    def test_mostrar_error(self):
        self.assertEqual(mostrar_error(), "Salida: entrada incorrecta, por favor ingrese Empezar")

class TestParte2(unittest.TestCase):

    def test_traducir_respuesta(self):
        self.assertEqual(traducir_respuesta('a'), 0)
        self.assertEqual(traducir_respuesta('b'), 1)
        self.assertEqual(traducir_respuesta('c'), 2)

    def test_control_respuesta(self):
        self.assertTrue(control_respuesta('a'))
        self.assertTrue(control_respuesta('b'))
        self.assertTrue(control_respuesta('c'))
        self.assertFalse(control_respuesta('d'))
        self.assertFalse(control_respuesta('1'))

    def test_buscar_opciones(self):
        opciones = buscar_opciones("Geography", 0)
        self.assertEqual(len(opciones), 2)
        self.assertNotIn("Washington", opciones)  # Suponiendo que "Washington" es la respuesta correcta en la fila 0

    def test_mostrar_pregunta(self):
        opciones = mostrar_pregunta(0)
        self.assertEqual(len(opciones), 3)

if __name__ == '__main__':
    unittest.main()