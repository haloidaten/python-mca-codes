
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def compare(self, other):
        if self.area() > other.area():
            print("First rectangle has greater area")
        elif self.area() < other.area():
            print("Second rectangle has greater area")
        else:
            print("Both rectangles have equal area")


r1 = Rectangle(10, 5)
r2 = Rectangle(8, 6)

print("Rectangle 1:")
print("Area:", r1.area())
print("Perimeter:", r1.perimeter())

print("\nRectangle 2:")
print("Area:", r2.area())
print("Perimeter:", r2.perimeter())

r1.compare(r2)
 