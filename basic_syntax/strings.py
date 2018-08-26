# strings and escaping chars
a = "String One"
b = 'String Two'
c = "string with 'quotes' here"
d = 'string with "quotes" here'
e = "string with \"quotes\" here"
f = 'string with \'quotes\' here'
g = "string that continues\
 in next line one"
h = 'string that continues' \
    ' in next line two'

# METHODS
# prints 5
print(len("hello"))
# prints "spam, eggs, ham"
print(", ".join(["spam", "eggs", "ham"]))
# prints "Hello world"
print("Hello ME".replace("ME", "world"))
# prints "True"
print("This is a sentence.".startswith("This"))
# prints "True"
print("This is a sentence.".endswith("sentence."))
# prints "THIS IS A SENTENCE."
print("This is a sentence.".upper())
# prints "an all caps sentence"
print("AN ALL CAPS SENTENCE".lower())
# prints "['spam', 'eggs', 'ham']"
print("spam, eggs, ham".split(", "))

# substrings / slicing
st = "0123456789"
print("01." + st[:])  # all
print("02." + st[0:])  # all from start
print("03." + st[0:5])  # from ix 0 to 4
print("04." + st[2:6])  # from ix 2 to 5
print("05." + st[-2])  # at ix 2, counting backwards
print("06." + st[-2:])  # from -2 counted backwards, to end
print("07." + st[:-2])  # from start, up to -2 from end
print("08." + st[::-1])  # reverse the string
print("09." + st[0:5:2])  # step: 2

# format / formatting
nums = [4, 5, 6]
print("Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2]))
print("Numbers: {0} {1}".format(nums[0], nums[1], nums[2]))
print("Numbers: {0} {1} {2}".format(nums[0], nums[1], nums[2], 7))

print("{x}, {y}, {z}".format(z=1, x=5, y=12))

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
result = 'Coordinates: {latitude}, {longitude}'.format(**coord)
print(result)
