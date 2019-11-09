print((1, 2) + (3, 4))  # Concatenation
print((1, 2) * 4)  # Repetition
T = (1, 2, 3, 4)  # Indexing, slicing
print(T[0], T[1:3])

x = (40)  # An integer
print(x)

y = (40,)  # A tuple containing an integer
print(y)

T = ('cc', 'aa', 'dd', 'bb')
tmp = list(T)  # Make a list from a tuples items
tmp.sort()  # sort the list
print(tmp)

T = tuple(tmp)  # Make a tuple from the lists items
print(T)

print(sorted(T))  # Or use the sorted built-in and save two steps
print(type(sorted(T)))

