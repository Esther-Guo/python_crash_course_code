class Restaurant:
    """A class representing a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        print(f'{self.restaurant_name.title()} is the name of the restaurant.')
        print(f'The cuisine type of this restaurant is {self.cuisine_type}.')

    def open_restaurant(self):
        """Display a message to say the restaurant is open"""
        print(f'{self.restaurant_name.title()} is now open!')


my_restaurant = Restaurant("Esther's cuisine", "chinese food")
print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
