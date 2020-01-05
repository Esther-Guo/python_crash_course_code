class Employee:
    """Describe an employee"""

    def __init__(self, first_name, last_name, salary):
        """Initialize an employee"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, raise_amount=5000):
        """Add raise amount to annual salary"""
        self.salary += raise_amount
