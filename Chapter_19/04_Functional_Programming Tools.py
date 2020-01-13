# Functional programing Tools
# Mapping Functions over Iterables: map

counters = [1, 2, 3, 4]

updated = []
for x in counters:
    updated.append(x + 10)  # add 10 to each item

print(updated)


def inc(x): return x + 10  # Function to be run


L = list(map(inc, counters))  # Collect results
print(L)

L = list(map((lambda x: x + 3), counters))  # Function expression
print(L)


def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res


L = list(map(inc, [1, 2, 3]))  # Built-in is an iterable
print(L)

L = mymap(inc, [1, 2, 3])  # Our builds a list (see generators)
print(L)

print(pow(3, 4))  # 3**4

L = list(map(pow, [1, 2, 3], [2, 3, 4]))  # 1**2, 2**3, 3**4
print(L)

L = list(map(inc, [1, 2, 3, 4]))
print(L)
L = [inc(x) for x in [1, 2, 3, 4]]  # Use () parens to generate items instead
print(L)
I = (inc(x) for x in [1, 2, 3, 4])
print(I.__next__())
print(I.__next__())

# Selecting Items in iterables: filter


