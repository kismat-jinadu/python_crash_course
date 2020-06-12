import unittest
from city_functions import get_formatted_city

class PlacesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py"""

    def test_city_country(self):
        """Do places like Paris, France work?"""
        formatted_city = get_formatted_city('paris','france')
        self.assertEqual(formatted_city, 'Paris, France')

    def test_city_country_population(self):
        """Do places like Paris, France - population 2100000 work"""
        formatted_city = get_formatted_city('paris','france','2100000')
        self.assertEqual(formatted_city, 'Paris, France - Population 2100000')

if __name__ == '__main__':
    unittest.main()