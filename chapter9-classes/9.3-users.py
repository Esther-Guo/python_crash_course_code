class User:
    def __init__(self, first_name, last_name, location):
        self.name = f'{first_name.title()} {last_name.title()}'
        self.location = location.title()

    def describe_user(self):
        name_msg = f"\nThe user's name is {self.name}."
        loc_msg = f"The user is located in {self.location}"
        print(name_msg)
        print(loc_msg)

    def greet_user(self):
        greet_msg = f'Welcome! {self.name}.'
        print(greet_msg)


user_1 = User('Will', 'Smith', 'Los Angeles')
user_2 = User('Esther', 'G', 'Perth')

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()
