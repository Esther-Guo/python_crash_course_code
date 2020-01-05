import unittest
from city_functions import city_country


class CityTestCase(unittest.TestCase):
    """Test for 'city_functions.py'."""
    def test_city_country(self):
        """Does input like 'santiago chile' works?"""
        formatted_name = city_country('santiago', 'chile')
        self.assertEqual(formatted_name, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
