class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w


    def rectangle_area(self):
        return self.length * self.width

rectangle_9 = Rectangle(15, 10)
print(rectangle_9.rectangle_area())