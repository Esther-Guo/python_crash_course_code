numbers = list(range(1, 6)) # numbers = [1,2,3,4,5]  
If you pass a third argument to range(), Python uses that value as a step size when generating numbers. list(range(2, 11, 2)) # [2,4,6,8,10]  
min(),max(),sum() for numerical list.  
**list comprehension**: combines the for loop and the creation of new elements into one line, and automatically appends each new element. eg. squares = [value**2 for value in range(1, 11)]  
copy lists: A = B (actually the same list), A = B[:] (two seperate lists)  
An immutable(unchanged) list is called a tuple.  
To change a tuple, assign a new value to the variable.  
Style guideline:
[ ]use four spaces per indentation level
[ ]each line should be less than 79 characters
[ ]limit all of your comments to 72 characters per line
[ ]To group parts of your program visually, use blank lines