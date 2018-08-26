import keyword

# Keywords (reserved)
print(keyword.kwlist)

# Type
a = "nyc"
print(type(a))
print(a)

# Reference
c = 'nyc'
d = c
print(c == d)
print(d is c)

# Assignments
a = b = c = 10
print(a)
print(b)
print(c)
x, y, z = 20, 30, 40
print(x)
print(y)
print(z)

# Global Scope
a = 10


def test():
    global a
    print("Value of a:", a)
    a = 5
    print("Value of a:", a)


test()
print("Value outside:", a)
