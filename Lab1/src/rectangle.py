from abc import ABC, abstractmethod

"""
 Sample modified from CS5500, Mike Shah

 A rectangle class
 Note that there is no constructor or destructor,
 so a default one will be created for us.
"""

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def set_values(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_values(self, x, y):
        self._width = x
        self._height = y
    
    def get_values(self):
        return (self._width, self._height)

    def area(self):
        return self._width * self._height


if __name__ == "__main__":
    # Create a rectangle object
    rect = Rectangle(5, 8)

    # Call a member function
    rect.set_values(3, 4)

    # Print out the area function
    print("area:", rect.area())
