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
To make the main program easier, You can store your functions in a separate file called a module and then importing that module into your main program.  
A module is a file ending in .py that contains the code you want to import into your program.  
import a entire module: import mudule_name  use: module_name.function_name()
impirt specific functions from a module: from module_name import function_name  use: function_name()  
from module_name import function_name as nickname  use: nickname()  
If you specify a default value for a parameter, no spaces should be used on either side of the equal sign: def function_name(parameter_0, parameter_1='default value')  
If a set of parameters causes a function’s definition to
be longer than 79 characters, press enter after the opening parenthesis on the definition line. On the next line, press tab twice to separate the list of arguments from the body of the function, which only indented once.
```
def function_name(
        parameter_0, parameter_1, parameter_2,
        parameter_3, parameter_4, parameter_5):
    function body...
```
Separate function definitions by two blank lines to make it easier to see where one function
ends and the next one begins.  
