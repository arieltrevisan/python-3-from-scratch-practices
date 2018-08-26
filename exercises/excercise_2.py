class Fruit(object):
    def __init__(self):
        print("Creating fruit")

    def nutrition(self):
        print("You should eat more of these.")

    def fruit_shape(self):
        print("Random shape")


class Orange(Fruit):
    def __init__(self):
        print("Creating Orange")

    def nutrition(self):
        print("Lots of vitamin C, sweet and acid.")

    def color(self):
        print("Color: Orange, duh!")


fruit = Fruit()
fruit.nutrition()
fruit.fruit_shape()

orange = Orange()
orange.nutrition()
orange.fruit_shape()
orange.color()
