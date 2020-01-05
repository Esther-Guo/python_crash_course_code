import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Create an employee and test the salary methods"""
        self.my_employee = Employee('Esther', 'G', 100000)

    def test_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary, 105000)

    def test_given_raise(self):
        self.my_employee.give_raise(7000)
        self.assertEqual(self.my_employee.salary, 107000)


if __name__ == '__main__':
    unittest.main()
