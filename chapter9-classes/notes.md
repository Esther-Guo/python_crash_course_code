In object-oriented programming you write **classes** that represent real-world things and situations, and you create **objects** based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.  
Making an object from a class is called **instantiation**, and you work with **instances** of a class.  
By convention, capitalized names refer to classes in Python. eg.Dog  
Write doctring for each class you define.  
The \__init__() method is a special method that Python runs automatically whenever we create a new instance based on the class.  
The self parameter is required in the method definition, and it must come first before the other parameters.  
3 ways to modify attributes' values: change directly, through method, increment through method.  
When one class inherits from another, it takes on the attributes and methods of the first class and it’s also free to define new attributes and methods of its own.  
When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.  
The name of the parent class must be included in parentheses in the definition of a child class.  
To override methods from the parent class, define a method in the child class with the same name as the method you want to override in the parent class.  
Class names should be written in CamelCase. To do this, capitalize the first letter of each word in the name, and don’t use underscores.  
Instance and module names should be written in lowercase with underscores between words.  
Every class, function and module should have a docstring immediately following the class definition.  
Within a class you can use one blank line between methods, and within a module you can use two blank lines to separate classes.  
Always place the import statement for the standard library module first. Then add a blank line and the import statement for the module you wrote.  