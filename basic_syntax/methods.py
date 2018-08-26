# parameters with default values
def sum_num_1(par1=1, par2=2) -> float:
    return par1 + par2 * 1.0


# parameters with default values and type hints
def sum_num_2(par1: int = 1, par2: int = 2) -> int:
    return par1 + par2


# variable number of parameters: asterisk
# *args does NOT necessarily needs to be named args
# args is a variable-length non-keyworded argument list
def sum_num_3(*args):
    print("args:", args)
    return sum(args)


# variable number of parameters: double asterisk
# **kwargs does NOT necessarily needs to be named kwargs
# kwargs is a variable-length argument dictionary
def sum_num_4(**kwargs):
    print("kwargs:", kwargs)
    result = 0
    for k, v in kwargs.items():
        if type(v) is int:
            result += v
    return result


print(sum_num_1())  # uses default values
print(sum_num_1(2))  # sends par1
print(sum_num_1(par2=3))  # sends par2
print(sum_num_1(4, 5))  # par1, then par2
print(sum_num_1(par2=5, par1=7))  # par2, then par1

print(sum_num_3(1, 2, 3, 4, 5))

print(sum_num_4(his_name="Ramon", his_age=40, her_name="Florinda", her_age=42))

