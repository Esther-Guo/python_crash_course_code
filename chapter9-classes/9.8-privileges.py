class User:
    def __init__(self, first_name, last_name, location):
        self.name = f'{first_name.title()} {last_name.title()}'
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        name_msg = f"\nThe user's name is {self.name}."
        loc_msg = f"The user is located in {self.location}"
        print(name_msg)
        print(loc_msg)

    def greet_user(self):
        greet_msg = f'Welcome! {self.name}.'
        print(greet_msg)

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    """set privilege instance"""
    def __init__(self):
        """initialize privileges"""
        self.privileges = []

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


admin = Admin('Will', 'Smith', 'Los Angeles')
admin.privileges.privileges = [
    "can add post",
    "can delete post",
    "can ban user",
    ]

admin.privileges.show_privileges()
