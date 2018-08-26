class Shape(object):
    _number_of_sides = 0

    def __init__(self, sides):
        self._number_of_sides = len(sides)

    @property
    def num_of_sides(self):
        return self._number_of_sides


class Rectangle(Shape):
    _protected_prop = "protected, starts with 1 underscore"
    __private_prop = "private, starts with 2 underscores"

    def __init__(self, width, height):
        super().__init__([width, height, width, height])
        self._max_size = 10
        self.width = width
        self.height = height

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, value):
        if value:
            password = input("Enter the password: ")
        if password == "boom":
            self._max_size = value
        else:
            print("Invalid password. Cannot change max_size.")

    def calculate_area(self):
        return self.width * self.height

    # cls is an object that holds class itself, not an instance!
    @classmethod
    def create_square(cls, side_length):
        return cls(side_length, side_length)

    @staticmethod
    def print_size(width, height):
        print("Size is: ({}x{})".format(width, height))

    @staticmethod
    def print_area(area):
        print("Area is:", area)


class Square(Rectangle):

    def __init__(self, side_len):
        super().__init__(side_len, side_len)


rec = Rectangle(5, 4)
Rectangle.print_size(5, 4)
Rectangle.print_area(rec.calculate_area())
print("Sides:", rec.num_of_sides)

squ = Square(4)
print("Square area:", squ.calculate_area())
print("Square sides:", squ.num_of_sides)
