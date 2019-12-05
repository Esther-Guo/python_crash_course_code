Each time you use the input() function, you should include a clear, easy-to follow prompt that tells the user exactly what kind of information you’re looking for. `name = input("Please enter your name: ")`
To build your prompt over several lines: ```
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
```
When you use the input() function, Python interprets everything the user enters as a string. Sometimes we need to use the int() function for numerical input, which tells Python to treat the input as a numerical value.  
modulo operator: %. 