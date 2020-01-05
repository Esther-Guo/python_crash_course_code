import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""
    def test_city_country(self):
        """Does input like 'santiago chile' work?"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does input like 'santiago chile 5000000' work?"""
        formatted_name = city_country('santiago', 'chile', 5000000)
        self.assertEqual(
            formatted_name,
            'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
