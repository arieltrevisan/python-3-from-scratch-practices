# SETS
# They cannot contain duplicate elements
nums = {1, 2, 1, 3, 1, 4, 5, 6}
empty_set = set()
print(nums)

# You add using add(), not append()
nums.add(7)
nums.remove(3)
print(nums)

first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

# Union
print(first | second)

# Intersection
print(first & second)

# Difference - found on 1st, not on 2nd
print(first - second)

# Difference - found on 2nd, not on 1st
print(second - first)

# Symmetric Different - item is in either set, but not both
print(first ^ second)
