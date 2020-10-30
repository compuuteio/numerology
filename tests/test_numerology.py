from numerology import __version__, PythagoreanNumerology
import unittest

class VersionTestCase(unittest.TestCase):
    def test_version(self):
        assert __version__ == '0.2.0'

class PythagoreanTestCase(unittest.TestCase):
    def setUp(self):
        self.name1 = PythagoreanNumerology("Jean-Pierre", "Boisrond", "1958-12-15")
        # self.name2 = PythagoreanNumerology("Michel", "Raynal")
        # self.name3 = PythagoreanNumerology("Muriel", "Darbois")
        
        self.name1.verbose = False
        # self.name2.verbose = False
        # self.name3.verbose = False
        
    def tearDown(self):
        pass
        
    def test_nombre_actif(self):
        self.assertEqual(11, self.name1.nombre_actif)
        # self.assertEqual(5, self.name2.nombre_actif)
        # self.assertEqual(6, self.name3.nombre_actif)
    
    def test_nombre_hereditaire(self):
        self.assertEqual(6, self.name1.nombre_hereditaire)
        # self.assertEqual(8, self.name2.nombre_hereditaire)
        # self.assertEqual(5, self.name3.nombre_hereditaire)
        
    def test_nombre_d_expression(self):
        self.assertEqual(8, self.name1.nombre_d_expression)
        # self.assertEqual(4, self.name2.nombre_d_expression)
        # self.assertEqual(2, self.name3.nombre_d_expression)
        
    def test_nombre_intime(self):
        self.assertEqual(1, self.name1.nombre_intime)
        # self.assertEqual(5, self.name2.nombre_intime)
        # self.assertEqual(6, self.name3.nombre_intime)
        
    def test_de_realisation(self):
        self.assertEqual(7, self.name1.nombre_de_realisation)
        # self.assertEqual(8, self.name2.nombre_de_realisation)
        # self.assertEqual(5, self.name3.nombre_de_realisation)

if __name__ == "__main__":
    unittest.main() # run all tests