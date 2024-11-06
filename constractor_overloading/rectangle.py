class Rectangle:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length  # Square if width is None

    def area(self):
        return self.length * self.width

# Example usage
square = Rectangle(5)
rectangle = Rectangle(5, 10)
print("Square Area:", square.area())
print("Rectangle Area:", rectangle.area())
