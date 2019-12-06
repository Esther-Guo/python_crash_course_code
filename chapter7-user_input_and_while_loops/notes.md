Each time you use the input() function, you should include a clear, easy-to follow prompt that tells the user exactly what kind of information you’re looking for. `name = input("Please enter your name: ")`
To build your prompt over several lines: ```
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
```
When you use the input() function, Python interprets everything the user enters as a string. Sometimes we need to use the int() function for numerical input, which tells Python to treat the input as a numerical value.  
modulo operator: %.  
Use flag in while loop if there are many different events could cause the program to stop running. We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False.  
To exit a loop immediately without running any remaining code in the while loop, use the **break** statement.  
Use the **continue** statement to return to the beginning of the loop based on the result of a conditional test.  
