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