
import unittest

from algoritmos import (
    burbuja,
    merge_sort,
    busqueda_lineal,
    busqueda_binaria
)


class TestAlgoritmos(unittest.TestCase):

    def setUp(self):
        self.datos = [45, 12, 78, 23, 9, 56, 34]
        self.esperado = [9, 12, 23, 34, 45, 56, 78]

    # Pruebas de Bubble Sort
    def test_burbuja(self):
        resultado = burbuja(self.datos)
        self.assertEqual(resultado, self.esperado)

    def test_burbuja_lista_vacia(self):
        self.assertEqual(burbuja([]), [])

    # Pruebas de Merge Sort
    def test_merge_sort(self):
        resultado = merge_sort(self.datos)
        self.assertEqual(resultado, self.esperado)

    def test_merge_sort_lista_vacia(self):
        self.assertEqual(merge_sort([]), [])

    # Pruebas de búsqueda lineal
    def test_busqueda_lineal_elemento_existente(self):
        posicion = busqueda_lineal(self.datos, 78)
        self.assertEqual(posicion, 2)

    def test_busqueda_lineal_elemento_inexistente(self):
        posicion = busqueda_lineal(self.datos, 100)
        self.assertEqual(posicion, -1)

    # Pruebas de búsqueda binaria
    def test_busqueda_binaria_elemento_existente(self):
        datos_ordenados = merge_sort(self.datos)
        posicion = busqueda_binaria(datos_ordenados, 45)
        self.assertEqual(posicion, 4)

    def test_busqueda_binaria_elemento_inexistente(self):
        datos_ordenados = merge_sort(self.datos)
        posicion = busqueda_binaria(datos_ordenados, 100)
        self.assertEqual(posicion, -1)

    # Prueba para comprobar que los algoritmos
    # de ordenamiento no modifican la lista original.
    def test_lista_original_no_se_modifica(self):
        original = self.datos.copy()

        burbuja(self.datos)
        merge_sort(self.datos)

        self.assertEqual(self.datos, original)


if __name__ == "__main__":
    unittest.main()

