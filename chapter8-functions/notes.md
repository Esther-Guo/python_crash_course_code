**docstring**: a comment which describes what the function does. Enclosed in triple quotes, which Python looks for when it generates documentation for the functions in your programs.  
parameter：形参, argument：实参  
key-value pair as argument: animal_type='hamster', pet_name='harry'  
When writing a function, you can define a default value for each parameter. When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. eg.
`def describe_pet(pet_name, animal_type='dog'):`
In conditional tests, None evaluates to False.  
When you pass a list to a function, the function can modify the list. To keep the original list, you can send a copy of the list to the function.
`function_name(list_name[:])`
Python allows a function to collect an arbitrary number of arguments from the calling statement. eg. def make_pizza(*toppings): Here this *toppings parameter collects as many arguments as the calling line provides. The asterisk* tells python to make an empty tuple called toppings and pack whatever values it receives into this tuple.  
The generic parameter name *args is used to collect arbitrary positional arguments.  
The double asterisks before the parameter **user_info cause Python to create an empty dictionary called user_info and pack whatever name-value pairs it receives into this dictionary. eg.
```
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')
```
The parameter name **kwargs is used to collect non-specific keyword arguments.