# -- while, for

li = []
x = 0
while x < 10:
    li.append(x)
    x += 1
print("while: %s" % li)

li.clear()
x = 0
for x in range(0, 10):
    li.append(x)
    x += 1
print("  for: %s" % li)

list1 = [1, 2, 3]
list2 = [4, 5, 6, 7, 8]
for x, y in zip(list1, list2):
    print("zip", x, y, end=' | ')
print()

# -- while-else, for-else

li.clear()
x = 0
while x < 10:
    if x == 5:
        break
    li.append(x)
    x += 1
else:
    print("while 1 did NOT break")
print("while 1: %s" % li)

li.clear()
x = 0
while x < 10:
    if x == 10:
        break
    li.append(x)
    x += 1
else:
    print("while 2 did NOT break")
print("while 2: %s" % li)

li.clear()
x = 0
while x < 10:
    x += 1
    if x > 5:
        continue
    li.append(x-1)
else:
    print("while 3 did NOT break, but it did continue")
print("while 3: %s" % li)
