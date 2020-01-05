A unit test verifies that one specific aspect of a function’s behavior is correct.  
A test case is a collection of unit tests that together prove that a function behaves as it’s supposed to, within the full range of situations you expect it to handle.  
```
if __name__ == '__main__':
    ---do sth---
```
sometimes you want to write a .py file that can be both used by other programs as a module, and can also be run as the main program itself(in this case, \_name__ is set to '\_main_').