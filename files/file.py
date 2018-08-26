"""
'r' : use for reading
'w' : use for writing
'x' : use for creating and writing to a new file
'a' : use for appending to a file
'r+' : use for reading and writing to the same file
"""

# read all lines and return a list
with open("test_file.txt", 'r') as f:
    print(type(f.readlines()))

# read all content
with open("test_file.txt", 'r') as f:
    print(type(f.read()))

# read line by line
with open("test_file.txt", 'r') as f:
    for line in f:
        print(line.rstrip('\n'), len(line))

print("*" * 20)

lines = ["Line 1", "Line 2", "Line 3"]
with open("write_file.txt", 'w') as f:
    for line in lines:
        f.write(line + "\n")
