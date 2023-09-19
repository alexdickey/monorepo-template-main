# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? 
  - A good example would be a function called 'pop' which only removes one element.
  - A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

ANSWER: I found that the names of the member functions of both list and dict correlate to what they did, perhaps list was a little bit more clear/easier to intuit. Functions such as append, extend, or even *= seemed to make logical sense. 

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

ANSWER: A dictionary differs from a list in that every element in a dictionary is made up from a key : value pair. The key can be represented by any immuteable data type, meaning it won't change and can be compared, while the value can be made up of anything, including a list or another dictionary.

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

ANSWER: A list does allow for random access. Items stored in a list are stored at a certain location and can be accessed by their index. 

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

ANSWER: Starting with the pros, it makes them very flexible in their use case, easier to understand and utilize, and useful for API implementation. Perhaps some cons would be if there is a necesity for homogenization or if you were uncertain of what would be stored in the list itself, you wouldn't know to perform one operation versus another. 

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

ANSWER: request, head, get, post, put, patch, delete. I would say that all of these are well named as I can intuit what they do aside from head which, lacking context, I do not think I would be able to guess what a head request would be.

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

ANSWER: The member function request has the most member functions. I believe this is because you can request many different things, and it additionally can use any of the other functions as its first argument. In a way, this API feels very concise and clean and anything that perhaps doesn't fit into another category is placed here which may cause some confusion.

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

ANSWER: **kwargs is the key word argument for taking an arbitrary number of keyword argyments. This can be great because it allows for flexible API design so that you do not have to account for every combination of keyword argument number or to pass on these arguments to a method. Additionally, the user has to specify what keyword they are trying to assign, making it so they cannot mess up the data on accident. 

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?

ANSWER: I would assume that many arguments are set to None, python's NULL signature, because unless a kwarg specifies what they should be, the arguments do not want to be used or considered. The arguments could be set to anthing besides "None" using a kwarg. and it might be good to set an argument to a predetermined value such as None because in source code their are conditionals that depend on if those values have information in them or not. 
