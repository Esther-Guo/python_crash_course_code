import unittest
from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""
    '''Any method that starts with test_ will be run automatically when we
        run test_name_function.py.'''
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        '''Assert methods verify that a result you received matches the result
            you expected to receive.'''
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


'''If this file is being run as the main program, the value of __name__ is set
    to '__main__'.'''
if __name__ == '__main__':
    unittest.main()
