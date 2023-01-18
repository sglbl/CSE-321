array = [5, 15, 23, 18, 7, 22]
x = 5

set = set()

for i in array:
    if abs(i - x) in set:
        print(i, " and ", i-x)
    if abs(i + x) in set:
        print(i+x, " and ", i)
    set.add(i)