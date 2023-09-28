# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- In it's current state, MObject is a concrete class. The clearest indicator of this is that it does not implement ABC. 
	Otherwise, any lower level object that would derivce from it would be an MObject, but an MObject can still exist. By making it abstract, no lower-level object can ever just be an MObject but one that also implements lower-level methods that might be necessary.

1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- This method is called when an instance is about to be destroyed/removed. If this is called from an inheretied class, it will look to call the base classes __del__ method so that it is properly removed. Sometimes, it may postpone the destruction of the instance by creating a reference to it, this is called resurrection, and I do not fully understand it. 

1. What class does Texture inherit from?
	- Image.

1. What methods and attributes does the Texture class inherit from 'Image'? 
	- It inherits every method: getHeight, getWeight, getPixels, getPixelColorR, setPixelsToRandomValue and every attribute: m_width, m_height, m_colorChannels, m_Pixels.

1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- I believe that a Texture should have a 'is-a' relationships with 'Image'. I believe this because I believe an Image should be able to be instantiated without needing a Texture. If anything, an Image might want to have a has-a relationship with Texture, but this would depend on the implementation of Texture and what other abstract classes and methods that one could define to describe an image.

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes - Python automatically creates a constructor for us. Additionally, if a class, like Texture, is derived from a base class and a constructor is not defined, it will assume the constructor of the parent in order to create itself. 

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

	They are not. This is because a thread may reads that there is no existing instance of the singleton and start to create one, but another thread does the same before the first instance was stored. I am not sure if this is a Python specific issue, or just a singleton design pattern issue. 
  
