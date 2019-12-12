class Restaurant:
    """A class representing a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        print(f'{self.restaurant_name.title()} is the name of the restaurant.')
        print(f'The cuisine type of this restaurant is {self.cuisine_type}.')

    def open_restaurant(self):
        """Display a message to say the restaurant is open"""
        print(f'{self.restaurant_name.title()} is now open!')

    def set_number_served(self, number_served):
        """Set the value of number_served"""
        self.number_served = number_served

    def increment_number_served(self, increment):
        """Add certain value to number_served"""
        self.number_served += increment


restaurant = Restaurant("Esther's cuisine", "chinese food")
print(restaurant.number_served)

restaurant.number_served = 10
print(restaurant.number_served)

restaurant.set_number_served(20)
print(restaurant.number_served)

restaurant.increment_number_served(40)
print(restaurant.number_served)
