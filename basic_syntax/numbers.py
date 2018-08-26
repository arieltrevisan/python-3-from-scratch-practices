"""
Number operations
"""


def print_type(val):
    print(type(val), end=': ')


int_num = 2
print_type(int_num)
print(int_num)

float_num = 3.0
print_type(float_num)
print(float_num)

add = int_num + float_num
print_type(add)
print(add)

sub = int_num - float_num
print_type(sub)
print(sub)

mul = int_num * float_num
print_type(mul)
print(mul)

div = int_num / float_num
print_type(div)
print(div)

exponent = 10 ** 2
print_type(exponent)
print(exponent)

modulo = 100 % 3
print_type(modulo)
print(modulo)

