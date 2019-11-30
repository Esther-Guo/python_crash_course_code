A list is a collection of items in a particular order.  
It’s a good idea to make the name of your list plural, such as letters, digits, or names, since a list usually contains more than one element.  
Add a new element at any position in your list by using the insert() method. eg.motorcycles.insert(0, 'ducati')  
If you know the position of the item you want to remove from a list(and never use it), you can use the del statement. eg.del motorcycles[0]  
The pop() method removes the last item in a list, but it lets you work with that item after removing it. pop(index) allows you to remove an element in any particular position.  
If you only know the value of the item you want to remove, you can use the
remove() method.  
The sort() method changes the order of the list permanently. You can also sort this list in reverse alphabetical order by passing the **reverse=True** argument to the sort() method.  
The sorted() function lets you display your list in a particular order but doesn’t affect the actual order of the list.  
reverse() simply reverses the order of the list.  
Whenever you want to access the last item in a list(not empty), you use the index -1.  
