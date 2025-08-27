import unittest
from main import es_par

class TestParImpar(unittest.TestCase):

    def test_numero_par(self):
        self.assertTrue(es_par(2))
        self.assertTrue(es_par(100))
        self.assertTrue(es_par(0))

    def test_numero_impar(self):
        self.assertFalse(es_par(1))
        self.assertFalse(es_par(99))
        self.assertFalse(es_par(-3))

if __name__ == "__main__":
    unittest.main()
