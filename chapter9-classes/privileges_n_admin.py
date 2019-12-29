"""Store Privileges and Admin class"""
from user_only import User


class Privileges:
    """set privilege instance"""
    def __init__(self):
        """initialize privileges"""
        self.privileges = [
            'can add post',
            'can delete post',
            'can add user',
        ]

    def show_privileges(self):
        """display all the privileges"""
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """define a admin user"""
    def __init__(self, first_name, last_name, location):
        """initialize a admin"""
        super().__init__(first_name, last_name, location)
        self.privileges = Privileges()
