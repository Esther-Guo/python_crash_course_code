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


user = User('Will', 'Smith', 'Los Angeles')

print(user.login_attempts)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)

user.reset_login_attempts()
print(user.login_attempts)
