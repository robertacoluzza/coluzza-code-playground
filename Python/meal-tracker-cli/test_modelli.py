import unittest
from modelli import Bambino, DatoNonValido


class TestBambino(unittest.TestCase):

    def test_bambino_nuovo_ha_conteggi_a_zero(self):
        anna = Bambino("Anna")
        self.assertEqual(sum(anna.conteggi().values()), 0)

    def test_giorno_non_valido(self):
        anna = Bambino("Anna")
        with self.assertRaises(DatoNonValido):
            anna.aggiungi_pasto("funedi", "pranzo", "pesce")

    def test_categoria_terminata(self):
        anna = Bambino("Anna")
        anna.aggiungi_pasto("lunedi", "pranzo", "carne-bianca")
        anna.aggiungi_pasto("martedi", "cena", "carne-bianca")
        self.assertEqual(anna.conteggi()["carne-bianca"], 2)
        self.assertNotIn("carne-bianca", anna.mancanti())

    def test_categoria_non_valida(self):
        anna = Bambino("Anna")
        with self.assertRaises(DatoNonValido):
            anna.aggiungi_pasto("lunedi", "pranzo", "pizza")

    def test_suggerimento_nuovo_bambino(self):
        nuovo_bambino = Bambino("Alessio")
        suggerimento = nuovo_bambino.suggerimento()
        self.assertEqual(suggerimento, ["legumi", "carne-bianca"]) 


if __name__ == "__main__":
    unittest.main()