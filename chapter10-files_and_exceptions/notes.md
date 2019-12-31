load the entire file:
```
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())  # remove the empty line in the end
```
file path: always use slash/ rather than backslash\ because Win sucks.  
If using absolute file path, assign it to a variable and use the variable instead.  
read file line by line:
```
with open(filename) as file_object:
    for line in file_object:
    print(line.rstrip())
```
`lines = file_object.readlines()`store the file’s lines in a list called `lines`.  
write to a file:
```
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
```
'w'-write 'r'-read(default) 'a'-append 'r+'-read and write  
If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.  
Exceptions are handled with try-except blocks.  
```
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```
Any code that depends on the try block executing successfully goes in the else block.  
The only code that should go in a try block is code that might cause an exception to be raised.  
To make a program fail silently:
```
try:
    --snip--
except FileNotFoundError:
    pass
else:
    --snip--
```
