Dictionary can store any two kinds of information that can be matched up.  
Use the del statement to completely remove a key-value pair. eg. del dict['name']  
When you know you’ll need more than one line to define a dictionary, press enter after the opening brace. Then indent the next line one level (four spaces), and write the first key-value pair, followed by a comma. Once you’ve finished defining the dictionary, add a closing brace on a new line after the last key-value pair and indent it one level so it aligns with the keys in the dictionary. It’s good practice to include a comma after the
last key-value pair as well. eg.
```
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
```
For dictionaries, specifically, you can use the get() method to set a default value that will be returned if the requested key doesn’t exist. get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist. eg.
```
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
```
