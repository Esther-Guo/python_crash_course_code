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


class IceCreamStand(Restaurant):
    """Represent an ice cream stand"""
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Initialize an ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = []

    def show_flavor(self):
        for flavor in self.flavor:
            print(flavor)


icecream_stand = IceCreamStand("Esther's ice cream stand")
icecream_stand.flavor = ['strawberry', 'mango', 'chocolate']
icecream_stand.show_flavor()
