class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __lt__(self, other):
        return self.area() < other.area()


r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)

if r1 < r2:
    print("First rectangle is smaller")
else:
    print("Second rectangle is smaller")