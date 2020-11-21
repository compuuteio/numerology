from numerology import __version__, PythagoreanNumerology
import unittest

# Use the command below to run tests
# python -m unittest tests/test_numerology.py 

class VersionTestCase(unittest.TestCase):
    def test_version(self):
        assert __version__ == '0.5.1'

class PythagoreanTestCase(unittest.TestCase):
    def setUp(self):
        self.name1 = PythagoreanNumerology("Jean-Pierre", "Boisrond", "1958-12-15")
        
    def tearDown(self):
        pass
    
    def test_first_name(self):
        self.assertEqual("Jean-Pierre", self.name1.key_figures['first_name'])
    
    def test_last_name(self):
        self.assertEqual("Boisrond", self.name1.key_figures['last_name'])
    
    def test_birthday(self):
        self.assertEqual("1958-12-15", self.name1.key_figures['birthdate'])
        
    def test_hearth_desire_number(self):
        self.assertEqual(1, self.name1.key_figures['hearth_desire_number'])
        
    def test_personality_number(self):
        self.assertEqual(7, self.name1.key_figures['personality_number'])
        
    def test_active_number(self):
        self.assertEqual(2, self.name1.key_figures['active_number'])
    
    def test_legacy_number(self):
        self.assertEqual(6, self.name1.key_figures['legacy_number'])
        
    def test_life_path_number(self):
        self.assertEqual(5, self.name1.key_figures['life_path_number'])
        
    def test_life_path_number_alternative(self):
        self.assertEqual(5, self.name1.key_figures['life_path_number_alternative'])
        
    def test_full_name_numbers(self):
        self.assertEqual({1: 3, 2: 1, 4: 1, 5: 5, 6: 2, 7: 1, 9: 5}, self.name1.key_figures['full_name_numbers'])
        
    def test_full_name_missing_numbers(self):
        self.assertEqual((3, 8), self.name1.key_figures['full_name_missing_numbers'])
        
    def test_birthdate_day_num(self):
        self.assertEqual(6, self.name1.key_figures['birthdate_day_num'])
        
    def test_birthdate_month_num(self):
        self.assertEqual(3, self.name1.key_figures['birthdate_month_num'])
        
    def test_birthdate_year_num(self):
        self.assertEqual(5, self.name1.key_figures['birthdate_year_num'])
        
    def test_birthdate_year_num_alternative(self):
        self.assertEqual(4, self.name1.key_figures['birthdate_year_num_alternative'])

    # Power Number not implemented so far.
    
if __name__ == "__main__":
    unittest.main()